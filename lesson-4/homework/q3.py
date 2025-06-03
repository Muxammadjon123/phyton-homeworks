choice=input("Please enter the character:")
unli=['a','e','o','u','i']
lst=[]
count=0
for i in choice:
    if (count+1)%3==0 and i not in unli and i!=choice[len(choice)-1]:
        lst.append(i)
        lst.append('_') #Muammmo shotta bo'lishi mumkin
        unli.append(i)
    else:
        lst.append(i)
        count+=1


final=''.join(lst)
print(final)

