#!/usr/bin/env python
# -*- coding: utf-8 -*-
from br.jus.portaltransparencia import enums
from br.jus.portaltransparencia import despesas
from datetime import datetime, timedelta
from decimal import Decimal
import unittest


class TestaDespesasUtil(unittest.TestCase):

    def setUp(self):
        self.inicio = datetime(day=1, month=7, year=2013)
        self.fim = datetime(day=31, month=7, year=2013)
        self.response = open("test_fixture.xml")

    def tearDown(self):
        self.response.close()

    def test_prepara_url(self):
        url = despesas.prepara_url(
            inicio=self.inicio,
            fim=self.fim,
            elemento = enums.elemento.DIARIAS_CIVIL.value,
            orgaoSuperior = enums.orgaoSuperior.JT.value,
            unidade = enums.unidade.TRT13.value
        )

        self.assertIn(
            "http://www.portaltransparencia.jus.br/despesas/rLista.php?" +
            "periodoInicio=01%2F07%2F2013&periodoFim=31%2F07%2F2013" +
            "&faseDespesa=ob&orgaoSuperior=15000&unidadeOrcamentaria=15114" +
            "&unidadeGestora=&elementoDespesa=14&nd=",
            url,
            ""
        )

    def testa_lista_resultados(self):
        resultados = despesas.lista_resultados(
            self.response.read()
        )
        self.assertEquals(len(resultados), 89)

    def testa_lista_resultados_vazia(self):
        resultados = despesas.lista_resultados("")
        self.assertEquals(len(resultados), 0)

    def testa_sumariza(self):
        soma = despesas.totaliza_valor(
            despesas.lista_resultados(self.response.read())
        )
        self.assertEquals(soma, Decimal("73718.72"))


class TestaConsultas(unittest.TestCase):

    def setUp(self):
        self.fim = datetime.utcnow().replace(day=1) - timedelta(days=1)
        self.inicio = self.fim.replace(day=1)

    def test_pega_diarias(self):
        resultados = despesas.consulta(
            inicio=self.inicio,
            fim=self.fim,
            orgaoSuperior = enums.orgaoSuperior.JT.value,
            unidade = enums.unidade.TRT13.value,
            elemento = enums.elemento.DIARIAS_CIVIL.value,
        )

        diarias_filtradas = filter(
            lambda x: x["elemento"] == enums.elemento.DIARIAS_CIVIL.label,
            resultados
        )

        #todas as entradas sao diarias
        self.assertEquals(len(diarias_filtradas), len(resultados))

        pagamentos_filtrados = filter(
            lambda x: x["fase"] == enums.fase.PAGAMENTO.label,
            resultados
        )

        #todas as entradas sao pagamentos
        self.assertEquals(len(pagamentos_filtrados), len(resultados))


if __name__ == '__main__':
    unittest.main()
