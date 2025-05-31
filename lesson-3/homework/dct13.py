dct={
    'a':'apple',
    'b':'banana',
    'c':'carrot',
    'd':'dragon',
    'e':'egg'
}
swapped = {v: k for k, v in dct.items()}
print(swapped)