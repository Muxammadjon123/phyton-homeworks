def invest(amount,year,rate):
    for i in range(1,year+1):
        amount=amount+amount*rate
        print(f"year {i}:{round(amount,2)}")

invest(100,4,0.05)

