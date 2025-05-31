dct={
    'a':'apple',
    'b':'banana',
    'c':'carrot',
    'd':'dragon',
    'e':'egg'
}
ky=input("Input:")
if ky in dct.keys():
    dct.pop(ky)
print(dct)