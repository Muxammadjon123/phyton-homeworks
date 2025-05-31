lst = [1, 23, 1, 1, 1, 3, 4, 5]

if len(lst) % 2 == 0:
    mid1 = len(lst) // 2 - 1
    mid2 = len(lst) // 2
    print(lst[mid1])
    print(lst[mid2])
else:
    print(lst[len(lst) // 2])
