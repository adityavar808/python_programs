st = input("Enter The String : ")

reg = ""

for i in st:
    if st.count(i) >= 2 and i not in reg:
        reg += i

print(reg)
