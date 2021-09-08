#sets =  collenction which is unordered, unidexed. no duplicate values // Os sets são uma coleção de itens desordenada, parcialmente imutável e que não podem conter elementos duplicados.

utensils = {"fork", "spoon", "knife", "plate"}

dishes = {"bowl", "plate", "cup"}


utensils.add("guardanapo")
utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)

dinner_table = utensils.union(dishes)

print(dinner_table)

for i in utensils:
    print(i, end = "  ")
print()

print(dishes.difference(utensils))
print(utensils.intersection(dishes))
