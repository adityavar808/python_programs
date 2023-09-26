num = int(input("Enter The Number : "))
cp = num
pw = 0

while num!= 0:
    num = num // 10
    pw = pw + 1

num = cp
s = 0
while num != 0:
    r = num % 10
    s = s + r ** pw
    num = num // 10
print('Armstrong number' if cp == s else 'Not a Armstrong')
