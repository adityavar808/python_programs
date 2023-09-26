num = int(input('Enter the number : '))
cp = num
s = 0

while num !=0:
    r = num % 10
    s = s*10 + r
    num = num // 10

if cp == s:
    print(f"{cp} is Palindrome.")

else:
    print(f"{cp} is not Palindrome.")
