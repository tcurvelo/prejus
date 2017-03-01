prejus
************************************************************************
Cliente para para consumir dados do `Portal Transparência`_ do Judiciário
Brasileiro.


Utilizando
==========

Para instalar::

  pip install prejus

Usando o cliente de linha de comando::

  $ prejus --elemento DIARIAS_CIVIL --inicio 01-01-2016 --fim 31-12-2016 TRT13 > diarias_2016.csv

Usando dentro de outra app::

    import prejus
    from datetime import date
    resultados = prejus.consulta(
        inicio = date(2016, 1, 1),
        fim = date(2016, 1, 31),
        unidade = prejus.Unidade.TRT13,
        elemento = prejus.Elemento.DIARIAS_CIVIL,
    )
    despesas.salva_csv(resultados, "diarias.csv")


Desenvolvendo
=============

Instalando::

    pip install --editable .

Rodando os testes::

    pip install pytest
    pytest


.. _`Portal Transparência`: http://www.portaltransparencia.jus.br/despesas/

