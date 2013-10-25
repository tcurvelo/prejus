#!/usr/bin/env python
# -*- coding: utf-8 -*-
from br.jus.portaltransparencia import despesas
from br.jus.portaltransparencia import enums
from datetime import date, timedelta
from decimal import Decimal

import os
import unittest


class TestaDespesasUtil(unittest.TestCase):

    def setUp(self):
        self.inicio = date(day=1, month=7, year=2013)
        self.fim = date(day=31, month=7, year=2013)
        self.response = open(
            os.path.join(os.path.dirname(__file__), 'test_fixture.xml')
        )

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

    def testa_ordem_dos_campos_resultado(self):
        esperado = (
            '01/07/2013', # data
            '2013OB802053', # documento
            '2013NE000065', # origem
            None, # especie
            'JUSTICA DO TRABALHO', # orgaoSuperior
            'TRIBUNAL REGIONAL DO TRABALHO DA 13A. REGIAO', #unidade
            'ANA PAULA AZEVEDO SA CAMPOS PORTO', # favorecido
            'TRIBUNAL REGIONAL DO TRABALHO DA 13A.REGIAO', # gestora
            'Pagamento', # fase
            Decimal('3946.38'), # valor
            'DIARIAS - PESSOAL CIVIL', # elemento
            u'Ordem Banc\xe1ria (OB)', # tipoDocumento
            '00001', # codGestao
            '080005', # codGestora
            '531335', # evento
        )

        resultados = despesas.lista_resultados(
            self.response.read()
        )

        self.assertEqual(
            resultados.next(),
            esperado
        )

    def testa_lista_resultados(self):
        resultados = despesas.lista_resultados(
            self.response.read()
        )
        self.assertEquals(len(list(resultados)), 89)

    def testa_lista_resultados_vazia(self):
        resultados = despesas.lista_resultados("")
        self.assertEquals(len(list(resultados)), 0)

    def testa_sumariza(self):
        soma = despesas.totaliza_valor(
            despesas.lista_resultados(self.response.read())
        )
        self.assertEquals(soma, Decimal("73718.72"))


class TestaConsultas(unittest.TestCase):

    def setUp(self):
        self.fim = date.today().replace(day=1) - timedelta(days=1)
        self.inicio = self.fim.replace(day=1)

    def test_pega_diarias(self):
        resultados = despesas.consulta(
            inicio=self.inicio,
            fim=self.fim,
            orgaoSuperior = enums.orgaoSuperior.JT.value,
            unidade = enums.unidade.TRT13.value,
            elemento = enums.elemento.DIARIAS_CIVIL.value,
        )

        resultados = list(resultados)

        diarias_filtradas = filter(
            lambda x: x.elemento == enums.elemento.DIARIAS_CIVIL.label,
            resultados
        )

        #todas as entradas sao diarias
        self.assertEquals(len(diarias_filtradas), len(resultados))

        pagamentos_filtrados = filter(
            lambda x: x.fase == enums.fase.PAGAMENTO.label,
            resultados
        )

        #todas as entradas sao pagamentos
        self.assertEquals(len(pagamentos_filtrados), len(resultados))


if __name__ == '__main__':
    unittest.main()
