import os
import WConio2 as WConio2
import sys


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




    bichoI = 3
    bichoJ = 3
    bicho = '@'


    os.system('cls')    #apaga a atela


    while(True):
                WConio2.gotoxy(0,0)  #apaga a tela


            #apagar a matriz
                for i in range(len(M)):          #todas as linhas
                    for j in range(len(M[i])):      #todas as colunas
                        M[i][j] = ' '       #conteúdo vazio


                    #desenhando os personagens
                M[bichoI][bichoJ] = bicho
                M[bichoI+1][bichoJ] = bicho
                M[bichoI+1][bichoJ-1] = bicho
                M[bichoI+1][bichoJ+1] = bicho


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


                if(WConio2.kbhit()):  #verifica se uma tecla foi apertada
                    codigo, letra = WConio2.getch()  #captura a tecla apertada


                    if(letra == 'a' and bichoJ > 0):
                        bichoJ -=1
                    elif(letra == 'd' and bichoJ < (colunas-1)):
                        bichoJ +=1
                    if(letra == 'w' and bichoI > 0):
                        bichoI -=1
                    elif(letra == 's' and bichoI < (linhas-1)):
                        bichoI +=1







