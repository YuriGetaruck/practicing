import signal


my_file = open('text.txt')
my_file.seek(0)


a = my_file.read()

#print(a)

for line in my_file:
    print(line)
