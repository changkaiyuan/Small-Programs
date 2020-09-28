# import libraries
import random

# simulate rolling dice with given dice number
def dice_rolling(dice_num):
    i = 0
    result=[]
    while i < dice_num:
        i+=1
        result.append(random.randint(1,6))
    return result


while True:
    is_rolling = input("Rolling? (y/n)")
    if is_rolling=='y' or is_rolling=="Y":
        print("Result:", end=" ")   
        print(dice_rolling(3))

    else:
        break


