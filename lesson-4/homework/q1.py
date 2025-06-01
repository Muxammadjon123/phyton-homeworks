list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_lst=[]
for i in list1:
    if i not in list2:
        new_lst.append(i)
for i in list2:
    if i not in list1:
        new_lst.append(i)
print(new_lst)