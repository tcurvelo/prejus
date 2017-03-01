# -*- coding: utf-8 -*-
from prejus import despesas, enums
from datetime import date, timedelta
from decimal import Decimal

import os


data_inicio = date(day=1, month=7, year=2013)
data_fim = date(day=31, month=7, year=2013)
fixture_path=os.path.join(os.path.dirname(__file__), 'fixtures', '{}')
response = open(fixture_path.format('test_fixture.xml')).read()
empty_response = open(fixture_path.format('test_fixture_vazio.xml')).read()


def testa_prepara_params_para_consulta():
    params = despesas.prepara_params(
        inicio=data_inicio,
        fim=data_fim,
        elemento = enums.Elemento.DIARIAS_CIVIL,
        orgaoSuperior = enums.OrgaoSuperior.JT,
        unidade = enums.Unidade.TRT13,
    )

    expected = set([
        ('periodoInicio', '01/07/2013'),
        ('periodoFim', '31/07/2013'),
        ('faseDespesa', 'ob'),
        ('orgaoSuperior', '15000'),
        ('unidadeOrcamentaria', '15114'),
        ('unidadeGestora', ''),
        ('elementoDespesa', '14'),
        # ('nd', ''),
    ])
    params_set = set(params.items())

    assert expected.issubset(params_set)


def testa_ordem_dos_campos_do_resultado():
    expected = despesas.Despesa(
        data=date(2013, 7, 1),
        documento='2013OB802053',
        origem='2013NE000065',
        especie=None,
        orgaoSuperior='JUSTICA DO TRABALHO',
        unidade='TRIBUNAL REGIONAL DO TRABALHO DA 13A. REGIAO',
        favorecido='ANA PAULA AZEVEDO SA CAMPOS PORTO',
        gestora='TRIBUNAL REGIONAL DO TRABALHO DA 13A.REGIAO',
        fase='Pagamento',
        valor=Decimal('3946.38'),
        elemento='DIARIAS - PESSOAL CIVIL',
        tipoDocumento=u'Ordem Banc\xe1ria (OB)',
        codGestao='00001',
        codGestora='080005',
        evento='531335',
    )

    resultados = despesas.lista_resultados(response)
    assert resultados[0] == expected


def testa_lista_resultados():
    resultados = despesas.lista_resultados(response)
    assert len(list(resultados)) ==  89


def testa_lista_resultados_vazia():
    resultados = despesas.lista_resultados(empty_response)
    assert len(list(resultados)) == 0


def testa_totaliza_valor():
    total = despesas.totaliza_valor(despesas.lista_resultados(response))
    assert total == Decimal("73718.72")


#FIXME: mockar o resultado desse request, sem realizá-lo de fato
def test_pega_diarias():
    inicio = date(2013, 8, 1)
    fim = date(2013, 8, 31)
    resultados = despesas.consulta(
        inicio=inicio,
        fim=fim,
        orgaoSuperior = enums.OrgaoSuperior.JT,
        unidade = enums.Unidade.TRT13,
        elemento = enums.Elemento.DIARIAS_CIVIL,
    )

    # confirma o total de resultados
    total = 158
    assert len(resultados) == total

    diarias_filtradas = filter(
        lambda x: x.elemento == enums.Elemento.DIARIAS_CIVIL.label,
        resultados
    )

    #todas as entradas sao diarias
    assert len(list(diarias_filtradas)) == total

    pagamentos_filtrados = filter(
        lambda x: x.fase == enums.Fase.PAGAMENTO.label,
        resultados
    )

    #todas as entradas sao pagamentos
    assert len(list(pagamentos_filtrados)) == total

#FIXME: mockar uma consulta a data futura, sem fazer o request
def testa_consulta_invalida():
    resultados = despesas.consulta(
        # inicio e fim como datas futuras
        inicio=date.today() + timedelta(days=1),
        fim=date.today() + timedelta(days=2),
        orgaoSuperior=enums.OrgaoSuperior.JT,
        fase=enums.Fase.PAGAMENTO,
    )

    assert isinstance(resultados, list)
    assert len(resultados) == 0

