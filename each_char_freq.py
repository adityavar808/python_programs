str1 = input("Enter the string : ")
reg = ''

for i in str1:
    if i not in reg:
        print(f'{i}: {str1.count(i)}')
        reg = reg + i

