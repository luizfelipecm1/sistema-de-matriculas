# Como rodar

## Requisitos
- Python ^3.12
- Poetry *

## Instalando o Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

[Documentacao Oficial](https://python-poetry.org/docs/#installing-with-the-official-installer)

## Instalando as depências

Com o poetry instalado, podemos instalar as dependências como abaixo:

```bash
cd Codigo/backend
poetry install
```

Após instalado, você deve estar pronto para começar.

## Poetry shell

Caso queira rodar o projeto de um terminal, abra um shell do poetry para ter acesso às dependências:

```bash
cd Codigo/backend
poetry shell
```

O seu terminal deverá ficar com a aparência assim:

```bash
(backend-py3.12) [TBD]$
```

## Rodando a main

Caso queira rodar a main de um terminal, garanta que tem acesso às dependências, com o passo anterior.

Após isso, rode:

```bash
cd Codigo/backend/backend
python -m main
```