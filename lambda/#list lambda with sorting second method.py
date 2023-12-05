#list lambda with sorting

ls = ['aditya', 'aditya Tiwari', 'arjun', 'afzal']
print('Before sorting', ls)
ls.sort(key = lambda st: sum([ord(i) for i in st]))
print('Afetr sorting', ls)