txt=input("Pleae enter the string:")
vowels="aeouiAEOUI"
txt_new=""
for i in txt:
    if i in vowels:
        txt_new+="*"
    else:
        txt_new+=i
        
print(txt_new)