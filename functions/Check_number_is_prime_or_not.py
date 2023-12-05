def prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
        
    if count == 2:
        return "Number is Prime."
    else:
        return "Number is not Prime."
            
num = int(input("Enter the Number : "))
out = prime(num)
print(out)