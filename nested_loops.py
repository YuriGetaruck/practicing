#nested loops (recurção)

rows = int(input("how many rows?:"))
columns = int(input("how many columns?:"))
symbol = input("Enter e symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()