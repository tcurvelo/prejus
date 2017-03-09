# -*- coding: utf-8 -*-
from datetime import date, datetime
from decimal import Decimal
from functools import reduce
from prejus import enums
from xml.etree import cElementTree as ET

import re
import requests
import time


URL_BASE = 'http://www.portaltransparencia.jus.br/portaltransparencia/despesas/rLista.php'


HEADERS = [
   'data', 'documento', 'origem', 'especie', 'orgaoSuperior', 'unidade',
   'favorecido', 'gestora', 'fase', 'valor', 'elemento', 'tipoDocumento',
   'codGestao', 'codGestora', 'evento'
]


def prepara_params(
    inicio=date.today(), fim=date.today(),
    fase=enums.Fase.PAGAMENTO,
    orgaoSuperior=enums.OrgaoSuperior.TODOS,
    unidade=enums.Unidade.TODOS,
    elemento=enums.Elemento.TODOS,
    ):
    return {
        'periodoInicio': inicio.strftime('%d/%m/%Y'),
        'periodoFim': fim.strftime('%d/%m/%Y'),
        'faseDespesa': fase.cod,
        'orgaoSuperior': orgaoSuperior.cod,
        'unidadeOrcamentaria': unidade.cod,
        'unidadeGestora': enums.Gestora.TODOS.cod,
        'elementoDespesa': elemento.cod,
        'nd': str(int(time.time()*1000)),
    }


def lista_resultados(text):
    result = []

    try:
        document = ET.fromstring(text)
    except ET.ParseError:
        return result

    for node in document:
        despesa = dict()
        for header in HEADERS:
            despesa[header] = node.find(header).text

        if not despesa['data'] or not despesa['documento']:
            continue

        despesa['data'] = datetime.strptime(despesa['data'], '%d/%m/%Y').date()
        despesa['documento'] = re.search('>(.*?)<', despesa['documento']).group(1)
        despesa['valor'] = Decimal(despesa['valor'])

        result.append(despesa)

    return result


def consulta(**kw):
    params = prepara_params(**kw)
    response = requests.get(URL_BASE, params=params)

    if response.status_code != 200:
        resultados = []
    else:
        resultados = lista_resultados(response.text)

    response.close()
    return resultados
