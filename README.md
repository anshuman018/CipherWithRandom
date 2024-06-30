#CipherWithRandom
#Overview
CipherWithRandom is a Python-based encryption and decryption tool that enhances security by inserting random words between encrypted characters. This unique approach adds an additional layer of complexity to the encrypted text, making it more secure and difficult to decipher without the proper decryption algorithm.

Features
Random Word Insertion: Inserts random words of specified length between encrypted characters.
Simple Encryption and Decryption: Easy-to-use functions for both encryption and decryption processes.
Modular Design: Organized into separate modules for encryption and decryption, promoting clean code and ease of maintenance.
How It Works
Encryption: The tool converts each character in the input text to its ASCII value, adds a specified offset to this value, and then converts it back to a character. A random word is inserted between each encrypted character.
Decryption: The tool extracts the encrypted characters by skipping the random words, reverses the offset added during encryption, and converts the values back to the original characters.
Installation
Clone the repository to your local machine using:

bash
Copy code
git clone https://github.com/anshuman018/CipherWithRandom.git
Navigate to the repository directory:

bash
Copy code
cd CipherWithRandom
Usage
Run the main script:

bash
Copy code
python main.py
Example usage in the main script:

python
Copy code
from encode import encryption
from decode import decryption

a = str(input("Enter any text: "))

ey = encryption(a)
print(f"After encryption : {ey}")

dy = decryption(ey)
print(f"After decryption : {dy}")
Example
Encryption
python
Copy code
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
Decryption
python
Copy code
def decryption(cin):
    listt = []
    i = 0
    while i < len(cin):
        # Take every 4th character (actual encoded character)
        listt.append(ord(cin[i]) - 12)
        i += 4  # Skip the random word (3 characters) + 1 actual character
    
    decoder = ""
    for val in listt:
        decoder += chr(val)
    
    return str(decoder)
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

License
This project is licensed under the MIT License.
