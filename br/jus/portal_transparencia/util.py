# -*- coding: utf-8 -*-
from decimal import Decimal
from xml.etree import ElementTree as ET
import time

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


def sumariza(resultado):
    raiz = ET.fromstring(resultado)

    soma = Decimal(0)
    for nodo in raiz:
        valor = nodo.find("valor")
        soma+= Decimal(valor.text)

    return soma
