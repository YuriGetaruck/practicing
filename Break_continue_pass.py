#break = terminate de loop // temina o loop
#continue = skips to the enxt interaction // vai para a proxima interação
#pass = does nothing, acts like a place holder // nao faz nada, apenas ocupa o lugar de uma interação

#while True:
#    name = input("enter your name: ")
#    if name != "":
#        break


phone_number = "123-456-789"

for i in phone_number:
    if i == "-":
        pass
    print(i, end="")

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)