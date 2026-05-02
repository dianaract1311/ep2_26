import random

def rolar_dados(n):  ## question 1
    lista = []
    i = 0
    
    while i < n:
        dado = random.randint(1, 6)
        lista.append(dado)
        i += 1
    
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):  ## question 2
    dado = dados_rolados[dado_para_guardar]
    
    nova_lista = []
    i = 0
    
    while i < len(dados_rolados):
        if i != dado_para_guardar:
            nova_lista.append(dados_rolados[i])
        i += 1
    
    dados_no_estoque.append(dado)
    
    return [nova_lista, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):  ## question 3
    dado = dados_no_estoque[dado_para_remover]
    
    nova_lista = []
    i = 0
    
    while i < len(dados_no_estoque):
        if i != dado_para_remover:
            nova_lista.append(dados_no_estoque[i])
        i += 1
    
    dados_rolados.append(dado)
    
    return [dados_rolados, nova_lista]

def calcula_pontos_regra_simples(dados):  ## question 4
    resultado = {}
    
    i = 1
    while i <= 6:
        soma = 0
        
        j = 0
        while j < len(dados):
            if dados[j] == i:
                soma += i
            j += 1
        
        resultado[i] = soma
        i += 1
    
    return resultado

def calcula_pontos_soma(dados):  ## question 5
    soma = 0
    i = 0
    
    while i < len(dados):
        soma += dados[i]
        i += 1
    
    return soma

def calcula_pontos_sequencia_baixa(dados): ## question 6
    # tirar repetidos
    valores = []
    i = 0
    while i < len(dados):
        if dados[i] not in valores:
            valores.append(dados[i])
        i += 1

    # verificar sequências
    if (1 in valores and 2 in valores and 3 in valores and 4 in valores):
        return 15
    if (2 in valores and 3 in valores and 4 in valores and 5 in valores):
        return 15
    if (3 in valores and 4 in valores and 5 in valores and 6 in valores):
        return 15

    return 0

def calcula_pontos_sequencia_alta(dados):  ## question 7
    # tirar repetidos
    valores = []
    i = 0
    while i < len(dados):
        if dados[i] not in valores:
            valores.append(dados[i])
        i += 1

    # verificar sequências de 5
    if (1 in valores and 2 in valores and 3 in valores and 4 in valores and 5 in valores):
        return 30
    if (2 in valores and 3 in valores and 4 in valores and 5 in valores and 6 in valores):
        return 30

    return 0

def calcula_pontos_full_house(dados):  ## question 8
    contagem = {}
    i = 0

    # contar ocorrências
    while i < len(dados):
        valor = dados[i]
        
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
        
        i += 1

    # pegar quantidades
    quantidades = []
    chaves = list(contagem.keys())
    i = 0
    
    while i < len(chaves):
        quantidades.append(contagem[chaves[i]])
        i += 1

    # verificar full house
    if 3 in quantidades and 2 in quantidades:
        soma = 0
        i = 0
        
        while i < len(dados):
            soma += dados[i]
            i += 1
        
        return soma

    return 0

def calcula_pontos_quadra(dados):  ## question 9
    contagem = {}
    i = 0

    # contar ocorrências
    while i < len(dados):
        valor = dados[i]
        
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
        
        i += 1

    # verificar se existe 4 ou mais
    chaves = list(contagem.keys())
    i = 0
    
    while i < len(chaves):
        if contagem[chaves[i]] >= 4:
            soma = 0
            j = 0
            
            while j < len(dados):
                soma += dados[j]
                j += 1
            
            return soma
        
        i += 1

    return 0

def calcula_pontos_quina(dados):   ## question 10
    contagem = {}
    i = 0

    # contar ocorrências
    while i < len(dados):
        valor = dados[i]
        
        if valor in contagem:
            contagem[valor] += 1
        else:
            contagem[valor] = 1
        
        i += 1

    # verificar se existe 5 ou mais
    chaves = list(contagem.keys())
    i = 0
    
    while i < len(chaves):
        if contagem[chaves[i]] >= 5:
            return 50
        i += 1

    return 0

def calcula_pontos_regra_avancada(dados):  ## question 11
    resultado = {}
    
    resultado['cinco_iguais'] = calcula_pontos_quina(dados)
    resultado['full_house'] = calcula_pontos_full_house(dados)
    resultado['quadra'] = calcula_pontos_quadra(dados)
    resultado['sem_combinacao'] = calcula_pontos_soma(dados)
    resultado['sequencia_alta'] = calcula_pontos_sequencia_alta(dados)
    resultado['sequencia_baixa'] = calcula_pontos_sequencia_baixa(dados)
    
    return resultado

def faz_jogada(dados, categoria, cartela_de_pontos):  ## question 12
    # regra simples
    if categoria == "1" or categoria == "2" or categoria == "3" or categoria == "4" or categoria == "5" or categoria == "6":
        pontos_simples = calcula_pontos_regra_simples(dados)
        cartela_de_pontos['regra_simples'][int(categoria)] = pontos_simples[int(categoria)]
    
    # regra avançada
    else:
        pontos_avancados = calcula_pontos_regra_avancada(dados)
        cartela_de_pontos['regra_avancada'][categoria] = pontos_avancados[categoria]
    
    return cartela_de_pontos