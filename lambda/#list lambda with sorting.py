#list lambda with sorting

apna_fun = lambda st:st[-1]

ls = ['aditya', 'aditya Tiwari', 'arjun', 'afzal']
print('Before sorting', ls)
ls.sort(key = apna_fun)
print('Afetr sorting', ls)