set1={1,2,3,4,5,6}
set2={7,8,9}
common=False
for i in set1:
    for j in set2:
        if i==j:
            common=True
if common:
    print("Yes they have")
else:
    print("No they don't have")