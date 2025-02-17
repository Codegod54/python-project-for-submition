# guess the number from 1 to 10
import random
guess = int(input("Guess the numbe from 1 to 10 :"))
def guess_the_number():
    number = random.randint(1, 10)
    if number == guess :
        print("You have guessed the correct number")

    else :
        print("You have guessed wrong numbrer. The correct number is : ", number)




guess_the_number()



