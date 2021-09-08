#Lists = used to store multiple itens in a sigle variable

food = ["pizza", "hotdog", "macarrão", "arroz"]
food[0] = "sushi"


#for i in range(food):

#food.pop()
food.append("sorvete")
food.remove("sushi")
food.insert(0, "bolinho")
food.sort()
#food.clear()


for x in food:
    print(x, end=" ")