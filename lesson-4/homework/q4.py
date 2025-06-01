import random
while True:
    number = random.randint(1, 100)
    attempts=0

    while attempts<10:
        user_choice=int(input("Please enter your guess:"))
        attempts+=1
        if user_choice>number:
            print("Too high")
        elif user_choice<number:
            print("Too low")
        else:
            print("You found!!!!!")
            break
    else:
        print("You failed")
    
    n=input("Wanna play again(yes or no)")
    if n=='no':
        break