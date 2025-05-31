lst = [1, -2, 3, 1, -1, 1, -3, 4, 5]
new_lst=[]
for i in lst:
    if i not in new_lst:
        new_lst.append(i)
print(new_lst)