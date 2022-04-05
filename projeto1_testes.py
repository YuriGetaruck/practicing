

tabuleiro = [['O',2,3,],[4,'O',6],[5,4,'O',]]
contO = 0
print(tabuleiro[1][0])

for i in range(3):
    if(tabuleiro[i][1] == 'O'):
        contO += 1
        if(contO == 3):
            print("jogador O vence!!!")

if((tabuleiro[0][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[2][2] == 'O') or (tabuleiro[2][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[0][2] == 'O')):
            print("jogador O vence!!!")
            print('aqui')