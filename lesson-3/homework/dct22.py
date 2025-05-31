dct={
    'c':'apple',
    'e':'banana',
    'd':'carrot',
    'b':'dragon',
    'a':'egg'
}
new_dct={}
for j in dct.keys():
    for i in dct.values():
        if dct[j]==i and len(i)==3:
            new_dct.update({j:i})
print(new_dct)