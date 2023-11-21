marks = {"physics" : 3,
         "english" : 2,
         "math" : 1,
         "webtech" : 5,
         "python" : None}
 
mul = 1
 
# run a loop
for i in marks:
    val = marks[i]
    if type(val) == int:
        mul *= val
# print answer
print(mul)