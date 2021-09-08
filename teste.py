
i = 1
cont = 0
tamanho = int(input('Digite até aonde voce gostaria de verificar os numeros primos: '))
while i < tamanho:

    contador = 0
    divid = 0


    for j in range (i+1):
        if(i % (j+1) == 0):
            contador = contador + 1
    if contador == 2:
        cont = cont+1
        print('Numero Primo: {} , este é o {}º numero primo'.format(i,cont))
    i=i+1
