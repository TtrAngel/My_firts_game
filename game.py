
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
print("\t\t\t   CDDomendo um monte:\n")
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

pausado = False
tempo_inicio = time.perf_counter()
tempo_total_pausado = 0.0
inicio_pausa = 0.0

Wconio2.clrscr()
Wconio2.setcursortype(0)  # Esconde o cursor

try:
    while True:
        # 1. Verifica se alguma tecla foi pressionada
        if Wconio2.kbhit():
            tecla = Wconio2.getch()[1].lower()

            if tecla == 'p':
                pausado = not pausado  # Alterna entre pausado e rodando

                if pausado:
                    inicio_pausa = time.perf_counter()
                    Wconio2.gotoxy(0, 3)
                    Wconio2.cputs("=== JOGO PAUSADO (Pressione P para voltar) ===")
                else:
                    # Soma o tempo que ficou parado ao acumulador
                    tempo_total_pausado += time.perf_counter() - inicio_pausa
                    Wconio2.gotoxy(0, 3)
                    Wconio2.cputs("                                              ")

            elif tecla == 'q':  # Tecla para sair
                break

        # 2. Lógica do jogo só roda se NÃO estiver pausado
        if not pausado:
            agora = time.perf_counter()
            tempo_decorrido = agora - tempo_inicio - tempo_total_pausado

            Wconio2.gotoxy(0, 1)
            Wconio2.cputs(f"Tempo de jogo: {tempo_decorrido:.1f}s   ")
            Wconio2.gotoxy(0, 5)
            Wconio2.cputs("Pressione 'P' para pausar ou 'Q' para sair.")

            # Coloque aqui a movimentação dos personagens, pontuação, etc.

        time.sleep(0.05)  # Evita uso excessivo da CPU

finally:
    Wconio2.setcursortype(1)  # Restaura o cursor ao sair
    Wconio2.clrscr()

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