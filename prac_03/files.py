name = input ("Enter your name:")
file = open ('name.txt','w')
file.write (name)
file.close()

file = open ('name.txt', 'r')
name_from_file = file.read()
file.close()

print(f"Hello {name_from_file}!")

with open ('numbers.txt','r')  as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
    result = number1 +number2
    print (result)

total = 0
with open ('numbers.txt','r') as file:
    for line in file:
        total += int(line.strip())
print (total)
