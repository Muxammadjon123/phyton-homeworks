txt=input("Please enter the string:")
reversed_txt=txt[::-1]
if txt==reversed_txt:
    print("Palindrome")
else:
    print("Not palindrome")