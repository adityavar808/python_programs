marks = {"physics" : 3,
         "english" : 2,
         "math" : 1,
         "webtech" : 5,
         "python" : None}

sum = 0

for i in marks:
    val = marks[i]
    if type(val) == int:
        sum += val
    

print(sum)