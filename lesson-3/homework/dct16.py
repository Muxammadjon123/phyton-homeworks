dct={
    'a':'apple',
    'b':'banana',
    'c':{'x': 10, 'y': 20},
    'd':'dragon',
    'e':'egg'
}
indct=False
for i in dct.keys():
    if type(dct[i]).__name__=='dict':
        indct=True
        break
if indct:
    print("Yes one of the value is dictionary")
else:
    print("No")
