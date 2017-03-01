import click

from click.testing import CliRunner
from scripts.prejus import cli


runner = CliRunner()


def testa_sem_indicar_o_orgao():
    result = runner.invoke(cli)
    assert result.exit_code == 2


def testa_indicando_um_orgao():
    result = runner.invoke(cli, ['TRT13'])
    assert result.exit_code == 0
