'''
Includes some methods used to help better visualize stuff in the CLI.
'''
import os


def cmd_clear():
    '''
    Clears the console.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def cmd_pause():
    '''
    Pauses the console.
    '''
    input('Press ENTER to continue...')
