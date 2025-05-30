txt=input("Please enter the string:")
character=input("Please enter the character:")
txt_new=""
for i in txt:
    if i!=character:
        txt_new+=i
print(txt_new)