import random

ran = random.randint(1,10)
result = int(input("number between (0,10):"))
while True:
    if result < 0 or result > 10:
        print("Error! wrong value")
        result = int(input("try again: "))
    if result != ran:
        result = int(input("Try again: "))
    else:
        print(f"win!! you guessed it. It was {result}")
        break
