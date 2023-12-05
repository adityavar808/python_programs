st = input('Enter the string :')

reg = ''"
for i in st:
    if i not in reg:
        reg += i

print(reg)
