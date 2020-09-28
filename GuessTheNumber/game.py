

# import libraries
import random

# Step 1 . set the min and max int and a counter
min = 0
max = 100
count = 0


# Step 2. generate a random number within the range(min, max)

random_int = random.randint(min, max)
# cheating
# print(str(random_int))

# Step 3. Loop, break if the player win the game
while True:

    # Ask for player input
    my_guess = int(input("Guess a number: "))
    count+=1

    # Compare user input to the random integer
    if my_guess == random_int:
        print("The number is "+str(random_int)+". You won in "+ str(count) + " tries")
        break
    elif my_guess < random_int:
        print("The number is greater than "+str(my_guess))
    else:
        print("The number is less than "+str(my_guess))