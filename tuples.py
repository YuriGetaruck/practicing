#tuples = colelction which io ordered and unchangable // used to group together related data // tuplas em pt-br

student = ("Yuri", 21, "masculino")

print(student.count("Yuri"), end = "  ")
print(student.index("masculino"))

for i in student:
    print(i)

if "Yuri" in student:
    print("Yuri esta aqui")