# t = tuple()
# item = input("Enter the Item : ").split()
# for i in item:
#     if item == "":
#         break
#     ls = list(t)
#     ls.append(item)
#     t1 = tuple(ls)
# print(t1,type(t1))

tp = (3,4,5,6)
item = int(input('Enter the item : '))
tp = tp + (item,)
print(tp)