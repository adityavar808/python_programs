def even(num):
    if num % 2 == 0:
        return "Number is Even."
    else:
        return "Number is not Even."
    
num = int(input("Enter the Number : "))
out = even(num)
print(out)