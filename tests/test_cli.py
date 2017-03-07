from click.testing import CliRunner
from datetime import date
from scripts.prejus import cli

import click
import mock
import prejus


runner = CliRunner()


def testa_sem_indicar_o_orgao():
    result = runner.invoke(cli)
    assert result.exit_code == 2


def testa_indicando_um_orgao():
    result = runner.invoke(cli, ['TRT13'])
    assert result.exit_code == 0

#FIXME:
def testa_validacoes_das_opcoes():
    args = [
        '--inicio', '01-01-2017',
        '--fim', '31-01-2017',
        '--elemento', 'AUXILIO_TRANSPORTE',
        '--fase', 'PAGAMENTO',
        'TRT13'
    ]
    expected = [
        date(2017, 1, 1),
        date(2017, 1, 31),
        prejus.Elemento.AUXILIO_TRANSPORTE,
        prejus.Fase.PAGAMENTO,
        prejus.Unidade.TRT13,
        ''
    ]
    result = runner.invoke(cli, args)
    assert result.output == '\n'.join(map(str, expected))

