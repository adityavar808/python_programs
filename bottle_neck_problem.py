num = input("Enter the Radius of bottle : ").split()

ls = [int(i) for i in num]
ls2 = []

for i in ls:
    t = ls.count(i)
    ls2.append(i)
    
print(t)
