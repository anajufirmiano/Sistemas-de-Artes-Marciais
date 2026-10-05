import pandas as pd
import math

# --------------------------------------- #
#         GESTOR DE CHAVEAMENTO           #
# --------------------------------------- #

df = pd.read_csv('cadastramento artes marciais/alunos.csv')

# CATEGORIAS DE IDADE
def categoria_idade(linha):
    idade = int(linha['Idade'])
    modalidade = str(linha['Modalidade'])

    # JIU-JITSU
    if modalidade == 'Jiu-Jitsu':
        if idade <= 6:
            return 'Pré-mirim'
        elif idade <= 9:
            return 'Mirim'
        elif idade <= 12:
            return 'Infantil'
        elif idade <= 15:
            return 'Infanto-Juvenil'
        elif idade <= 17:
            return 'Juvenil'
        elif idade <= 29:
            return 'Adulto'
        elif idade <= 35:
            return 'Master 1'
        elif idade <= 40:
            return 'Master 2'
        elif idade <= 45:
            return 'Master 3'
        elif idade <= 50:
            return 'Master 4'
        elif idade <= 55:
            return 'Master 5'
        elif idade <= 60:
            return 'Master 6'
        else:
            return 'Master 7'

    # LUTA LIVRE ESPORTIVA
    elif modalidade == 'Luta Livre Esportiva':
        if idade <= 9:
            return 'Mirim'
        elif idade <= 12:
            return 'Infanto-Juvenil'
        elif idade <= 17:
            return 'Juvenil'
        elif idade <= 29:
            return 'Adulto'
        elif idade <= 35:
            return 'Master 1'
        elif idade <= 40:
            return 'Sênior'
        else:
            return 'Veteran'

    return 'Indefinido'

df['categoria_idade'] = df.apply(categoria_idade, axis=1)

# CATEGORIAS DE PESO
def categoria_peso(linha):
    peso = float(linha['Peso'])
    modalidade = str(linha['Modalidade'])
    cat_idade = str(linha['categoria_idade'])
    sexo = str(linha['Sexo']).strip().capitalize() # Normaliza para 'Feminino' ou 'Masculino'

    # JIU-JITSU
    if modalidade == 'Jiu-Jitsu':

        # PRÉ-MIRIM
        if cat_idade == 'Pré-mirim':
            if peso <= 15.00: return 'Galo'
            elif peso <= 18.00: return 'Pluma'
            elif peso <= 21.00: return 'Pena'
            elif peso <= 24.00: return 'Leve'
            elif peso <= 27.00: return 'Médio'
            elif peso <= 30.00: return 'Meio-pesado'
            elif peso <= 33.00: return 'Pesado'
            elif peso <= 36.00: return 'Super pesado'
            else: return 'Pesadíssimo'

        # MIRIM
        elif cat_idade == 'Mirim':
            if peso <= 21.00: return 'Pena'
            elif peso <= 24.00: return 'Leve'
            else: return 'Pesado'

        # INFANTIL
        elif cat_idade == 'Infantil':
            if peso <= 30.20: return 'Pena'
            elif peso <= 33.20: return 'Leve'
            else: return 'Pesado'

        # INFANTO-JUVENIL
        elif cat_idade == 'Infanto-Juvenil':
            if peso <= 48.30: return 'Pluma'
            elif peso <= 52.50: return 'Pena'
            elif peso <= 56.50: return 'Leve'
            else: return 'Pesado'

        # JUVENIL - FEMININO
        elif cat_idade == 'Juvenil' and sexo == 'Feminino':
            if peso <= 44.30: return 'Galo'
            elif peso <= 48.30: return 'Pluma'
            elif peso <= 52.50: return 'Pena'
            elif peso <= 56.50: return 'Leve'
            elif peso <= 60.50: return 'Médio'
            elif peso <= 65.00: return 'Meio-pesado'
            elif peso <= 69.00: return 'Pesado'
            else: return 'Pesadíssimo'

        # JUVENIL - MASCULINO
        elif cat_idade == 'Juvenil' and sexo == 'Masculino':
            if peso <= 53.50: return 'Galo'
            elif peso <= 58.50: return 'Pluma'
            elif peso <= 64.00: return 'Pena'
            elif peso <= 69.00: return 'Leve'
            elif peso <= 74.00: return 'Médio'
            elif peso <= 79.30: return 'Meio-pesado'
            elif peso <= 84.30: return 'Pesado'
            elif peso <= 89.30: return 'Super Pesado'
            else: return 'Pesadíssimo'

        # ADULTO E MASTER - FEMININO
        elif (cat_idade == 'Adulto' or cat_idade.startswith('Master')) and sexo == 'Feminino':
            if peso <= 48.50: return 'Galo'
            elif peso <= 53.50: return 'Pluma'
            elif peso <= 58.50: return 'Pena'
            elif peso <= 64.00: return 'Leve'
            elif peso <= 69.00: return 'Médio'
            elif peso <= 74.00: return 'Meio Pesado'
            else: return 'Super Pesado'

        # ADULTO E MASTER - MASCULINO
        elif (cat_idade == 'Adulto' or cat_idade.startswith('Master')) and sexo == 'Masculino':
            if peso <= 57.50: return 'Galo'
            elif peso <= 64.00: return 'Pluma'
            elif peso <= 70.00: return 'Pena'
            elif peso <= 76.00: return 'Leve'
            elif peso <= 82.30: return 'Médio'
            elif peso <= 88.30: return 'Meio Pesado'
            elif peso <= 94.30: return 'Pesado'
            elif peso <= 100.50: return 'Super Pesado'
            else: return 'Pesadíssimo'

    # LUTA LIVRE ESPORTIVA
    elif modalidade == 'Luta Livre Esportiva':

        # MIRIM
        if cat_idade == 'Mirim':
            if peso <= 20.00: return 'Até 20kg'
            elif peso <= 24.00: return 'Até 24kg'
            elif peso <= 28.00: return 'Até 28kg'
            elif peso <= 32.00: return 'Até 32kg'
            elif peso <= 36.00: return 'Até 36kg'
            elif peso <= 40.00: return 'Até 40kg'
            else: return 'Peso Livre'

        # INFANTO-JUVENIL - FEMININO
        elif cat_idade == 'Infanto-Juvenil' and sexo == 'Feminino':
            if peso <= 40.00: return 'Galo'
            elif peso <= 44.00: return 'Pluma'
            elif peso <= 48.00: return 'Pena'
            elif peso <= 52.00: return 'Leve'
            elif peso <= 56.00: return 'Médio'
            elif peso <= 60.00: return 'Meio Pesado'
            elif peso <= 65.00: return 'Pesado'
            else: return 'Super Pesado'

        # INFANTO-JUVENIL - MASCULINO
        elif cat_idade == 'Infanto-Juvenil' and sexo == 'Masculino':
            if peso <= 44.00: return 'Galo'
            elif peso <= 48.00: return 'Pluma'
            elif peso <= 52.00: return 'Pena'
            elif peso <= 56.00: return 'Leve'
            elif peso <= 60.00: return 'Médio'
            elif peso <= 65.00: return 'Meio Pesado'
            elif peso <= 70.00: return 'Pesado'
            elif peso <= 75.00: return 'Super Pesado'
            else: return 'Pesadíssimo'

        # JUVENIL - FEMININO
        elif cat_idade == 'Juvenil' and sexo == 'Feminino':
            if peso <= 44.00: return 'Galo'
            elif peso <= 48.00: return 'Pluma'
            elif peso <= 52.00: return 'Pena'
            elif peso <= 56.00: return 'Leve'
            elif peso <= 60.00: return 'Médio'
            elif peso <= 65.00: return 'Meio-pesado'
            elif peso <= 69.00: return 'Pesado'
            else: return 'Super Pesado'

        # JUVENIL - MASCULINO
        elif cat_idade == 'Juvenil' and sexo == 'Masculino':
            if peso <= 53.00: return 'Galo'
            elif peso <= 57.00: return 'Pluma'
            elif peso <= 62.00: return 'Pena'
            elif peso <= 67.00: return 'Leve'
            elif peso <= 73.00: return 'Médio'
            elif peso <= 78.00: return 'Meio-pesado'
            elif peso <= 84.00: return 'Pesado'
            elif peso <= 89.00: return 'Super Pesado'
            else: return 'Pesadíssimo'

        # ADULTO, MASTER, SÊNIOR E VETERAN - FEMININO
        elif (cat_idade in ['Adulto', 'Master 1', 'Sênior', 'Veteran']) and sexo == 'Feminino':
            if peso <= 48.00: return 'Galo'
            elif peso <= 52.00: return 'Pluma'
            elif peso <= 56.00: return 'Pena'
            elif peso <= 60.00: return 'Leve'
            elif peso <= 65.00: return 'Médio'
            elif peso <= 70.00: return 'Meio Pesado'
            elif peso <= 75.00: return 'Pesado'
            else: return 'Pesadíssimo'

        # ADULTO, MASTER, SÊNIOR E VETERAN - MASCULINO
        elif (cat_idade in ['Adulto', 'Master 1', 'Sênior', 'Veteran']) and sexo == 'Masculino':
            if peso <= 57.00: return 'Galo'
            elif peso <= 62.00: return 'Pluma'
            elif peso <= 66.00: return 'Pena'
            elif peso <= 73.00: return 'Leve'
            elif peso <= 79.00: return 'Médio'
            elif peso <= 85.00: return 'Meio Pesado'
            elif peso <= 92.00: return 'Pesado'
            elif peso <= 99.00: return 'Super Pesado'
            else: return 'Pesadíssimo'

    return 'Peso_Indefinido'

df['categoria_peso'] = df.apply(categoria_peso, axis=1)

# Gerando a chave de categoria combinada
df['categoria_chave'] = (df['Faixa'] + '-' + df['categoria_idade'] + '-' + df['categoria_peso'] + '-' + df['Sexo'])

# -------------------------------------------------- #
#        EXIBIÇÃO DOS ATLETAS POR CATEGORIA          #
# -------------------------------------------------- #

print("\n==================================================")
print("              ATLETAS POR CATEGORIA               ")
print("==================================================\n")

# Agrupa o DataFrame pela chave criada
for chave, grupo in df.groupby('categoria_chave'):
    print("-" * 50)
    print(f"🏆 CATEGORIA: {chave}")
    print(f"👥 Total de atletas: {len(grupo)}")
    print("-" * 50)

    # Pega os nomes daquela chave específica
    atletas = grupo['Nome Completo'].tolist()

    # Imprime cada atleta numerado
    for i, atleta in enumerate(atletas, 1):
        print(f"  {i}. {atleta}")

    print() # Linha em branco para separar da próxima categoria

import random
import math

print("\n==================================================")
print("            CHAVEAMENTO DOS CONFRONTOS            ")
print("==================================================\n")

for chave, grupo in df.groupby('categoria_chave'):
    atletas = grupo['Nome Completo'].tolist()
    n = len(atletas)

    print("=" * 55)
    print(f"🏆 CATEGORIA: {chave}")
    print(f"👥 Total de Atletas: {n}")
    print("=" * 55)

    # Caso 1: Apenas 1 atleta na categoria
    if n == 1:
        print(f"  🥇 Campeão(ã) por W.O. (Sem adversários): {atletas[0]}\n")
        continue

    # Embaralha os atletas da categoria
    random.shuffle(atletas)

    # Calcula o tamanho ideal da chave (2, 4, 8, 16...) e ajusta os 'BYEs'
    tamanho_chave = 2 ** math.ceil(math.log2(n))
    num_byes = tamanho_chave - n
    participantes = atletas + ['BYE'] * num_byes

    # --- 1ª RODADA ---
    print("\n  --- 1ª RODADA ---")
    luta_id = 1
    proxima_rodada_slots = []

    for i in range(0, tamanho_chave, 2):
        p1 = participantes[i]
        p2 = participantes[i+1]

        if p1 == 'BYE':
            print(f"  Luta {luta_id}: {p2} -> Passa direto (BYE)")
            proxima_rodada_slots.append(f"Vencedor Luta {luta_id} ({p2})")
        elif p2 == 'BYE':
            print(f"  Luta {luta_id}: {p1} -> Passa direto (BYE)")
            proxima_rodada_slots.append(f"Vencedor Luta {luta_id} ({p1})")
        else:
            print(f"  Luta {luta_id}: {p1}  VS  {p2}")
            proxima_rodada_slots.append(f"Vencedor da Luta {luta_id}")

        luta_id += 1

    # --- RODADAS SEGUINTES (Semis, Final...) ---
    rodada_num = 2
    while len(proxima_rodada_slots) > 1:
        novos_slots = []
        nome_fase = "FINAL" if len(proxima_rodada_slots) == 2 else f"RODADA {rodada_num}"
        print(f"\n  --- {nome_fase} ---")

        for i in range(0, len(proxima_rodada_slots), 2):
            l1 = proxima_rodada_slots[i]
            l2 = proxima_rodada_slots[i+1]

            rotulo_luta = "Disputa do Título" if nome_fase == "FINAL" else f"Luta {luta_id}"
            print(f"  {rotulo_luta}: [ {l1} ]  VS  [ {l2} ]")

            novos_slots.append(f"Vencedor da {rotulo_luta}")
            luta_id += 1

        proxima_rodada_slots = novos_slots
        rodada_num += 1

    print("\n")
