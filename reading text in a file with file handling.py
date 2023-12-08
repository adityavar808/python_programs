# file read
f = open('sample.txt', 'r')
data = f.read(16)
print(data)
f.close()