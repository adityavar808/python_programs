def prime(num):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count = count + 1
    
    if count == 2:
        return True
    else:
        return False

lst = [1,2,3,4,5,6,7,8,9,10]
print('prime number: ',  lst)
out = list(map(prime, lst))
print(out)