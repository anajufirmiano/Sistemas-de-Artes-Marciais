# --------------------------------------- #
#        CADASTRAMENTO DE ATLETAS         #
# --------------------------------------- #

import csv
import os
import emoji
from datetime import datetime
from time import sleep

print ('--------------------------------------------------------------------------------------')
print ('                            CADASTRAMENTO DE ATLETAS                                  ')
print ('                         Para Chaveamento de Campeonato                               ')
print ('--------------------------------------------------------------------------------------')

nome = str(input('Nome Completo do aluno: '))

sexo = input('Sexo: ').upper()

# Validação da data de nascimento e cálculo de idade
while True:
    nascimento = input('Data de nascimento (com barras): ')
    try:
        # Tenta converter a string para data
        nascimento_formatado = datetime.strptime(nascimento, '%d/%m/%Y') # ------------------------------------------------------------------ Recebe e converte a data de nascimento
        hoje = datetime.today() # ----------------------------------------------------------------------------------------------------------- Pega a data de hoje automaticamente

        # Validação extra: garante que a data não seja no futuro
        if nascimento_formatado > hoje:
            print ('A data de nascimento não pode ser no futuro.')
            sleep(1)
            print ('Tente novamente.')
            continue

        idade = (hoje.year - nascimento_formatado.year - ((hoje.month, hoje.day) < (nascimento_formatado.month, nascimento_formatado.day))) # Calcula a idade exata
        # Se chegou até aqui sem erros, sai do loop
        break
    except ValueError:
    # Executado caso o formato esteja errado ou a data seja inválida (ex: 31/02/2020)
        print ('Digite uma data de nascimento válida.')
        sleep(1)
        print ('Tente novamente.')

modalidade = int(input('Modalidade desejada: \n1. Jiu-Jitsu \n2. Luta Livre Esportiva \nOpção: '))

# Listas de faixas
faixa_jj = ['Branca', 'Cinza/Branca', 'Cinza', 'Cinza/Preta', 'Amarela/Branca', 'Amarela', 'Amarela/Preta', 'Laranja/Branca', 'Laranja', 'Laranja/Preta', 'Verde/Branca', 'Verde', 'Verde/Preta', 'Azul', 'Roxa', 'Marrom', 'Preta', 'Coral']
faixa_lle = ['Branca', 'Cinza', 'Amarela', 'Laranja', 'Verde', 'Azul', 'Roxa', 'Marrom', 'Preta', 'Coral']

# Filtro de faixas por idade e modalidade
if modalidade == 1 and idade <=15:
    faixas = faixa_jj[:13]
elif modalidade == 1 and idade >=16:
    faixas = [faixa_jj[0]] + faixa_jj[13:]
elif modalidade == 2 and idade <= 15:
    faixas = faixa_lle[:5]
elif modalidade == 2 and idade >=16:
    faixas = [faixa_lle[0]] + faixa_lle[2:4] + faixa_lle[5:]

# Validação da faixa
while True:
    faixa = input ('Faixa: ').strip() .title()
    if faixa in faixas:
        faixa_s = faixa
        break
    else:
        print ('A faixa {} é inválida ou não é permitida para esta modalidade/idade.' .format(faixa.upper()))
        sleep(1)
        print ('Tente novamente.')


peso = float(input('Peso: '))

academia = str(input('Academia: '))

professor = str(input('Nome do professor: '))

# Validação do telefone
while True:
    numero = str(input('Número de telefone: '))
    if len(numero) == 11:
        break
    else:
        print ('Número de telefone incorreto.')
        sleep(1)
        print ('Tente novamente.')


print (emoji.emojize('Cadastro Finalizado com sucesso! :smiling_face:'))

# Define o caminho do arquivo no mesmo diretório do script
diretorio_script = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio_script, 'alunos.csv')

# Verifica se o arquivo precisa de cabeçalho
cadastro_vazio = not os.path.exists(caminho_csv) or os.path.getsize(caminho_csv) == 0

with open(caminho_csv, 'a', newline='', encoding='utf-8') as cadastro:
    escritor = csv.writer(cadastro)
    
    if cadastro_vazio:
        escritor.writerow([
            'Nome Completo', 'Sexo', 'Modalidade', 'Data de Nascimento', 
            'Idade', 'Faixa', 'Peso', 'CT', 'Professor', 'Número de telefone'
        ])
        
    # Adiciona o novo aluno
    escritor.writerow([nome, sexo, modalidade, nascimento, idade, faixa, peso, academia, professor, numero])