#!/usr/bin/env python
# -*- coding: utf-8 -*-

from br.jus.portal_transparencia import enums
from br.jus.portal_transparencia import util
from datetime import datetime, timedelta
from decimal import Decimal
import unittest
import urllib2


class TestaModuleUtil(unittest.TestCase):

    def setUp(self):
        self.inicio = datetime(day=1, month=7, year=2013)
        self.fim = datetime(day=31, month=7, year=2013)

    def test_prepara_url(self):
        url = util.prepara_url(
            self.inicio, self.fim, enums.elementos.DIARIAS_CIVIL.value
        )

        self.assertIn(
            "http://www.portaltransparencia.jus.br/despesas/rLista.php?" +
            "periodoInicio=01%2F07%2F2013&periodoFim=31%2F07%2F2013" +
            "&faseDespesa=ob&orgaoSuperior=15000&unidadeOrcamentaria=15114" +
            "&unidadeGestora=080005&elementoDespesa=14&nd=",
            url,
            ""
        )

    def testa_sumariza(self):
        with open("test_fixture.xml") as response:
            soma = util.totaliza_valor(util.lista_de_resultados(response.read()))
        self.assertEquals(soma, Decimal("73718.72"))


class TestaRequest(unittest.TestCase):

    def setUp(self):
        self.fim = datetime.utcnow().replace(day=1) - timedelta(days=1)
        self.inicio = self.fim.replace(day=1)

    def test_pega_diarias(self):
        url = util.prepara_url(
            self.inicio, self.fim,
            elemento = enums.elementos.DIARIAS_CIVIL.value
        )

        resultados = util.lista_de_resultados(urllib2.urlopen(url).read())

        diarias_filtradas = filter(
            lambda x: x["elemento"] == enums.elementos.DIARIAS_CIVIL.label,
            resultados
        )

        #todos as entradas tem o 'label' de diarias
        self.assertEquals(len(diarias_filtradas), len(resultados))



if __name__ == '__main__':
    unittest.main()