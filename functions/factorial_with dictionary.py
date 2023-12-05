def fac(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact

dict = {}
while 1:
    num = int(input("Enter the Number : "))
    out = fac(num)
    print(f"Factorial of {num} is {out}.")
    dict[num] = out
    print("Do you want to continue Y/N ?")
    if input() != 'Y':
        print(f"Your all Result {dict}")
        break