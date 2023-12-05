def apna_fun(x):
    return x % 2 == 0

lst = [4,6,7,8,10]
print('Before mapping', lst)
out = list(map(apna_fun, lst))
print('After mapping', out)