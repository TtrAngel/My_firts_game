from ast import While
import os
# import WConio2 as WConio2
import sys
import random


#desenhar o menu de opções
os.system('CLS')
print("____________________________________________________________")
print("\n")
print("\t\t\tComendo um monte:\n")
print("\t\t\tWelcome\n")
print("\t\t\t[S] Bora?")
print("\t\t\t[C] Sair\n\n")
print("____________________________________________________________")


resposta = input().strip().upper()


if resposta == "S":
  print("VOCÊ DECIDIU COMEÇAR.")
elif resposta == "C":
  print("VOCÊ DECIDIU SAIR.")
  sys.exit()


else:
  print("Opção inválida.")
  sys.exit()



os.system("PAUSE")


espaco = ' '
quantidade = 1.0
while True:
    #desenha a tela principal do jogo
    M = []          #criando a matriz vazia
    linhas = 20
    colunas = 50


    for i in range(linhas):
            M.append([])    #criando a linhas
            for j in range(colunas):
                M[i].append(' ') #adicionei elementos na linha i

    cobra = [
        [3, 3],
        [3, 2],
        [3, 1]
    ]

    pontuacao = 0

    bicho = '@'

    comidaI = 5
    comidaJ = 10
    comida = '*'



    ##bichoI = 3
    ##bichoJ = 3
    ##bicho = '@'


    os.system('cls')    #apaga a atela


    while(True):
                os.system('cls')    #apaga a tela
                # WConio2.gotoxy(0,0)  #apaga a tela


            #apagar a matriz
                for i in range(len(M)):          #todas as linhas
                    for j in range(len(M[i])):      #todas as colunas
                        M[i][j] = ' '       #conteúdo vazio


                    #desenhando os personagens
                for parte in cobra:
                    i = parte[0]
                    j = parte[1]

                    M[i][j] = bicho
                #M[bichoI][bichoJ] = bicho
                #M[bichoI+1][bichoJ] = bicho
                #M[bichoI+1][bichoJ-1] = bicho
                #M[bichoI+1][bichoJ+1] = bicho
                for parte in cobra:
                    i = parte[0]
                    j = parte[1]

                    M[i][j] = bicho

                    M[comidaI][comidaJ] = comida


                #imprimir uma matriz
                tela = ''
                tela += (colunas+2)*"#"
                tela += '\n'
                for i in range(len(M)):         #todas as linhas
                    tela += "#"
                    for j in range(len(M[i])):  #todas as colunas
                        tela += M[i][j]         #mostra o conteúdo
                    tela += "#\n"               #pular linha quando necessário
                tela += (colunas+2)*"#"
                tela += '\n'


                print(tela)
                print(f"Pontuação: {pontuacao}")


                #Temporariamente usaremos:

                tecla = input("Movimento (W/A/S/D): ").lower()

                novaI = cobra[0][0]
                novaJ = cobra[0][1]

                if tecla == 'a':
                    novaJ -= 1  
                elif tecla == 'd':
                    novaJ += 1
                elif tecla == 'w':
                    novaI -= 1
                elif tecla == 's':
                    novaI += 1

                else:
                    print("Tecla inválida.")
                    continue

                novaI = novaI % linhas
                novaJ = novaJ % colunas

                if [novaI, novaJ] in cobra:
                    print("Você perdeu! A cobra bateu no próprio corpo.")
                    break
                    

                if [novaI, novaJ] == [comidaI, comidaJ]:
                    print("Você comeu a comida!")
                    pontuacao += 10
                    cobra.insert(0, [novaI, novaJ])

    while True:

                        comidaI = random.randint(0, linhas - 1)
                        comidaJ = random.randint(0, colunas - 1)
                        if [comidaI, comidaJ] not in cobra:
                            break

                        else:

                            cobra.insert(0, [novaI, novaJ])
                            cobra.pop()
                    
                
                #Esta parte será utilizada depois.

                # if WConio2.kbhit():
                    # codigo, letra = Wconio2.getch()

                     #novaI = cobra[0][0]
                     #novaJ = cobra[0][1]

                     #if letra == 'a':
                        # novaJ -= 1 
                     #elif letra == 'd':
                       #  novaJ += 1
                    # elif letra == 'w':
                    #     novaI -= 1
                    # elif letra == 's':
                    #     novaI += 1

                    # else:
                     #    continue

                     #novaI = novaI % linhas
                     #novaJ = novaJ % colunas

                     #cobra.insert(0, [novaI, novaJ])
                     #cobra.pop()
                     

                     #Antiga

                #if(WConio2.kbhit()):  #verifica se uma tecla foi apertada
                    #codigo, letra = WConio2.getch()  #captura a tecla apertada


                    #if(letra == 'a' and bichoJ > 0):
                        #bichoJ -=1
                    #elif(letra == 'd' and bichoJ < (colunas-1)):
                       #bichoJ +=1
                    #if(letra == 'w' and bichoI > 0):
                        #bichoI -=1
                    #elif(letra == 's' and bichoI < (linhas-1)):
                        #bichoI +=1

            
    os.system('cls')

    print("============================================================")
    print("                         Fim de jogo")
    print("============================================================")
    print(f"Sua pontuação final foi: {pontuacao}")
    print("\nVocê perdeu!")
    
    input("\nPressione ENTER para sair...")
    break