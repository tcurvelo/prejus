# -*- coding: utf-8 -*-
from br.jus.portaltransparencia import enums
from datetime import date
from decimal import Decimal
from xml.etree import ElementTree as ET
import re
import time
import urllib2


url_base = "http://www.portaltransparencia.jus.br/despesas/rLista.php"


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
        map(lambda x: x["valor"], resultados)
    )


def lista_resultados(response):
    try:
        raiz = ET.fromstring(response)
    except ET.ParseError:
        return []

    resultados = []
    for nodo in raiz:
        entrada = {}
        entrada["data"] = nodo.find("data").text
        entrada["documento"] = re.search(
            ">(.*?)<",
            nodo.find("documento").text
        ).group(1)
        entrada["origem"] = nodo.find("origem").text
        entrada["especie"] = nodo.find("especie").text
        entrada["orgaoSuperior"] = nodo.find("orgaoSuperior").text
        entrada["unidade"] = nodo.find("unidade").text
        entrada["favorecido"] = nodo.find("favorecido").text
        entrada["gestora"] = nodo.find("gestora").text
        entrada["fase"] = nodo.find("fase").text
        entrada["valor"] = Decimal(nodo.find("valor").text)
        entrada["elemento"] = nodo.find("elemento").text
        entrada["tipoDocumento"] = nodo.find("tipoDocumento").text
        entrada["codGestao"] = nodo.find("codGestao").text
        entrada["codGestora"] = nodo.find("codGestora").text
        entrada["evento"] = nodo.find("evento").text
        resultados.append(entrada)
    return resultados


def consulta(**kw):
    url = prepara_url(**kw)
    return lista_resultados(
        urllib2.urlopen(url).read()
    )
