# Sistema de Cadastro e Chaveamento de Artes Marciais

Projeto em Python com programas de terminal para cadastro de alunos e atletas de artes marciais. Um dos scripts também organiza atletas de Jiu-Jitsu e Luta Livre Esportiva em categorias e gera confrontos para campeonatos.

## Arquivos do projeto

### `cadastramentodealunos.py`

Fluxo de matrícula de alunos em uma academia. Solicita dados pessoais e, para menores de idade, dados de responsáveis. Permite escolher a modalidade e a graduação, oferece equipamentos para alunos iniciantes e apresenta opções de pagamento por PIX ou cartão.

### `cadastramentodeatletas.py`

Cadastro de atletas para o chaveamento de campeonatos. Solicita nome, sexo, data de nascimento, modalidade, faixa, peso, academia, professor e telefone. Valida a data de nascimento, calcula a idade e acrescenta o cadastro ao arquivo `alunos.csv`.

### `gestordechaveamento.py`

Lê os registros de `alunos.csv`, calcula as categorias de idade e peso conforme a modalidade e agrupa os atletas por faixa, idade, peso e sexo. Em seguida, exibe os participantes de cada categoria e gera confrontos aleatórios em formato eliminatório, incluindo BYEs quando necessário e vitória por W.O. para categorias com um único atleta.

### `alunos.csv`

Arquivo de entrada e saída do fluxo de campeonato: o cadastro de atletas acrescenta linhas a esse arquivo, e o gestor usa os dados para formar as categorias. A primeira linha contém os nomes das colunas esperadas. O arquivo incluído no repositório tem dados sintéticos de demonstração; substitua-os por cadastros válidos e autorizados antes de usar o gestor em um campeonato.

## Requisitos

- Python 3
- Bibliotecas `emoji` e `pandas`

Instale as bibliotecas necessárias:

```bash
python -m pip install emoji pandas
```

## Como executar

Execute os comandos a partir da pasta do projeto. O fluxo de matrícula é independente:

```bash
python cadastramentodealunos.py
```

Para cadastrar atletas e depois gerar as categorias e os confrontos:

```bash
python cadastramentodeatletas.py
python gestordechaveamento.py
```

O gestor espera encontrar `alunos.csv` na pasta de onde for executado. O cadastro de atletas também grava nesse arquivo, criando o cabeçalho quando ele ainda não existe ou está vazio.
