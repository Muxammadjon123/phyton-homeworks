lst = [1, 2, 3, 4, 5]
sublst = [3, 4]
found = False
for i in range(len(lst) - len(sublst) + 1):
    if lst[i:i+len(sublst)] == sublst:
        found = True
        break
print(found)  
