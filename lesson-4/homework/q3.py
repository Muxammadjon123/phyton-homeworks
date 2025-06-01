choice=input("Please enter the character:")
unli='aeoui'
lst=[]
already_added=[]
count=0
for i in choice:
    if (count+1)%3==0 and i not in unli and i not in already_added and i!=choice[len(choice)-1]:
        lst.append(i)
        lst.append('_') #Muammmo shotta bo'lishi mumkin
        already_added.append(i)
    else:
        lst.append(i)
        count+=1


final=''.join(lst)
print(final)

