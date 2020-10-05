


        

                        
from random import *

def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.
    """
    random_key = choice(list(glossary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(glossary[random_key])
    user_response = input('Did you know the definition? enter y for yes: ')
    if user_response == 'y':
        del glossary[random_key]
    elif user_response == 'n':
        print ('Ok.')
    else:
        print ('Please respond with a y or n.')

# Set up the glossary

glossary = {'word1':'definition1',
            'word2':'definition2',
            'word3':'definition3'}

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
        if not glossary:
         exit = True
    else:
        print('You need to enter either q or s.')
