tpl=(1,2,3,3,2,1)
lst=(list(tpl))
if lst==lst[::-1]:
    print("Yes palindrome")
else:
    print("No it is not palindrome")