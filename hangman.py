def get_word():     #Function to get a random word.
    import random
    words_list= open('words.txt','r') #Opening  text file.
    word=random.choice(words_list.readlines()).replace('\n','') #Getting random word.
    return(word)

def start(): #function to print welcome message and start the game.
    print('___Welcome__')
    print("""Rules for this game:
            1.Guess a word.
            2.You're allowed to guess using any letter of the alphabet.
            3.You have a total of 7 chances.
            4.If you fail to guess correctly, the hangman will be gradually drawn.""")
    print("Let's start the game.")

    masking_word()  #Calling masking_word function.


def image(chance):   #Function to display pictures.
    if chance ==  6:
        print("""|_______\n|  |\n|\n|\n|\n|\n|_""")
    elif chance == 5:
        print("""|_______\n|  |\n|  0\n|\n|\n|\n|""")
    elif chance == 4:
        print("""|_______\n|  |\n|  0\n| / \n|\n|\n|""")
    elif chance == 3:
        print("""|_______\n|  |\n|  0\n| / \\ \n|\n|\n|""")
    elif chance == 2:
        print("""|_______\n|  |\n|  0\n| /|\\ \n|\n|\n|""")
    elif chance == 1:
        print("""|_______\n|  |\n|  0\n| /|\\ \n| /\n|\n|""")
    elif chance == 0:                                                                                                                                                                                                                                                                       
        print("""|_______\n|  |\n|  0\n| /|\\ \n| / \\\n|\n|""")


def masking_word():# function for masking and unmasking word.
    chance=7    
    word = get_word()       #Getting the word.
    masked_word = ""
    for letter in range(0,len(word)):       
        masked_word = masked_word + '-'  #masking the word
    print(masked_word,len(masked_word), 'Letter word')
    guessed_letter_list=[]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    while(chance>0):       #Loop 
        guessed_letter = input('enter a letter:')  #input from the user.
        if guessed_letter not in guessed_letter_list: #Checking whether the guessed letter already enter.
            guessed_letter_list.append(guessed_letter) #Creating list of letters entered by the user.
            print('Your previous choices :-',guessed_letter_list)
            if guessed_letter in word: #Checking the user input inside the word.
                for letter in range(0,len(word)):
                    if word[letter] == guessed_letter:   
                        masked_word = masked_word[:letter] + guessed_letter + masked_word[letter+1:] #unmasking the word.
            else:
                chance -= 1
                image(chance) #Calling image function.
                print("You've missed an opportunity.")
                print("chances left--",chance)
            if masked_word == word : #Validating word and the output.    
                print("You've guessed correctly: 'Congratulations on completing the game!'")
                exit()
            if chance == 0: #Check if the user has run out of chances.
                print("You've exhausted your chances,You were eliminated from the game .The word is-",word)
                exit()
            print(masked_word)
        else:
            print('You made this choice earlier.')


if __name__ == "__main__":
    start()