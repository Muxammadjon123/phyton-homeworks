dct={
    'a':'apple',
    'b':'banana',
    'c':'carrot',
    'd':'dragon',
    'e':'egg'
}
dct2={
    "f":'fruit',
    'g':'grape'
}
combined = dict(list(dct.items()) + list(dct2.items()))
print(combined)