

tabuleiro = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

roda_jogo = True

def imprime_tabuleiro(tab):
    i=j=0
    for i in range(3):
        for j in range(3):
            print(tabuleiro[i][j], end ="\t")
        print("\n")

def recebe_jogada_O():
    print("Jogador 'O' escolha uma posiçao do tabuleiro: ", end = " ")

    A = int(input())

    for i in range(3):
        for j in range(3):
            if A == tabuleiro[i][j]:
                tabuleiro[i][j] = 'O'

def recebe_jogada_X():
    print("Jogador 'X' escolha uma posiçao do tabuleiro: ", end = " ")

    A = int(input())

    for i in range(3):
        for j in range(3):
            if A == tabuleiro[i][j]:
                tabuleiro[i][j] = 'X'

def verifica_vitoria():

    contO_vert = contX_vert = contO_diag = contX_diag = 0


    for i in range(3):
        if(tabuleiro[i] == ['O','O','O']):
            print("jogador O vence!!!")
            exit()

        elif(tabuleiro[i] == ['X','X','X']):
            print("jogador X vence!!!")
            exit()

        elif(tabuleiro[i][0] == 'O'):
            contO_vert += 1
            if(contO_vert == 3):
                print("jogador O vence!!!")
                exit()

        elif(tabuleiro[i][0] == 'X'):
            contX_vert += 1
            if(contX_vert == 3):
                print("jogador X vence!!!")
                exit()

        elif(tabuleiro[i][1] == 'O'):
            contO_vert += 1
            if(contO_vert == 3):
                print("jogador O vence!!!")
                exit()

        elif(tabuleiro[i][1] == 'X'):
            contX_vert += 1
            if(contX_vert == 3):
                print("jogador X vence!!!")
                exit()
        
        elif(tabuleiro[i][2] == 'O'):
            contO_vert += 1
            if(contO_vert == 3):
                print("jogador O vence!!!")
                exit()

        elif(tabuleiro[i][2] == 'X'):
            contX_vert += 1
            if(contX_vert == 3):
                print("jogador X vence!!!")
                exit()
        
        elif((tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O') or (tabuleiro[2][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[0][2] == 'O')):
            print("jogador O vence!!!")
            exit()
        
        elif((tabuleiro[0][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[2][2] == 'X') or (tabuleiro[2][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[0][2] == 'X')):
            print("jogador X vence!!!")
            exit()


print("---------------------------")
print('Vamos jogar o jogo da velha')
print(" O primeiro jogador é 'O' ")

while roda_jogo:
    imprime_tabuleiro(tabuleiro)
    verifica_vitoria()
    recebe_jogada_O()
    imprime_tabuleiro(tabuleiro)
    verifica_vitoria()
    recebe_jogada_X()


