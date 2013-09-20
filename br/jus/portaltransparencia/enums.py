#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import namedtuple
Item = namedtuple('Item', 'value label')

def Enum(**enums):
    return type("Enum", (), enums)

elemento = Enum(
    TODOS =  Item(value="", label= u"Todos"),
    APOSENTADORIAS_E_REFORMAS = Item(value="01", label= u"APOSENT.RPPS, RESER.REMUNER. E REFOR.MILITAR"),
    AQUISICAO_DE_IMOVEIS = Item(value="61", label= u"Aquisição de Imóveis"),
    AQUISICAO_DE_PRODUTOS_PARA_REVENDA = Item(value="62", label= u"Aquisição de Produtos para Revenda"),
    AQUISICAO_DE_TITULOS_DE_CREDITO = Item(value="63", label= u"Aquisição de Títulos de Crédito"),
    AQUISICAO_DE_TITULOS_REPRESENTATIVOS_DE_CAPITAL_JA_INTEGRALIZADO = Item(value="64", label= u"Aquisição de Títulos Representativos de Capital já Integralizado"),
    ARRENDAMENTO_MERCANTIL = Item(value="38", label= u"Arrendamento Mercantil"),
    AUXILIO_FINANCEIRO_A_ESTUDANTES = Item(value="18", label= u"Auxílio Financeiro a Estudantes"),
    AUXILIO_FINANCEIRO_A_PESQUISADORES = Item(value="20", label= u"Auxílio Financeiro a Pesquisadores"),

    AUXILIO_ALIMENTACAO = Item(value="46", label= u"AUXILIO-ALIMENTACAO"),

    AUXILIO_FARDAMENTO = Item(value="19", label= u"Auxílio-Fardamento"),
    AUXILIOS = Item(value="42", label= u"Auxílios"),

    AUXILIO_TRANSPORTE = Item(value="49", label= u"AUXILIO-TRANSPORTE"),

    BENEFICIO_MENSAL_AO_DEFICIENTE_E_AO_IDOSO = Item(value="06", label= u"Benefício Mensal ao Deficiente e ao Idoso"),
    CONCESSAO_DE_EMPRESTIMOS_E_FINANCIAMENTOS = Item(value="66", label= u"Concessão de Empréstimos e Financiamentos"),
    CONSTITUICAO_OU_AUMENTO_DE_CAPITAL_DE_EMPRESAS = Item(value="65", label= u"Constituição ou Aumento de Capital de Empresas"),
    CONTRATACAO_POR_TEMPO_DETERMINADO = Item(value="04", label= u"Contratação por Tempo Determinado"),
    CONTRIBUICAO_A_ENTIDADES_FECHADAS_DE_PREVIDENCIA = Item(value="07", label= u"Contribuição a Entidades Fechadas de Previdência"),
    CONTRIBUICOES = Item(value="41", label= u"Contribuições"),
    CORRECAO_MONETARIA_DA_DIVIDA_DE_OPERACOES_DE_CREDITO_POR_ANTECIPACAO_DE_RECEITA = Item(value="75", label= u"Correção Monetária da Dívida de Operações de Crédito por Antecipação de Receita"),
    CORRECAO_MONETARIA_OU_CAMBIAL_DA_DIVIDA_CONTRATUAL_RESGATADA = Item(value="73", label= u"Correção Monetária ou Cambial da Dívida Contratual Resgatada"),
    CORRECAO_MONETARIA_OU_CAMBIAL_DA_DIVIDA_MOBILIARIA_RESGATADA = Item(value="74", label= u"Correção Monetária ou Cambial da Dívida Mobiliária Resgatada"),
    DEPOSITOS_COMPULSORIOS = Item(value="67", label= u"Depósitos Compulsórios"),

    DESPESAS_DE_EXERCICIOS_ANTERIORES = Item(value="92", label= u"DESPESAS DE EXERCICIOS ANTERIORES"),
    DIARIAS_CIVIL = Item(value="14", label= u"DIARIAS - PESSOAL CIVIL"),

    DIARIAS_MILITAR = Item(value="15", label= u"Diárias - Militar"),
    DISTRIBUICAO_CONSTITUCIONAL_OU_LEGAL_DE_RECEITAS = Item(value="81", label= u"Distribuição Constitucional ou Legal de Receitas"),
    ENCARGOS_PELA_HONRA_DE_AVAIS_GARANTIAS_SEGUROS_E_SIMILARES = Item(value="27", label= u"Encargos pela Honra de Avais, Garantias, Seguros e Similares"),
    ENCARGOS_SOBRE_OPERACOES_DE_CREDITO_POR_ANTECIPACAO_DA_RECEITA = Item(value="25", label= u"Encargos sobre Operações de Crédito por Antecipação da Receita"),
    EQUALIZACAO_DE_PRECOS_E_TAXAS = Item(value="45", label= u"Equalização de Preços e Taxas"),
    EQUIPAMENTOS_E_MATERIAL_PERMANENTE = Item(value="52", label= u"Equipamentos e Material Permanente"),
    INDENIZACAO_PELA_EXECUCAO_DE_TRABALHOS_DE_CAMPO = Item(value="95", label= u"Indenização pela Execução de Trabalhos de Campo"),

    INDENIZACOES_E_RESTITUICOES = Item(value="93", label= u"INDENIZACOES E RESTITUICOES"),

    INDENIZACOES_E_RESTITUICOES_TRABALHISTAS = Item(value="94", label= u"Indenizações e Restituições Trabalhistas"),
    JUROS_SOBRE_A_DIVIDA_POR_CONTRATO = Item(value="21", label= u"Juros sobre a Dívida por Contrato"),
    JUROS_DESAGIOS_E_DESCONTOS_DA_DIVIDA_MOBILIARIA = Item(value="23", label= u"Juros, Deságios e Descontos da Dívida Mobiliária"),

    LOCACAO_DE_MAO_DE_OBRA = Item(value="37", label= u"LOCACAO DE MAO-DE-OBRA"),
    MATERIAL_DE_CONSUMO = Item(value="30", label= u"MATERIAL DE CONSUMO"),

    MATERIAL_DE_DISTRIBUICAO_GRATUITA = Item(value="32", label= u"Material de Distribuição Gratuita"),

    OBRAS_E_INSTALACOES = Item(value="51", label= u"OBRAS E INSTALACOES"),

    OBRIGACOES_DECORRENTES_DE_POLITICA_MONETARIA = Item(value="26", label= u"Obrigações decorrentes de Política Monetária"),

    OBRIGACOES_PATRONAIS = Item(value="13", label= u"OBRIGACOES PATRONAIS - OP.INTRA-ORCAMENTARIAS"),
    OBRIGACOES_TRIBUTARIAS_E_CONTRIBUTIVAS = Item(value="47", label= u"OBRIG.TRIBUT.E CONTRIB-OP.INTRA-ORCAMENTARIAS"),

    OUTRAS_DESPESAS_DE_PESSOAL_DECORRENTES_DE_CONTRATOS_DE_TERCEIRIZACAO = Item(value="34", label= u"Outras Despesas de Pessoal decorrentes de Contratos de Terceirização"),

    OUTRAS_DESPESAS_VARIAVEIS_PESSOAL_CIVIL = Item(value="16", label= u"OUTRAS DESPESAS VARIAVEIS - PESSOAL CIVIL"),
    OUTRAS_DESPESAS_VARIAVEIS_PESSOAL_MILITAR = Item(value="17", label= u"Outras Despesas Variáveis - Pessoal Militar"),
    OUTROS_AUXILIOS_FINANCEIROS_A_PESSOAS_FISICAS = Item(value="48", label= u"Outros Auxílios Financeiros a Pessoas Físicas"),
    OUTROS_BENEFICIOS_ASSISTENCIAIS = Item(value="08", label= u"OUTROS BENEF.ASSIST. DO SERVIDOR E DO MILITAR"),
    OUTROS_BENEFICIOS_DE_NATUREZA_SOCIAL = Item(value="10", label= u"Outros Benefícios de Natureza Social"),
    OUTROS_BENEFICIOS_PREVIDENCIARIOS = Item(value="05", label= u"Outros Benefícios Previdenciários"),
    OUTROS_ENCARGOS_SOBRE_A_DIVIDA_MOBILIARIA = Item(value="24", label= u"Outros Encargos sobre a Dívida Mobiliária"),
    OUTROS_ENCARGOS_SOBRE_A_DIVIDA_POR_CONTRATO = Item(value="22", label= u"Outros Encargos sobre a Dívida por Contrato"),

    OUTROS_SERVICOS_DE_TERCEIROS_PESSOA_FISICA = Item(value="36", label= u"OUTROS SERVICOS DE TERCEIROS - PESSOA FISICA"),
    OUTROS_SERVICOS_DE_TERCEIROS_PESSOA_JURIDICA = Item(value="39", label= u"OUTROS SERVICOS DE TERCEIROS-PESSOA JURIDICA"),
    PASSAGENS_E_DESPESAS_COM_LOCOMOCAO = Item(value="33", label= u"PASSAGENS E DESPESAS COM LOCOMOCAO"),
    PENSOES = Item(value="03", label= u"PENSOES DO RPPS E DO MILITAR"),

    PREMIACOES_CULTURAIS_ARTISTICAS_CIENTIFICAS_DESPORTIVAS_E_OUTRAS = Item(value="31", label= u"Premiações Culturais, Artísticas, Científicas, Desportivas e Outras"),
    PRINCIPAL_CORRIGIDO_DA_DIVIDA_CONTRATUAL_REFINANCIADO = Item(value="77", label= u"Principal Corrigido da Dívida Contratual Refinanciado"),
    PRINCIPAL_CORRIGIDO_DA_DIVIDA_MOBILIARIA_REFINANCIADO = Item(value="76", label= u"Principal Corrigido da Dívida Mobiliária Refinanciado"),
    PRINCIPAL_DA_DIVIDA_CONTRATUAL_RESGATADO = Item(value="71", label= u"Principal da Dívida Contratual Resgatado"),
    PRINCIPAL_DA_DIVIDA_MOBILIARIA_RESGATADO = Item(value="72", label= u"Principal da Dívida Mobiliária Resgatado"),
    REMUNERACAO_DE_COTAS_DE_FUNDOS_AUTARQUICOS = Item(value="28", label= u"Remuneração de Cotas de Fundos Autárquicos"),

    RESSARCIMENTO_DE_DESPESAS_DE_PESSOAL_REQUISITADO = Item(value="96", label= u"RESSARCIMENTO DE DESP. DE PESSOAL REQUISITADO"),

    SALARIO_FAMILIA = Item(value="09", label= u"Salário-Família"),

    SENTENCAS_JUDICIAIS = Item(value="91", label= u"SENTENCAS JUDICIAIS"),
    SERVICOS_DE_CONSULTORIA = Item(value="35", label= u"SERVICOS DE CONSULTORIA"),

    SUBVENCOES_SOCIAIS = Item(value="43", label= u"Subvenções Sociais"),

    VENCIMENTOS_E_VANTAGENS_FIXAS_PESSOAL_CIVIL = Item(value="11", label= u"VENCIMENTOS E VANTAGENS FIXAS - PESSOAL CIVIL"),

    VENCIMENTOS_E_VANTAGENS_FIXAS_PESSOAL_MILITAR = Item(value="12", label= u"Vencimentos e Vantagens Fixas - Pessoal Militar"),
)


fase = Enum(
    EMPENHO = Item(value="ne", label=u"Empenho"),
    LIQUIDACAO = Item(value="nl", label=u"Liquidação"),
    PAGAMENTO = Item(value="ob", label=u"Pagamento"),
)


orgaoSuperior = Enum(
    TODOS = Item(value="11000,12000,13000,14000,15000,16000,17000", label=u"Todos"),
    STJ = Item(value="11000", label=u"SUPERIOR TRIBUNAL DE JUSTICA"),
    JF = Item(value="12000", label=u"JUSTICA FEDERAL"),
    JM = Item(value="13000", label=u"JUSTICA MILITAR"),
    JE = Item(value="14000", label=u"JUSTIÇA ELEITORAL"),
    JT = Item(value="15000", label=u"JUSTICA DO TRABALHO"),
    JDF = Item(value="16000", label=u"JUSTICA DO DISTRITO FEDERAL E DOS TERRITORIOS"),
    CNJ = Item(value="17000", label=u"CONSELHO NACIONAL DE JUSTICA"),
)


unidade = Enum(
    TODOS = Item(value="", label=u"Todos"),
    JF1GRAU = Item(value="12101", label=u"12101 - JUSTICA FEDERAL DE PRIMEIRO GRAU"),
    TRF1 = Item(value="12102", label=u"12102 - TRIBUNAL REGIONAL FEDERAL DA 1A. REGIAO"),
    TRF2 = Item(value="12103", label=u"12103 - TRIBUNAL REGIONAL FEDERAL DA 2A. REGIAO"),
    TRF3 = Item(value="12104", label=u"12104 - TRIBUNAL REGIONAL FEDERAL DA 3A. REGIAO"),
    TRF4 = Item(value="12105", label=u"12105 - TRIBUNAL REGIONAL FEDERAL DA 4A. REGIAO"),
    TRF5 = Item(value="12106", label=u"12106 - TRIBUNAL REGIONAL FEDERAL DA 5A. REGIAO"),
    JM = Item(value="13101", label=u"13101 - JUSTICA MILITAR"),
    TSE = Item(value="14101", label=u"14101 - TRIBUNAL SUPERIOR ELEITORAL"),
    TRE_AC = Item(value="14102", label=u"14102 - TRIBUNAL REGIONAL ELEITORAL DO ACRE"),
    TRE_AL = Item(value="14103", label=u"14103 - TRIBUNAL REGIONAL ELEITORAL DE ALAGOAS"),
    TRE_AM = Item(value="14104", label=u"14104 - TRIBUNAL REGIONAL ELEITORAL DO AMAZONAS"),
    TRE_BA = Item(value="14105", label=u"14105 - TRIBUNAL REGIONAL ELEITORAL DA BAHIA"),
    TRE_CE = Item(value="14106", label=u"14106 - TRIBUNAL REGIONAL ELEITORAL DO CEARA"),
    TRE_DF = Item(value="14107", label=u"14107 - TRIBUNAL REGIONAL ELEITORAL DO DIST. FEDERAL"),
    TRE_ES = Item(value="14108", label=u"14108 - TRIBUNAL REGIONAL ELEITORAL DO ESPIRITO SANTO"),
    TRE_GO = Item(value="14109", label=u"14109 - TRIBUNAL REGIONAL ELEITORAL DE GOIAS"),
    TRE_MA = Item(value="14110", label=u"14110 - TRIBUNAL REGIONAL ELEITORAL DO MARANHAO"),
    TRE_MT = Item(value="14111", label=u"14111 - TRIBUNAL REGIONAL ELEITORAL DE MATO GROSSO"),
    TRE_MS = Item(value="14112", label=u"14112 - TRIBUNAL REGIONAL ELEITORAL DE MATO G. DO SUL"),
    TRE_MG = Item(value="14113", label=u"14113 - TRIBUNAL REGIONAL ELEITORAL DE MINAS GERAIS"),
    TRE_PA = Item(value="14114", label=u"14114 - TRIBUNAL REGIONAL ELEITORAL DO PARA"),
    TRE_PB = Item(value="14115", label=u"14115 - TRIBUNAL REGIONAL ELEITORAL DA PARAIBA"),
    TRE_PR = Item(value="14116", label=u"14116 - TRIBUNAL REGIONAL ELEITORAL DO PARANA"),
    TRE_PE = Item(value="14117", label=u"14117 - TRIBUNAL REGIONAL ELEITORAL DE PERNAMBUCO"),
    TRE_PI = Item(value="14118", label=u"14118 - TRIBUNAL REGIONAL ELEITORAL DO PIAUI"),
    TRE_RJ = Item(value="14119", label=u"14119 - TRIBUNAL REGIONAL ELEITORAL DO RIO DE JANEIRO"),
    TRE_RN = Item(value="14120", label=u"14120 - TRIBUNAL REGIONAL ELEITORAL DO RIO G.DO NORTE"),
    TRE_RS = Item(value="14121", label=u"14121 - TRIBUNAL REGIONAL ELEITORAL DO RIO G. DO SUL"),
    TRE_RO = Item(value="14122", label=u"14122 - TRIBUNAL REGIONAL ELEITORAL DE RONDONIA"),
    TRE_SC = Item(value="14123", label=u"14123 - TRIBUNAL REGIONAL ELEITORAL DE SANTA CATARINA"),
    TRE_SP = Item(value="14124", label=u"14124 - TRIBUNAL REGIONAL ELEITORAL DE SAO PAULO"),
    TRE_SE = Item(value="14125", label=u"14125 - TRIBUNAL REGIONAL ELEITORAL DE SERGIPE"),
    TRE_TO = Item(value="14126", label=u"14126 - TRIBUNAL REGIONAL ELEITORAL DE TOCANTINS"),
    TRE_RR = Item(value="14127", label=u"14127 - TRIBUNAL REGIONAL ELEITORAL DE RORAIMA"),
    TRE_AP = Item(value="14128", label=u"14128 - TRIBUNAL REGIONAL ELEITORAL DO AMAPA"),
    FUNDO_PARTIDARIO = Item(value="14901", label=u"14901 - FUNDO PARTIDARIO"),
    TST = Item(value="15101", label=u"15101 - TRIBUNAL SUPERIOR DO TRABALHO"),
    TRT1 = Item(value="15102", label=u"15102 - TRIBUNAL REGIONAL DO TRABALHO DA 1A. REGIAO"),
    TRT2 = Item(value="15103", label=u"15103 - TRIBUNAL REGIONAL DO TRABALHO DA 2A. REGIAO"),
    TRT3 = Item(value="15104", label=u"15104 - TRIBUNAL REGIONAL DO TRABALHO DA 3A. REGIAO"),
    TRT4 = Item(value="15105", label=u"15105 - TRIBUNAL REGIONAL DO TRABALHO DA 4A. REGIAO"),
    TRT5 = Item(value="15106", label=u"15106 - TRIBUNAL REGIONAL DO TRABALHO DA 5A. REGIAO"),
    TRT6 = Item(value="15107", label=u"15107 - TRIBUNAL REGIONAL DO TRABALHO DA 6A. REGIAO"),
    TRT7 = Item(value="15108", label=u"15108 - TRIBUNAL REGIONAL DO TRABALHO DA 7A. REGIAO"),
    TRT8 = Item(value="15109", label=u"15109 - TRIBUNAL REGIONAL DO TRABALHO DA 8A. REGIAO"),
    TRT9 = Item(value="15110", label=u"15110 - TRIBUNAL REGIONAL DO TRABALHO DA 9A. REGIAO"),
    TRT10 = Item(value="15111", label=u"15111 - TRIBUNAL REGIONAL DO TRABALHO DA 10A. REGIAO"),
    TRT11 = Item(value="15112", label=u"15112 - TRIBUNAL REGIONAL DO TRABALHO DA 11A. REGIAO"),
    TRT12 = Item(value="15113", label=u"15113 - TRIBUNAL REGIONAL DO TRABALHO DA 12A. REGIAO"),
    TRT13 = Item(value="15114", label=u"15114 - TRIBUNAL REGIONAL DO TRABALHO DA 13A. REGIAO"),
    TRT14 = Item(value="15115", label=u"15115 - TRIBUNAL REGIONAL DO TRABALHO DA 14A. REGIAO"),
    TRT15 = Item(value="15116", label=u"15116 - TRIBUNAL REGIONAL DO TRABALHO DA 15A. REGIAO"),
    TRT16 = Item(value="15117", label=u"15117 - TRIBUNAL REGIONAL DO TRABALHO DA 16A. REGIAO"),
    TRT17 = Item(value="15118", label=u"15118 - TRIBUNAL REGIONAL DO TRABALHO DA 17A. REGIAO"),
    TRT18 = Item(value="15119", label=u"15119 - TRIBUNAL REGIONAL DO TRABALHO DA 18A. REGIAO"),
    TRT19 = Item(value="15120", label=u"15120 - TRIBUNAL REGIONAL DO TRABALHO DA 19A. REGIAO"),
    TRT20 = Item(value="15121", label=u"15121 - TRIBUNAL REGIONAL DO TRABALHO DA 20A. REGIAO"),
    TRT21 = Item(value="15122", label=u"15122 - TRIBUNAL REGIONAL DO TRABALHO DA 21A. REGIAO"),
    TRT22 = Item(value="15123", label=u"15123 - TRIBUNAL REGIONAL DO TRABALHO DA 22A. REGIAO"),
    TRT23 = Item(value="15124", label=u"15124 - TRIBUNAL REGIONAL DO TRABALHO DA 23A. REGIAO"),
    TRT24 = Item(value="15125", label=u"15125 - TRIBUNAL REGIONAL DO TRABALHO DA 24A. REGIAO"),
    TJDF = Item(value="16101", label=u"16101 - TRIBUNAL DE JUSTICA DO DISTRITO FEDERAL"),
    INFANCIA_JUVENTUDE = Item(value="16103", label=u"16103 - JUSTICA DA INFANCIA E DA JUVENTUDE"),
    CNJ = Item(value="17101", label=u"17101 - CONSELHO NACIONAL DE JUSTICA"),
)

gestora = Enum(
    TODOS = Item(value="", label=u"Todos"),
    #FIXME:
)

