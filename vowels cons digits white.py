st = input("Enter the string :")

vowels = 0
cons = 0
digits = 0
space = 0

for i in st:

    if i in 'aeiouAEIOU':
        vowels += 1

    elif i.isalpha():
        cons += 1

    elif i.isdigit():
        digits += 1

    elif i.isspace():
        space += 1

print("Vowels : ",vowels)
print("Consonats : ",cons)
print("Digits : ",digits)
print("Whitespaces : ",space)
