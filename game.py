
import os
import sys
import random
import time
import WConio2 as Wconio2
import WConio2


# Desenhar o menu de opções
os.system('cls')

amarelo = '\033[33m'
branco = '\033[m'
vermelho = '\033[31m'
verde = '\033[32m'
azul =  '\033[34m'

print(amarelo)
print("____________________________________________________________")
print("\n")
print(azul)
print("\t\t\t   Comendo um monte:\n")
print(branco)
print("\t\t\t       WELCOME\n")
print(azul)
print("\t\t\t     [S] Bora?")
print("\t\t\t     [C] Sair\n\n")
print(amarelo)
print("____________________________________________________________")
print(branco)
resposta = input().strip().upper()

if resposta == "S":
    print("VOCÊ DECIDIU COMEÇAR.")

elif resposta == "C":
    print("VOCÊ DECIDIU SAIR.")
    sys.exit()

else:
    print("Opção inválida.")
    sys.exit()

os.system("pause")


# Configurações iniciais
espaco = ' '
linhas = 15
colunas = 35

while True:

    os.system('cls')

    # Criando a matriz
    M = []

    for i in range(linhas):
        M.append([])

        for j in range(colunas):
            M[i].append(' ')

    # Posição inicial da cobra
    cobra = [
        [3, 3],
        [3, 2],
        [3, 1]
    ]

    pontuacao = 0
    bicho = ':]'
    comida = '°'

    # Posição inicial da comida
    while True:
        comidaI = random.randint(0, linhas - 1)
        comidaJ = random.randint(0, colunas - 1)

        if [comidaI, comidaJ] not in cobra:
            break
    direcao = 'd'

    # Loop principal do jogo
    while True:
        Wconio2.gotoxy(0, 0) #apaga a tela

        # Apagar o conteúdo da matriz
        for i in range(linhas):
            for j in range(colunas):
                M[i][j] = ' '

        # Desenhar a cobra
        for parte in cobra:
            i = parte[0]
            j = parte[1]

            M[i][j] = bicho

        # Desenhar a comida
        M[comidaI][comidaJ] = comida

        # Imprimir o tabuleiro
        print("#" * (colunas + 2))

        for i in range(linhas):
            print("#" + "".join(M[i]) + "#")

        print("#" * (colunas + 2))

        print(f"Pontuação: {pontuacao}")

        # Capturar a tecla sem interromper o jogo
        if WConio2.kbhit():
            codigo, tecla = WConio2.getch()
            tecla = tecla.lower()

            if tecla in ['a', 'd', 'w', 's']:
                direcao = tecla
 
        # Posição da cabeça da cobra
        novaI = cobra[0][0]
        novaJ = cobra[0][1]

        # Movimentação conforme a direção atual
        if direcao == 'a':
            novaJ -= 1

        elif direcao == 'd':
            novaJ += 1

        elif direcao == 'w':
            novaI -= 1

        elif direcao == 's':
            novaI += 1
        # Permitir atravessar as bordas
        novaI = novaI % linhas
        novaJ = novaJ % colunas

        # Verificar se a cobra comeu
        comeu = [novaI, novaJ] == [comidaI, comidaJ]

        # Verificar colisão com o próprio corpo
        if [novaI, novaJ] in cobra[:-1]:
            break

        # Movimentar a cobra
        cobra.insert(0, [novaI, novaJ])

        if comeu:

            pontuacao += 10

            # Gerar nova comida em uma posição livre
            while True:
    
                comidaI = random.randint(0, linhas - 1)
                comidaJ = random.randint(0, colunas - 1)

                if [comidaI, comidaJ] not in cobra:
                    break
            

        else:
            cobra.pop()
        time.sleep(0.15)

    # Tela de fim de jogo
    os.system('cls')
    print(amarelo)
    print("============================================================")
    print(branco)
    print("\n\n")
    print("                         Fim de jogo")
    print(amarelo)
    print("\n\n")
    print("============================================================")
    print(azul)
    print(f"Sua pontuação final foi: {pontuacao}")
    print("\nVocê perdeu!")

    input("\nPressione ENTER para sair...")
    break
