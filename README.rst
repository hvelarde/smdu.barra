**********************
SMDU Identidade visual
**********************

.. contents:: Conteúdos
   :depth: 2

Introdução
-----------

.. image:: https://img.shields.io/travis/hvelarde/smdu.identidadevisual/master.svg
    :target: http://travis-ci.org/hvelarde/smdu.identidadevisual

.. image:: https://img.shields.io/coveralls/hvelarde/smdu.identidadevisual/master.svg
    :target: https://coveralls.io/r/hvelarde/smdu.identidadevisual

Barra de identidade visual e footer para uso em sites Plone da Prefeitura de São Paulo.

Instalação
----------

Para habilitar a instalação deste produto em um ambiente que utilize o buildout:

1. Editar o arquivo buildout.cfg (ou outro arquivo de configuração) e adicionar o pacote ``smdu.identidadevisual`` à lista de eggs da instalação:

.. code-block:: ini

    [buildout]
    ...
    eggs =
        smdu.identidadevisual

2. Após alterar o arquivo de configuração é necessário executar ``bin/buildout``, que atualizará sua instalação.

3. Reinicie o Plone

4. Acesse o painel de controle e instale o produto 'SMDU Identidade visual'.

Captura de telas
----------------

.. figure:: https://raw.github.com/hvelarde/smdu.identidadevisual/master/docs/identity-bar.png
    :align: center
    :height: 225px
    :width: 768px

    A barra de identidade visual.

.. figure:: https://raw.github.com/hvelarde/smdu.identidadevisual/master/docs/footer.png
    :align: center
    :height: 405px
    :width: 768px

    O footer.
