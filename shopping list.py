#shopping list
ls = []

while 1:
    item = input("Enter the Item : ")
    if item == "":
        break
    ls.append(item)
    
ls.sort()
print(ls)
