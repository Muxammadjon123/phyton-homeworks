dct={
    'c':'apple',
    'e':'banana',
    'd':'carrot',
    'b':'dragon',
    'a':'egg'
}
new_dct={}
lst=list(dct.keys())
sorted_lst=sorted(lst)
for i in sorted_lst:
    new_dct.update({i:dct[i]})
print(new_dct)