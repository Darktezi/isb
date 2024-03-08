import logging
from writer_and_reader import read_from_file, write_to_file


rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def caesar_encrypt(text: str, shift: int) -> str:
    """
    This function takes a text and a shift value as input 
    and performs Caesar encryption on the text.
    """
    encrypted_text = ''
    for char in text:
        if char in rus_alphabet:
            position = rus_alphabet.index(char)
            new_position = (position + shift) % len(rus_alphabet)
            encrypted_text += rus_alphabet[new_position]
        else:
            encrypted_text += char
    return encrypted_text

if __name__ == "__main__":
    text = read_from_file("lab_1/task1/text.txt")
    write_to_file("lab_1/task1/encrypted_text.txt",caesar_encrypt(text, 5))
