marks = {"physics" : 3,
         "english" : 2,
         "math" : 1,
         "webtech" : 5,
         "python" : 10}

val = 0
key = ''

for i in marks:
    m = marks[i]
    if val < m:
        val = m
        key = i
print('maximum : ', key, val)