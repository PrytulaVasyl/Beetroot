str1 = input()
new_list = str1.split()
new_set = set(new_list)
dict1 = {i: new_list.count(i) for i in new_set}
print (dict1)