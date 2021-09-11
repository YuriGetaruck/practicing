

capitals = {'USA':'Washington DC', 'Brazil': 'brasilia', "China":"Beijing", "Russia":"Moscow"}

#print(capitals["Germany"])

print(capitals.get('Germany'))

print(capitals.keys())
print(capitals.values())
print(capitals.items())


for key, value in capitals.items():
    print(key, value)

capitals.update({"Germany": "Berlim"})
print(" ")


for key, value in capitals.items():
    print(key, value)

capitals.update({"USA":"Las vegas"})
print()
for key, value in capitals.items():
    print(key, value)

capitals.pop("USA")

print()

for key, value in capitals.items():
    print(key, value)

