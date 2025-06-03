number=int(input("Please enter a positive integar:"))

factor=[num for num in range(1,number+1) if number%num==0]
for i in factor:
    print(f"{i} is factor of {number}")