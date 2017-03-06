# -*- coding: utf-8 -*-
from collections import namedtuple
from datetime import date, datetime
from decimal import Decimal
from functools import reduce
from prejus import enums
from xml.etree import cElementTree as ET

import csv
import re
import requests
import time


URL_BASE = 'http://www.portaltransparencia.jus.br/portaltransparencia/despesas/rLista.php'


Despesa = namedtuple(
    "Despesa",
    """ data documento origem especie orgaoSuperior unidade favorecido gestora
        fase valor elemento tipoDocumento codGestao codGestora evento
    """
)


def prepara_params(inicio=date.today(), fim=date.today(),
                fase=enums.Fase.PAGAMENTO,
                orgaoSuperior=enums.OrgaoSuperior.TODOS,
                unidade=enums.Unidade.TODOS,
                elemento=enums.Elemento.TODOS,
                ):
    params ={
        'periodoInicio': inicio.strftime('%d/%m/%Y'),
        'periodoFim': fim.strftime('%d/%m/%Y'),
        'faseDespesa': fase.cod,
        'orgaoSuperior': orgaoSuperior.cod,
        'unidadeOrcamentaria': unidade.cod,
        'unidadeGestora': enums.Gestora.TODOS.cod,
        'elementoDespesa': elemento.cod,
        'nd': str(int(time.time()*1000)),
    }

    return params


def totaliza_valor(resultados):
    return reduce(
        lambda x, y: x + y,
        map(lambda x: x.valor, resultados)
    )


def lista_resultados(text):
    try:
        lista = ET.fromstring(text)
        return [
            Despesa(
                data=datetime.strptime(
                    nodo.find("data").text,
                    '%d/%m/%Y'
                ).date(),
                documento=re.search(
                    ">(.*?)<",
                    nodo.find("documento").text
                ).group(1),
                origem=nodo.find("origem").text,
                especie=nodo.find("especie").text,
                orgaoSuperior=nodo.find("orgaoSuperior").text,
                unidade=nodo.find("unidade").text,
                favorecido=nodo.find("favorecido").text,
                gestora=nodo.find("gestora").text,
                fase=nodo.find("fase").text,
                valor=Decimal(nodo.find("valor").text),
                elemento=nodo.find("elemento").text,
                tipoDocumento=nodo.find("tipoDocumento").text,
                codGestao=nodo.find("codGestao").text,
                codGestora=nodo.find("codGestora").text,
                evento=nodo.find("evento").text,
            ) for nodo in lista
        ]
    except ET.ParseError as e:
        return []


def salva_csv(resultados, arquivo="resultados.csv"):

    cabecalho = [
        'data', 'documento', 'origem', 'especie', 'orgaoSuperior', 'unidade',
        'favorecido', 'gestora', 'fase', 'valor', 'elemento', 'tipoDocumento',
        'codGestao', 'codGestora', 'evento'
    ]

    # abre o arquivo para escrita, com buffer de linha
    with open(arquivo, "w", 1) as csvfile:
        writer = csv.writer(
            csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL
        )
        writer.writerow(cabecalho)
        writer.writerows(resultados)


def consulta(**kw):
    params = prepara_params(**kw)
    response = requests.get(URL_BASE, params=params)

    if response.status_code != 200:
        resultados = []
    else:
        resultados = lista_resultados(response.text)

    response.close()
    return resultados
