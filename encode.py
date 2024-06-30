import random
import string

def generate_random_word(length):
    # Generates a random word of the given length
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def encryption(cin):
    listt = []
    for i in cin:
        listt.append(ord(i) + 12)
    
    encoder = ""
    for val in listt:
        encoder += chr(val)
        # Insert a random word of length 3 between each character
        encoder += generate_random_word(3)
    
    return str(encoder)
