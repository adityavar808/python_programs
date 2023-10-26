num = input("Enter the Numbers : ").split()

ls = [int(i) for i in num]
reg = []

for i in ls:
    if i not in reg:
        reg.append(i)
        
maxls1 =  max(reg)
reg.remove(maxls1)
        
maxls2 = max(reg)
print(maxls2)
