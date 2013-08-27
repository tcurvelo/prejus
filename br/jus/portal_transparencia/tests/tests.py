#!/usr/bin/env python
# -*- coding: utf-8 -*-
from br.jus.portal_transparencia import elementos_despesa
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
            self.inicio, self.fim, elementos_despesa.DIARIAS_CIVIL
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
        with open("fixture.xml") as resultado:
            soma = util.sumariza(resultado.read())
        self.assertEquals(soma, Decimal("73718.72"))


class TestaRequest(unittest.TestCase):

    def setUp(self):
        self.fim = datetime.utcnow().replace(day=1) - timedelta(days=1)
        self.inicio = self.fim.replace(day=1)

    def test_pega_diarias(self):
        url = util.prepara_url(
            self.inicio, self.fim,
            elemento = elementos_despesa.DIARIAS_CIVIL
        )

        resultado = urllib2.urlopen(url).read()
        total = util.sumariza(resultado)

        self.assertEquals(total, Decimal("73718.72"))


if __name__ == '__main__':
    unittest.main()
