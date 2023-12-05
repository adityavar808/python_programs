lst = [4,6,7,8,10]
print('Before mapping', lst)
out = list(map(lambda n: n + 3, lst))
print('After mapping', out)