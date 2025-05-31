dct = {
    'a': 'bpple',
    'b': 'canana',
    'c': 'aarrot',
    'd': 'eragon',
    'e': 'dgg'
}
new_dct = {}
lst = list(dct.values())          
sorted_lst = sorted(lst)          
for val in sorted_lst:
    for key in dct:
        if dct[key] == val and key not in new_dct:
            new_dct[key] = val     
            break
print(new_dct)
