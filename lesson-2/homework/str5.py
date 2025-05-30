txt=input("Please enter the string:")
vowels="aeuioAEOUI"
v=0
c=0
for i in txt:
    if i in vowels:
        v+=1
    else:
        c+=1
print(c,v)