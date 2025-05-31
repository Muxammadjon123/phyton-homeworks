lst=[1,23,1,1,1,3,4,5]
element=3
new_element=5
for i in range(len(lst)):
    if lst[i]==element:
        lst[i]=new_element
        break
print(lst)



