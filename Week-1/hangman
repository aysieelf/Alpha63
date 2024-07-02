import random as rd
animals = [
    "Elephant",
    "Kangaroo",
    "Giraffe",
    "Hippopotamus",
    "Rhinoceros",
    "Chimpanzee",
    "Alligator",
    "Crocodile",
    "Flamingo",
    "Armadillo",
    "Porcupine",
    "Platypus",
    "Cheetah",
    "Jaguar",
    "Gorilla",
    "Penguin",
    "Peacock",
    "Tarantula",
    "Salamander",
    "Cockatoo",
    "Lemur",
    "Otter",
    "Meerkat",
    "Koala",
    "Wombat"
]

def get_word():
    word = (rd.choice(animals)).lower()

    return word


def get_initials_positions(word):

    word_lenght = len(word)
    bool_lst = word_lenght*[False]
    bool_lst[0], bool_lst[-1] = True,True

    return bool_lst


def hide_word(word, bool_lst):

    hidden_word = ""

    for i in range(len(bool_lst)):
        if bool_lst[i]:
            hidden_word+=word[i]
        else:
            hidden_word+="-"
    
    return hidden_word


def check_guess(word, letter, bool_lst):

    new_bool_lst = bool_lst.copy()
    if letter in word:
        for l in range(len(word)):
            if word[l] == letter:
                new_bool_lst[l] = True
    return new_bool_lst


def check_for_win(bool_lst):

    for _ in bool_lst:
        if _ == False:
            return False
    return True

def play_hangman():
    print("Guess the animal !")
    word = get_word()
    lives = 5
    positions = get_initials_positions(word)
    hidden = hide_word(word, positions)
 
    print(hidden)
 
    while True: # we will check for win or loss in the loop and break accordingly
        next_letter = input()
        new_positions = check_guess(word,next_letter,positions)
 
        # Option 1 - both lists are the same - the next_letter is not a correct guess
        if new_positions == positions:
            print('No such letter or already guessed')
            print(f'Lives remaining: {lives - 1}')
            lives = lives - 1
 
            if lives == 0: # no more lives - break
                print('You lose!')
                break
 
        # Option 2 - if the lists are not the  same, all values in new_positions may be True
        #    we use the check_for_win function to validate
        elif check_for_win(new_positions):
            print('You win!')
            break
 
        # Option 3 - the two lists are not the same, and new_postions is not all True - this means that another letter is guessed. We need to print it.
        else:
            print('Another letter guessed!')
            print(hide_word(word,new_positions))
 
            # it's important to update the positions list for the next iteration
            positions = new_positions 

play_hangman()
