from datetime import datetime

import click
import prejus


def validate_options(ctx, param, value):
    if not value:
        return param.default
    try:
        classname = param.name.title()
        cls = getattr(prejus, classname)
        return cls[value]
    except KeyError as error:
        raise click.BadParameter('"{}" não é uma opção válida.'.format(value))

def validate_dates(ctx, param, value):
    if not value:
        return param.default
    try:
        return datetime.strptime(value, '%d-%m-%Y').date()
    except (TypeError, ValueError) as error:
        raise click.BadParameter(
            '"{}" não é um valor válido. Use "dd-mm-aaaa".'.format(value))

def validate_orgao(ctx, param, value):
    try:
        orgao = ('orgaoSuperior', prejus.OrgaoSuperior[value])
    except KeyError:
        try:
            orgao = ('unidade', prejus.Unidade[value])
        except KeyError:
            raise click.BadParameter(
                '"{}" não é um valor válido para {}.'.format(value, param))
    return orgao


@click.command()
@click.option('--inicio', callback=validate_dates,
              help='Data de início da consulta.')
@click.option('--fim', callback=validate_dates,
              help='Data de fim da consulta.')
@click.option('--elemento', callback=validate_options,
              help='Elemento de despesa.')
@click.option('--fase', callback=validate_options, default='EMPENHO',
              help='Fase da despesa.')
@click.argument('orgao', callback=validate_orgao)
def cli(**kwargs):
    '''
    Consulta despesas do Judiciário Brasileiro, no Portal da Transparência.
    '''
    orgao = kwargs.pop('orgao')
    kwargs[orgao[0]] = orgao[1]
    kwargs = {key: value for key, value in kwargs.items() if value}
    results = prejus.consulta(**kwargs)

