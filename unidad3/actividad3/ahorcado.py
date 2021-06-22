from os import system
import random

GAME_START = '''
  _____ _____ _____ _____    _____ _____ _____ _____ _____ 
  |   __|  _  |     |   __|  |   __|_   _|  _  | __  |_   _|
  |  |  |     | | | |   __|  |__   | | | |     |    -| | |  
  |_____|__|__|_|_|_|_____|  |_____| |_| |__|__|__|__| |_|  
'''

IMAGES = ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

CATEGORIES = [
    ['argentina', 'colombia', 'españa', 'peru', 'canada'],
    ['pera', 'uva', 'banano', 'manzana', 'fresa'],
    ['rock','pop','metal','disco','country'],
    ['conejo','perro','gato','raton','leon'],
    []
]


def select_word(CATEGORIES):
    print(CATEGORIES)
    index = random.randint(0, len(CATEGORIES) - 1)
    return CATEGORIES[index]


def select_category(chosen_category):
    if chosen_category == 1:
        word = select_word(CATEGORIES[0])
    elif chosen_category == 2:
        word = select_word(CATEGORIES[1])
    return word

def board(tries, hidden_word):
    print(f'Intento # {tries}')
    print(f'Te quedan # {8-tries} intentos')
    print(IMAGES[tries])
    print(hidden_word)


def game(chosen_category):
    word = select_category(chosen_category)
    print(word)
    list_word = list(word)
    hiden_word = ['-'] * len(list_word)
    tries = 0
    print(GAME_START)
    while tries <= 8:
        board(tries, hiden_word)
        current_letter = str(input('Escoge una letra: '))
        for caracter in list_word:
            print(caracter)
            if caracter == current_letter:
                print('Acertaste')
                list_word.pop(caracter)
            else:
                pass


def run():
    menu_category = """
    Elija una categoría de las siguientes:
    1) Países 🌎🌏🌍
    2) Frutas 🍎🍇🍏
    3) Géneros Musicales 🎶🎵
    4) Animales 🐶🦁🐱
    5) Película 🎥🎬
    """
    print(menu_category)
    chosen_category = int(input('Por favor elija una opción: '))
    if chosen_category == 1:
        system("cls")
        print('Eligió la categoría de países 🌎🌏🌍')
        game(chosen_category)
    elif chosen_category == 2:
        system("cls")
        print('Eligió la categoría de Frutas 🍎🍇🍏')
        game(chosen_category)
    elif chosen_category == 3:
        system("cls")
        print('Eligió la categoría de Géneros Musicales 🎶🎵')
        game(chosen_category)
    elif chosen_category == 4:
        system("cls")
        print('Eligió la categoría de Animales 🐶🦁🐱')
        game(chosen_category)
    elif chosen_category == 5:
        system("cls")
        print('Eligió la categoría de Película 🎥🎬')
        game(chosen_category)
    else:
        print('Error')


if __name__ == '__main__':
    print('''
  
  .______    __   _______ .__   __. ____    ____  _______ .__   __.  __   _______   ______   
  |   _  \  |  | |   ____||  \ |  | \   \  /   / |   ____||  \ |  | |  | |       \ /  __  \  
  |  |_)  | |  | |  |__   |   \|  |  \   \/   /  |  |__   |   \|  | |  | |  .--.  |  |  |  | 
  |   _  <  |  | |   __|  |  . `  |   \      /   |   __|  |  . `  | |  | |  |  |  |  |  |  | 
  |  |_)  | |  | |  |____ |  |\   |    \    /    |  |____ |  |\   | |  | |  '--'  |  `--'  | 
  |______/  |__| |_______||__| \__|     \__/     |_______||__| \__| |__| |_______/ \______/  

          ''')
    run()
