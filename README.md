# Previsão Eleitoral

## Visão geral

Este É o projeto Kedro de Previsão eleitoral, que foi gerado usando `Kedro 0.18.4` para o Programa Lighthouse.

Dê uma olhada na [documentação do Kedro](https://kedro.readthedocs.io) para começar.

## Regras e diretrizes

Para obter o melhor do modelo:

* Não remova nenhuma linha do arquivo `.gitignore` que fornecemos
* Certifique-se de que seus resultados possam ser reproduzidos seguindo uma [convenção de engenharia de dados](https://kedro.readthedocs.io/en/stable/faq/faq.html#what-is-data-engineering-convention)
* Não envie dados para o seu repositório
* Não confirme nenhuma credencial ou sua configuração local em seu repositório. Mantenha todas as suas credenciais e configurações locais em `conf/local/`

## Como instalar dependências

Declare quaisquer dependências em `src/requirements.txt` para instalação `pip` e `src/environment.yml` para instalação `conda`.

Para instalá-los, execute:

```
pip install -r src/requirements.txt
```

## Como executar seu pipeline Kedro

Você pode executar seu projeto Kedro com:

```
kedro run
```

## Como testar seu projeto Kedro

Dê uma olhada no arquivo `src/tests/test_run.py` para obter instruções sobre como escrever seus testes. Você pode executar seus testes da seguinte maneira:

```
kedro test
```

Para configurar o limite de cobertura, acesse o arquivo `.coveragerc`.

## Dependências do projeto

Para gerar ou atualizar os requisitos de dependência para seu projeto:

```
kedro build-reqs
```

Isso irá `pip-compile` o conteúdo de `src/requirements.txt` em um novo arquivo `src/requirements.lock`. Você pode ver a saída da resolução abrindo `src/requirements.lock`.

Depois disso, se você quiser atualizar os requisitos do seu projeto, atualize `src/requirements.txt` e execute novamente `kedro build-reqs`.

[Mais informações sobre dependências do projeto](https://kedro.readthedocs.io/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## Como trabalhar com Kedro e notebooks

> Nota: Usar `kedro jupyter` ou `kedro ipython` para executar seu notebook fornece estas variáveis no escopo: `context`, `catalog` e `startup_error`.
>
> Jupyter, JupyterLab e IPython já estão incluídos nos requisitos do projeto por padrão, portanto, depois de executar `pip install -r src/requirements.txt`, você não precisará executar nenhuma etapa extra antes de usá-los.

### Jupyter
Para usar os notebooks Jupyter em seu projeto Kedro, você precisa instalar o Jupyter:

```
pip install jupyter
```

Depois de instalar o Jupyter, você pode iniciar um servidor de notebook local:

```
kedro jupyter notebook
```

### JupyterLab
Para usar o JupyterLab, você precisa instalá-lo:

```
pip install jupyterlab
```

Você também pode iniciar o JupyterLab:

```
kedro jupyter lab
```

### IPython
E se você quiser executar uma sessão IPython:

```
kedro ipython
```

### Como converter células de notebook em nós em um projeto Kedro
Você pode mover o código do notebook para uma estrutura de projeto Kedro usando uma mistura de [marcação de célula](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) e Kedro Comandos da CLI.

Ao adicionar a tag `node` a uma célula e executar o comando abaixo, o código-fonte da célula será copiado para um arquivo Python dentro de `src/<package_name>/nodes/`:

```
kedro jupyter convert <filepath_to_my_notebook>
```
> *Observação:* O nome do arquivo Python corresponde ao nome do notebook original.

Alternativamente, você pode querer transformar todos os seus cadernos de uma só vez. Execute o seguinte comando para converter todos os arquivos do notebook encontrados no diretório raiz do projeto e em qualquer uma de suas subpastas:

```
kedro jupyter convert --all
```

### Como ignorar as células de saída do notebook no `git`
Para remover automaticamente todo o conteúdo da célula de saída antes de se comprometer com o `git`, você pode executar `kedro activate-nbstripout`. Isso adicionará um gancho em `.git/config` que executará `nbstripout` antes que qualquer coisa seja confirmada no `git`.

> *Observação:* Suas células de saída serão mantidas localmente.

## Empacote seu projeto Kedro

[Mais informações sobre como criar a documentação do projeto e empacotar seu projeto](https://kedro.readthedocs.io/en/stable/tutorial/package_a_project.html)
