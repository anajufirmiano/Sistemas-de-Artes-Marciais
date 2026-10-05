from datetime import datetime
from time import sleep
from emoji import emojize

print('-=' * 50)
print('                                       CADASTRAMENTO DE ALUNOS                                     ')
print('-=' * 50)

# ------------------------------ #
# 1. RECEBER OS DADOS DOS ALUNOS #
# ------------------------------ #
sleep(2)
nome = str(input('Nome completo do aluno: '))
sexo = input('Sexo: \n1. Feminino \n2. Masculino \nOpção: ')

# DATA DE NASCIMENTO + FORMATAÇÃO
nascimento = input('Data de nascimento (com barras): ')
nascimento_formatado = datetime.strptime(nascimento, '%d/%m/%Y') # ------------------------------------------------------------------ Recebe e converte a data de nascimento
hoje = datetime.today() # ----------------------------------------------------------------------------------------------------------- Pega a data de hoje automaticamente
idade = (hoje.year - nascimento_formatado.year - ((hoje.month, hoje.day) < (nascimento_formatado.month, nascimento_formatado.day))) # Calcula a idade exata

# 1.1 Condição de idade
while True:
    if idade < 18:
        responsavel = str(input('Nome completo do responsável: '))
        responsavel_num = str(input('Número de telefone do responsável: '))
        parentesco = int(input('Tipo de Parentesco: \n1. Pais \n2. Avós \n3. Irmãos \n4. Outro \nOpção: '))
        if parentesco == 4:
            outro_parentesco = str(input("O que essa pessoa é do aluno? "))

# 1.2 Adicionar outro responsável
        outro_responsavel = str(input('Deseja adicionar um segundo responsável? '))
        if outro_responsavel.lower() == 'sim':
            responsavel2 = str(input('Nome completo do segundo responsável: '))
            responsavel_num2 = str(input('Número de telefone do segundo responsável: '))
            parentesco2 = input('Tipo de Parentesco: \n1. Pais \n2. Avós \n3. Irmãos \n4. Outro \nOpção: ')
            if parentesco2 == '4':
                outro_parentesco2 = str(input('O que essa pessoa é do aluno? '))
            break
        else:
            break
    else:
        # Se for maior de idade, cadastra o número do aluno
        while True:
            numero = str(input('Número de telefone: '))
            if len(numero) == 11 and numero.isdigit():
                break
            else:
                print('Erro \nTente novamente.')
        break

while True:
    cep = str(input ('CEP: '))
    if len(cep) == 8 and cep.isdigit():
        break
    else:
        print ('Erro \nTente novamente.')

# ------------------------ #
# 2. MODALIDADE PRETENDIDA #
# ------------------------ #

# 2.1 Modalidades e seus valores
while True:
    print ('-' * 32)
    print ('     VALORES DAS MODALIDADES')
    print ('')
    print (' 1. Jiu-Jitsu: R$ 120,00 \n 2. Luta Livre Esportiva: R$100,00 \n 3. Muay-thai: R$150,00')
    print ('-' * 32)

# VARIÁVEIS COM OS VALORES DAS MODALIDADES
    jj = 120.0
    lle = 100.0
    mt = 150.0

    modalidade = int(input('Digite o número de acordo com a modalidade escolhida: '))

# 2.2 Condição de Faixa para Cada Idade e Modalidade
    if modalidade == 1 and idade <= 15:
        print ('---------------------------------------')
        print ('                 FAIXA:                ')
        print (' 1. Branca          2. Cinza/Branca')
        print (' 3. Cinza           4. Cinza/Preta')
        print (' 5. Amarela/Branca  6. Amarela')
        print (' 7. Amarela/Preta   8. Laranja/Branca')
        print (' 9. Laranja         10.Laranja/Preta')
        print (' 11. Verde/Branca   12. Verde')
        print (' 13. Verde/Preta')
        print ('---------------------------------------')
        faixa_jj = int(input ('Digite o número de acordo com a faixa atual do aluno: '))
    elif modalidade == 1 and idade >= 16:
        print ('------------------------')
        print ('         FAIXA:         ')
        print (' 1. Branca   2. Azul')
        print (' 3. Roxa     4. Marrom')
        print (' 5. Preta    6. Coral')
        print ('------------------------')
        faixa_jj = int(input ('Digite o número de acordo com a faixa atual do aluno: '))
    elif modalidade == 2 and idade <= 15:
        print ('------------------------')
        print ('         FAIXA:         ')
        print (' 1. Branca   2. Cinza')
        print (' 3. Amarela  4. Laranja')
        print (' 5. Verde')
        print ('------------------------')
        faixa_lle = int(input ('Digite o número de acordo com a faixa atual do aluno: '))
    elif modalidade == 2 and idade >= 16:
        print ('------------------------')
        print ('         FAIXA:         ')
        print (' 1. Branca   2. Amarela')
        print (' 3. Laranja  4. Azul')
        print (' 5. Roxa     6. Marrom')
        print (' 7. Preta    8. Coral')
        print ('------------------------')
        faixa_lle = int(input ('Digite o número de acordo com a faixa atual do aluno: '))
    elif modalidade == 3 and idade <= 15:
        print ('------------------------------------------')
        print ('                  TARJA:                  ')
        print (' 1. Branca      2. Branca/Vermelha')
        print (' 3. Vermelha    4. Vermelha/Azul Clara')
        print (' 5. Azul Clara  6. Azul Clara/Azul Escura')
        print ('------------------------------------------')
        tarja = int(input ('Digite o número de acordo com a tarja atual do aluno: '))
    else:
        print ('------------------------------------------')
        print ('                  TARJA:                  ')
        print (' 1. Branca       2. Branca/Vermelha')
        print (' 3. Vermelha     4. Vermelha/Azul Clara')
        print (' 5. Azul Clara   6. Azul Clara/Azul Escura')
        print (' 7. Azul Escura  8. Azul Escura/Preta')
        print (' 9. Preta        9. Preta/Branca')
        print (' 10. Preta/Branca/Vermelha')
        print ('------------------------------------------')
        tarja = int(input ('Digite o número de acordo com a tarja atual do aluno: '))

    print ('Cadastro finalizado com sucesso!')
    sleep(2)

# --------------------------------------------------- #
# 3 COMPRAS POR MODALIDADE - (caso seja faixa branca) #
# --------------------------------------------------- #

# VARIÁVEIS COM OS VALORES DOS TRAJES
    kimono = 420.0
    faixa = 50.0
    resguarde = 90.0
    short = 90.0
    tarja_v = 70.0

# 3.1 JIU-JITSU
    if modalidade == 1 and faixa_jj == 1:
        print ('------------------------------')
        print ('      VALORES DOS TRAJES      ')
        print ('')
        print (' Kimono: R$ 420,00 \n Faixa: R$50,00 \n Resguarde: R$90,00')
        print ('------------------------------')

        comprar = int(input ('Comprar: \n1. Kimono \n2. Faixa \n3. Resguarde \n4. Nenhum \nOpção: '))

        if comprar == 1:
            kimono_tam = int(input ('Tamanho: \n1. A1 \n2. A2 \n3. A3 \n4. A4 \nOpção: '))
            cor = int(input ("Cor: \n1. Branco \n2. Preto \n3. Azul \nOpção: "))
            produtos_j = [jj, kimono] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_j = sum(produtos_j) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # AQUI VAI MOSTRAR O TOTAL
            print("Total: {}".format(total_j))  
        elif comprar == 2:
            faixa_tam = int(input ('Tamanho: \n1. A1 \n2. A2 \n3. A3 \n4. A4 \nOpção: '))
            produtos_jf = [jj, faixa] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_jf = sum(produtos_jf) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # AQUI VAI MOSTRAR O TOTAL
            print("Total: {}".format(total_jf))
        elif comprar == 3:
            resg_tam = int(input ("Tamanho: \n1. PP \n2. P \n3. M \n4. G \n5. GG \nOpção: "))
            produtos_jfr = [jj, resguarde] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_jfr = sum(produtos_jfr) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # AQUI VAI MOSTRAR O TOTAL
            print("Total: {}".format(total_jfr))
        else:
            break

# 3.2 LUTA LIVRE ESPORTIVA
    if modalidade == 2 and faixa_lle == 1:
        print ('------------------------------')
        print ('      VALORES DOS TRAJES      ')
        print ('')
        print (' Faixa: R$ 50,00 \n Resguarde: R$90,00 \n Short: R$90,00 ')
        print ('------------------------------')

        comprar = int(input('Comprar: \n1. Faixa \n2. Resguarde \n3. Short \n4. Nenhum \nOpção: '))

        if comprar == 1:
            faixa_tam = int(input ('Tamanho: \n1. A1 \n2. A2 \n3. A3 \n4. A4 \nOpção: '))
            produtos_l = [lle, faixa] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_l = sum(produtos_l) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_l)) 
        elif comprar == 2:
            resg_tam = int(input ('Tamanho: \n1. PP \n2. P \n3. M \n4. G \n5. GG \nOpção: '))
            produtos_lr = [lle, resguarde] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_lr = sum(produtos_lr) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_lr))
        elif comprar == 3:
            short_tam = int(input ('Tamanho: \n1. PP \n2. P \n3. M \n4. G \n5. GG \nOpção: '))
            produtos_lrs = [lle, short] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_lrs = sum(produtos_lrs) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_lrs))
        else:
            break

# 3.3 MUAY-THAI
    if modalidade == 3 and tarja == 1:
        print ('------------------------------')
        print ('      VALORES DOS TRAJES      ')
        print ('')
        print (' Tarja: R$ 70,00 \n Resguarde: R$90,00 \n Short: R$90,00 ')
        print ('------------------------------')

        comprar = int(input ('Comprar: \n1. Tarja \n2. Resguarde \n3. Short \n4. Nenhum \nOpção: '))

        if comprar == 1:
            produtos_m = [mt, tarja_v] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_m = sum(produtos_m) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_m))
        elif comprar == 2:
            short_tam = int(input ('Tamanho: '))
            produtos_mr = [mt, resguarde] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_mr = sum(produtos_mr) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_mr))
        elif comprar == 3:
            resg_tam = int(input ('Tamanho: '))
            produtos_mrs = [mt, short] # --------------------------------------------------- AQUI VAI SELECIONAR OS PRODUTOS
            total_mrs = sum(produtos_mrs) # --------------------------------------------------- AQUI VAI SOMAR OS PRODUTOS SELECIONADOS
            # TOTAL DOS PRODUTOS
            print ('Total: {}'.format(total_mrs))
        else:
            break
    break

# ----------------------- #
# 4. FORMAS DE PAGAMENTO  #
# ----------------------- #
sleep(2)#
pagamento = int(input ('Forma de pagamento: \n1. PIX \n2. Cartão \nOpção: '))

if pagamento == 1:
    print ('PROCESSANDO...')
    sleep(3)

elif pagamento == 2:
# LOOP PARA VALIDAÇÃO DOS DADOS DO CARTÃO
    while True:
        dados_cartao = str(input('Número do cartão (16 dígitos): '))
        if len(dados_cartao) == 16 and dados_cartao.isdigit():
            break
        else:
            print ('Erro! Cartão inválido.')
            sleep(1)
            print ('Tente novamente.')

    nome_cartao = str(input ('Nome no cartão: '))

    while True:
        cvv_cartao = input('CVV: ')
        if len(cvv_cartao) == 3 and cvv_cartao.isdigit():
            break
        else:
            print ('Erro! CVV inválido.')
            sleep(1)
            print ('Tente novamente.')

    vencimento_cartao = input('Vencimento (MM/AA): ')
    vencimento_cartao_formatado = datetime.strptime (vencimento_cartao, '%m/%y')# --------------------- Recebe e converte a data de vencimento

    cartao = str(input('Débito ou Crédito? '))
    if cartao.lower() == 'débito' or cartao.lower() == 'debito':
        print ('PROCESSANDO...')
        sleep(3)
    elif cartao.lower() == 'crédito' or cartao.lower() == 'credito':
        parcelamento = input('Deseja parcelar? ')
        if parcelamento.lower() == 'sim':
            parcelamento_vezes = str(input ('Em quantas vezes? \n1x \n2x \n3x \nOpção: '))
            if parcelamento_vezes == '1x':
                print ('')
            elif parcelamento_vezes == '2x':
                print ('')
            elif parcelamento_vezes == '3x':
                print('')
            else:
                print ('Erro! Tente novamente')

print ('Pagamento finalizado com sucesso!')
sleep(1)
print (emojize ('Obrigada pela preferência :smiling_face:'))
