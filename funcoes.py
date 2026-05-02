import random

def rolar_dados(n):
    lista = []
    i = 0
    
    while i < n:
        dado = random.randint(1, 6)
        lista.append(dado)
        i += 1
    
    return lista

def guardar_dado(dados_rolados, dados_no_estoque, dado_para_guardar):
    dado = dados_rolados[dado_para_guardar]
    
    nova_lista = []
    i = 0
    
    while i < len(dados_rolados):
        if i != dado_para_guardar:
            nova_lista.append(dados_rolados[i])
        i += 1
    
    dados_no_estoque.append(dado)
    
    return [nova_lista, dados_no_estoque]

def remover_dado(dados_rolados, dados_no_estoque, dado_para_remover):
    dado = dados_no_estoque[dado_para_remover]
    
    nova_lista = []
    i = 0
    
    while i < len(dados_no_estoque):
        if i != dado_para_remover:
            nova_lista.append(dados_no_estoque[i])
        i += 1
    
    dados_rolados.append(dado)
    
    return [dados_rolados, nova_lista]

def calcula_pontos_regra_simples(dados):
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