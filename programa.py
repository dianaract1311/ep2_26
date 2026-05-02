from funcoes import *

# criar cartela inicial
cartela = {
    'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
    'regra_avancada': {
        'sem_combinacao':-1,
        'quadra': -1,
        'full_house': -1,
        'sequencia_baixa': -1,
        'sequencia_alta': -1,
        'cinco_iguais': -1
    }
}

rodadas = 0

while rodadas < 12:
    dados_rolados = rolar_dados(5)
    dados_guardados = []
    rerrolagens = 0

    jogou = False

    while not jogou:
        print(f"Dados rolados: {dados_rolados}")
        print(f"Dados guardados: {dados_guardados}")
        print("Digite 1 para guardar um dado, 2 para remover um dado, 3 para rerrolar, 4 para ver a cartela ou 0 para marcar a pontuação:")

        opcao = input()

        if opcao == "1":
            print("Digite o índice do dado a ser guardado (0 a 4):")
            idx = int(input())
            resultado = guardar_dado(dados_rolados, dados_guardados, idx)
            dados_rolados, dados_guardados = resultado

        elif opcao == "2":
            print("Digite o índice do dado a ser removido (0 a 4):")
            idx = int(input())
            resultado = remover_dado(dados_rolados, dados_guardados, idx)
            dados_rolados, dados_guardados = resultado

        elif opcao == "3":
            if rerrolagens < 2:
                novos = rolar_dados(5 - len(dados_guardados))
                dados_rolados = novos
                rerrolagens += 1
            else:
                print("Você já usou todas as rerrolagens.")

        elif opcao == "4":
            imprime_cartela(cartela)

        elif opcao == "0":
            print("Digite a combinação desejada:")
            categoria = input()

            # valida categoria
            if categoria.isdigit():
                cat_int = int(categoria)
                if cartela['regra_simples'][cat_int] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    jogou = True
                    rodadas += 1
            elif categoria in cartela['regra_avancada']:
                if cartela['regra_avancada'][categoria] != -1:
                    print("Essa combinação já foi utilizada.")
                else:
                    cartela = faz_jogada(dados_rolados + dados_guardados, categoria, cartela)
                    jogou = True
                    rodadas += 1
            else:
                print("Combinação inválida. Tente novamente.")

        else:
            print("Opção inválida. Tente novamente.")

# calcular pontuação final
pontuacao = 0

for i in cartela['regra_simples']:
    if cartela['regra_simples'][i] != -1:
        pontuacao += cartela['regra_simples'][i]

for i in cartela['regra_avancada']:
    if cartela['regra_avancada'][i] != -1:
        pontuacao += cartela['regra_avancada'][i]

# bônus
soma_simples = 0
for i in cartela['regra_simples']:
    if cartela['regra_simples'][i] != -1:
        soma_simples += cartela['regra_simples'][i]

if soma_simples >= 63:
    pontuacao += 35

imprime_cartela(cartela)
print(f"Pontuação total: {pontuacao}")