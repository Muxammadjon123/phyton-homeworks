dct={
    'a':'apple',
    'b':'banana',
    'c':'carrot',
    'd':'dragon',
    'e':'egg'
}
lst=[]
for i in dct.values():
    lst.append(i)
print(len(set(lst)))