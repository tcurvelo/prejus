br.jus.portaltransparencia
************************************************************************

Cliente para para consumir dados do `Portal Transparência`_ do
Judiciário Brasileiro

Exemplo de uso
--------------
::

    from br.jus.portaltransparencia import despesas, enums
    from datetime import date
    resultados = despesas.consulta(
        inicio = date(2013,8,1),
        fim = date(2013,8,30),
        orgaoSuperior = enums.orgaoSuperior.JT.value,
        unidade = enums.unidade.TRT13.value,
        elemento = enums.elemento.DIARIAS_CIVIL.value,
    )
    print resultados

TODO
----
* ``unidadeGestora`` ainda fixa em 'TODOS'
* criar função para gerar csv (`exemplo
  <https://gist.github.com/tcurvelo/6128607>`_)

.. _`Portal Transparência`: http://www.portaltransparencia.jus.br/despesas/