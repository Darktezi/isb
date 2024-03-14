import argparse
import logging
import os

from writer_and_reader import read_from_file, write_to_file


logging.basicConfig(level=logging.INFO)


rus_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def caesar_encrypt(text: str, shift: int) -> str:
    """
    This function takes a text and a shift value as input 
    and performs Caesar encryption on the text.
    """
    try:
        encrypted_text = ''
        for char in text:
            if char in rus_alphabet:
                position = rus_alphabet.index(char)
                new_position = (position + shift) % len(rus_alphabet)
                encrypted_text += rus_alphabet[new_position]
            else:
                encrypted_text += char
        return encrypted_text
    except Exception as ex:
        logging.error(f"Can't encrypt text: {ex}\n")

def caesar_decrypt(encrypted_text: str, shift: int) -> str:
    """
    This function takes an encrypted text and a shift value as input 
    and performs Caesar decryption on the text.
    """
    try:
        decrypted_text = ''
        for char in encrypted_text:
            if char in rus_alphabet:
                position = rus_alphabet.index(char)
                new_position = (position - shift) % len(rus_alphabet)
                decrypted_text += rus_alphabet[new_position]
            else:
                decrypted_text += char
        return decrypted_text
    except Exception as ex:
        logging.error(f"Can't decrypt text: {ex}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Caesar encryption.')
    parser.add_argument('--input_file',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'input.txt'),
                        help='Input file path.')
    parser.add_argument('--shift',
                        type=int,
                        default=5,
                        help='Shift value.')
    parser.add_argument('--output_crypted',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'encrypted_text.txt'),
                        help='Output crypted file path.')
    parser.add_argument('--output_decrypted',
                        type=str,
                        default=os.path.join('isb','lab_1','task1', 'decrypted_text.txt'),
                        help='Output decrypted file path.')

    args = parser.parse_args()

    try:
        text = read_from_file(args.input_file)
        encrypted_text = read_from_file(args.output_crypted)
        write_to_file(args.output_crypted, caesar_encrypt(text, args.shift))
        write_to_file(args.output_decrypted, caesar_decrypt(encrypted_text, args.shift))
    except Exception as ex:
        logging.error(f"Can't encrypt or decrypt text: {ex}")
