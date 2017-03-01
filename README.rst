prejus
************************************************************************
Cliente para para consumir dados do `Portal Transparência`_ do
Judiciário Brasileiro.


Utilizando
==========
Para instalar::

    pip install .

Exemplo::

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

