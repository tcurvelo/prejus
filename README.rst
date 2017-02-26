br.jus.portaltransparencia
************************************************************************
Cliente para para consumir dados do `Portal Transparência`_ do
Judiciário Brasileiro.


Utilizando
==========
Para instalar::

    python setup.py install

Exemplo::

    from br.jus.portaltransparencia import despesas, enums
    from datetime import date
    resultados = despesas.consulta(
        inicio = date(2013,8,1),
        fim = date(2013,8,30),
        orgaoSuperior = enums.orgaoSuperior.JT.value,
        unidade = enums.unidade.TRT13.value,
        elemento = enums.elemento.DIARIAS_CIVIL.value,
    )
    despesas.salva_csv(resultados, "diarias.csv")


Desenvolvendo
=============
Instalando::

    python setup.py develop

Rodando os testes::

    pip install pytest
    pytest


.. _`Portal Transparência`: http://www.portaltransparencia.jus.br/despesas/

