import copy
count = 0
list3 = []
while count != len(list1):
    list3.append(copy.copy(list1[count]))
    count += 1
else:
    print(list3)
    print(id(list1))
    print(id(list3))

