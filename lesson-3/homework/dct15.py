dct={}
lst=['a','b','c']
lst2=[1,2,3]
for i in range(0,len(lst)):
    dct.update({lst[i]:lst2[i]})
print(dct)