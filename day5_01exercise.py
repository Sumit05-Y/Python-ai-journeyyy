import random
num = random.randint(0,100)
attempt=7
for i in range(0,7):
    guess=int(input("enter the number you guess:"))
    if guess > num:
        print("TOO HIGH")
        attempt -=1
        print(f"no of attempt left : {attempt}")
    elif guess < num:
        print("TOO LOW")
        attempt -=1
        print(f"no of attempt left : {attempt}")
    else:
        print(f"good job you guessed it right.The number is {num}")
        break
if attempt==0:
        print(f"The number was {num}")
        print("No attempt left")

       
