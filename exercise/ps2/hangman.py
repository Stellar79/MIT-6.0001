# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "D:/Works/course/6.0001/MIT-6.0001/exercise/ps2/words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the scize of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed_string=''.join(letters_guessed)
    return letters_guessed_string==secret_word
    
# secret_word='apple'
# letters_guessed=['e','i','k','p','r','s']
# print(is_word_guessed(secret_word,letters_guessed))



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = []
    letters_guessed_string=''.join(letters_guessed)
    for char in secret_word:
        if char in letters_guessed_string:
            result.append(char)
        else:
            result.append('_ ')
    return result
# secret_word='apple'
# letters_guessed=['e','i','k','p','r','s']
# print(get_guessed_word(secret_word,letters_guessed))
    

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    available_letters= string.ascii_lowercase
    for char in letters_guessed:
        if char in available_letters:
            # s = s.replace('M','')
            available_letters = available_letters.replace(char,'')
    return available_letters
# letters_guessed=['e','i','k','p','r','s']
# print(get_available_letters(letters_guessed))


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    length = len(secret_word)
    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {length} letters long.")
    print(f"You have {warnings_remaining} warnings left:")
    print("------------- ")
    letters_guessed = []
    guessed_word = []
    
    while (1):
      if (guesses_remaining <=0):
        print("Sorry, you ran out of guesses. The word was else.")
        break
      available_letters = get_available_letters(letters_guessed)
      print(f"You have {guesses_remaining} guesses left.")
      print(f"Available letters: {available_letters} ")

      # deal with input
      guessed_letter = input("Please guess a letter: ")
      if (not str.isalpha(guessed_letter)):
        if (warnings_remaining == 0):
          guesses_remaining -= 1
        else:
          warnings_remaining -= 1
        print (f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:  {''.join(guessed_word)} ")
        print('------------')
        continue
      elif (guessed_letter in letters_guessed):
        if (warnings_remaining == 0):
            guesses_remaining -= 1
        else:
            warnings_remaining -= 1
        print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: {''.join(guessed_word)}")
        print('------------')
        continue
      else:
        guessed_letter = str.lower(guessed_letter)
      
      #
      letters_guessed.append(guessed_letter)
      guessed_word = get_guessed_word(secret_word, letters_guessed)
      if guessed_letter in secret_word:
          print(f"Good guess: {''.join(guessed_word)}")
      else:
          if (guessed_letter in "aeiou"):
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
          print(f"Oops! That letter is not in my word: {''.join(guessed_word)}")
      print('------------')
      
      # weather users won
      if (is_word_guessed(secret_word,guessed_word)):
        total_score = guesses_remaining-1 * length
        print("Congratulations, you won! ")
        print(f"Your total score for this game is: {total_score}")
        break

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------
# message = 'a_ _ le'

# # remove leading and trailing whitespaces
# print('Message:', message.replace("_ ", "_"))
def match_with_gaps(my_word, other_word):
    
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    
    my_word = my_word.replace("_ ", "_")
    if (len(my_word) != len(other_word)):
       return False
    else:
       for i in range(len(other_word)):
          if (my_word[i] == '_'): 
             if (other_word[i] in my_word):
              return False
          elif (my_word[i] != other_word[i]):
             return False
    return True
# print(match_with_gaps("te_ t", "tact"))




def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    matches = []
    for other_word in wordlist:
       if match_with_gaps (my_word, other_word):
          matches.append(other_word)
    if not matches:
       print ("No matches found")
    else:
      return matches
print(show_possible_matches('a_ pl_ '))

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    length = len(secret_word)
    print('Welcome to the game Hangman!')
    print(f"I am thinking of a word that is {length} letters long.")
    print(f"You have {warnings_remaining} warnings left:")
    print("------------- ")
    letters_guessed = []
    guessed_word = []
    
    while (1):
      if (guesses_remaining <=0):
        print("Sorry, you ran out of guesses. The word was else.")
        break
      available_letters = get_available_letters(letters_guessed)
      print(f"You have {guesses_remaining} guesses left.")
      print(f"Available letters: {available_letters} ")
      # deal with input
      guessed_letter = input("Please guess a letter: ")
      if ((guessed_letter == '*') and (guessed_word)):
         possible_matches = show_possible_matches(''.join(guessed_word))
         print('Possible word matches are: ')
         print(possible_matches)
         continue
      if (not str.isalpha(guessed_letter)):
        if (warnings_remaining == 0):
          guesses_remaining -= 1
        else:
          warnings_remaining -= 1
        print (f"Oops! That is not a valid letter. You have {warnings_remaining} warnings left:  {''.join(guessed_word)} ")
        print('------------')
        continue
      elif (guessed_letter in letters_guessed):
        if (warnings_remaining == 0):
            guesses_remaining -= 1
        else:
            warnings_remaining -= 1
        print(f"Oops! You've already guessed that letter. You now have {warnings_remaining} warnings: {''.join(guessed_word)}")
        print('------------')
        continue
      else:
        guessed_letter = str.lower(guessed_letter)
      
      #
      letters_guessed.append(guessed_letter)
      guessed_word = get_guessed_word(secret_word, letters_guessed)
      if guessed_letter in secret_word:
          print(f"Good guess: {''.join(guessed_word)}")
      else:
          if (guessed_letter in "aeiou"):
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
          print(f"Oops! That letter is not in my word: {''.join(guessed_word)}")
      print('------------')
      
      # weather users won
      if (is_word_guessed(secret_word,guessed_word)):
        total_score = guesses_remaining * length
        print("Congratulations, you won! ")
        print(f"Your total score for this game is: {total_score}")
        break



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     # pass

#     # To test part 2, comment out the pass line above and
#     # uncomment the following two lines.
    
#     secret_word = choose_word(wordlist)
#     hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
