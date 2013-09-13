# -*- coding: utf-8 -*-
from decimal import Decimal
from xml.etree import ElementTree as ET
import time
import re

url_base = "http://www.portaltransparencia.jus.br/despesas/rLista.php"

def prepara_url(inicio, fim, elemento):
    parametros = [
        ("periodoInicio", "%.2d%%2F%.2d%%2F%.4d" % (
                                inicio.day, inicio.month, inicio.year
                          )
        ),

        ("periodoFim", "%.2d%%2F%.2d%%2F%.4d" % (
                            fim.day, fim.month, fim.year
                        )
        ),

        # 'ne' : Empenho
        # 'nl' : Liquidação
        # 'ob' : Pagamento
        ("faseDespesa", "ob"),

        #'15000' : 'Justica do Trabalho'
        ("orgaoSuperior", "15000"),

        #'15114' : "TRT13"
        ("unidadeOrcamentaria", "15114"),

        #'080005' : "TRT13"
        ("unidadeGestora", "080005"),

        #elementoDespesa : "14"
        ("elementoDespesa", elemento),

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


def lista_de_resultados(response):
    raiz = ET.fromstring(response)

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
