dct={
    'a':'apple',
    'b':'banana',
    'c':'carrot',
    'd':'dragon',
    'e':'egg'
}
val='banana'
count=0
for i in dct.values():
    if i==val:
        count+=1
print(count)