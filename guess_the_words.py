# guess the words(provide hint + deduct points)


import random

words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya", "quince", "raspberry", "strawberry", "tangerine", "watermelon", "zucchini"]

def shuffled_word():
    word = random.choice(words)
    word_list = list(word)
    random.shuffle(word_list)
    shuffled= ''.join(word_list)
    return shuffled, word

def select_function(shuffled,  word, points):
    print("Your points are : ", points)

    print("The shuffled word is : ", shuffled)
    try:
        seleect_function = int(input("enter '1'to write answer, '2' to get hint, '3' new word and '4' to exit:" )) 
    except:
        print("Invalid input. Please enter a valid number.")
        return select_function(shuffled, word, points)
    if seleect_function == 1:
        check_guess(word, points)
    elif seleect_function == 2:
        points = deduct_points(points)
        hint(word, shuffled, points)
    elif seleect_function == 3:
        new_shuffled, new_word = shuffled_word()
        select_function(new_shuffled, new_word, points)
    elif seleect_function == 4:
        exit()
    else:
        print("Please enter valid input")
        select_function(shuffled, word, points)
    

def hint(word, shuffled, points):
    if word == "apple":
        print("Hint: It fell into Newton's head")
    elif word == "banana":
        print("Hint: It gives fruit once in a plant and is yellow in color")
    elif word == "cherry":
        print("Hint: It is a red fruit and is used in ice cream")
    elif word == "date":
        print("Hint: It is a dry fruit and is eaten during fasts")
    elif word == "elderberry":
        print("Hint: It is a fruit and is used in wine")
    elif word == "fig":
        print("Hint: It is used in pudding and a small insect is born in it")
    elif word == "grape":
        print("Hint: It is used in wine, is round, and grows in vines")
    elif word == "honeydew":
        print("Hint: It is sweet in taste")
    elif word == "kiwi":
        print("Hint: It is used in ice cream")
    elif word == "lemon":
        print("Hint: It is sour in taste")
    elif word == "mango":
        print("Hint: It is known as the king of fruits")
    elif word == "nectarine":
        print("Hint: It is used in ice cream")
    elif word == "orange":
        print("Hint: It is orange in color")
    elif word == "papaya":
        print("Hint: It is used in ice cream")
    elif word == "quince":
        print("Hint: It is used in ice cream")
    elif word == "raspberry":
        print("Hint: It is used in ice cream")
    elif word == "strawberry":
        print("Hint: It is used in ice cream")
    elif word == "tangerine":
        print("Hint: It is used in ice cream")
    elif word == "watermelon":
        print("Hint: It is used in ice cream")
    elif word == "zucchini":
        print("Hint: It is used in ice cream")
    select_function(shuffled, word, points)

        


def check_guess(word, points):
    guess = input("Enter the guessed word : ").strip().lower()
    if guess == word:
        print("You have guessed the correct word")

    else:
        points = deduct_points(points)
        print("You have guessed wrong word. The correct word is : ", word)
    new_shuffled, new_word = shuffled_word()
    select_function(new_shuffled, new_word, points)

# deduct points for hint

def deduct_points(points):
    points -= 1
    if points <= 0:
        print("GAME OVER")
        exit()
    return points


shuffled, word = shuffled_word()
select_function(shuffled, word, 10)
