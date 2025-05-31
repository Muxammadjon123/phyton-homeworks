dct={
    'c':'apple',
    'e':'banana',
    'd':'carrot',
    'b':'dragon',
    'a':'egg'
}
dct2={
    'c':1,
    'b':4
}
for i in dct.keys():
    for j in dct2.keys():
        if i==j:
            print(i)