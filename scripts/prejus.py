import click


@click.command()
@click.option('--inicio', default='', help='Data de início da consulta.')
@click.option('--fim', default='', help='Data de fim da consulta.')
@click.option('--elemento', help='Elemento de despesa.')
@click.option('--fase', default='EMPENHO', help='Fase da despesa.')
@click.argument('orgao')
def cli(inicio, fim, elemento, fase, orgao):
    '''
    Consulta despesas do Judiciário Brasileiro, no Portal da Transparência.
    '''
    click.echo('Hello prejus!')
