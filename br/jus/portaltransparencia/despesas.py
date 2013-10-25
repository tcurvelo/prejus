# -*- coding: utf-8 -*-
from br.jus.portaltransparencia import enums
from collections import namedtuple
from datetime import date
from decimal import Decimal
from xml.etree import ElementTree as ET

import csv
import re
import time
import urllib2


url_base = "http://www.portaltransparencia.jus.br/despesas/rLista.php"


Despesa = namedtuple(
    "Despesa",
    """ data documento origem especie orgaoSuperior unidade favorecido gestora
        fase valor elemento tipoDocumento codGestao codGestora evento
    """
)


def prepara_url(**kw):
    inicio = kw["inicio"] if "inicio" in kw else date.today()
    fim = kw["fim"] if "fim" in kw else date.today()

    parametros = [
        ("periodoInicio", "%.2d%%2F%.2d%%2F%.4d" % (
            inicio.day, inicio.month, inicio.year
        )),
        ("periodoFim", "%.2d%%2F%.2d%%2F%.4d" % (
            fim.day, fim.month, fim.year
        )),
        ("faseDespesa",
            kw["fase"] if "fase" in kw else enums.fase.PAGAMENTO.value
        ),
        ("orgaoSuperior",
            kw["orgaoSuperior"] if "orgaoSuperior" in kw else
                enums.orgaoSuperior.TODOS.value
        ),
        ("unidadeOrcamentaria",
            kw["unidade"] if "unidade" in kw else enums.unidade.TODOS.value
        ),
        ("unidadeGestora",
            #FIXME
            # kw["gestora"] if "gestora" in kw else enums.gestora.TODOS.value
            enums.gestora.TODOS.value
        ),
        ("elementoDespesa",
            kw["elemento"] if "elemento" in kw else enums.elemento.TODOS.value
        ),
        ("nd", str(int(time.time()*1000)) )
    ]

    url = url_base + "?" + "&".join(
        ["=".join([k, v]) for k, v in parametros]
    )

    return url


def totaliza_valor(resultados):
    return reduce(
        lambda x, y: x + y,
        map(lambda x: x.valor, resultados)
    )


def lista_resultados(response):
    try:
        lista = ET.parse(response)
        for nodo in lista.iter(tag='ob'):
            despesa = Despesa(
                data=nodo.find("data").text,
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
            )
            yield despesa
    except Exception:
        return


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
    url = prepara_url(**kw)
    return lista_resultados(
        urllib2.urlopen(url)
    )
