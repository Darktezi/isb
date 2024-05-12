import os

from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class AESCipher:
    """
    Class providing methods for symmetric cryptography operations.
    """
    
    def encrypt_text(self, text: bytes, sym_key:bytes) -> bytes:
        """"
        Encrypt text with symmetric key
        """
        iv = os.urandom(16)
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(text) + padder.finalize()
        cipher = Cipher(algorithms.AES(sym_key), modes.CBC(iv))
        encryptor = cipher.encryptor()
        crypted_text = encryptor.update(padded_data) + encryptor.finalize()
        return iv + crypted_text

    def decrypt_text(self, crypted_text: bytes, sym_key: bytes) -> bytes:
        """
        Decrypt text with symmetric key
        """
        iv = crypted_text[:16]
        crypted_text = crypted_text[16:]
        cipher = Cipher(algorithms.AES(sym_key), modes.CBC(iv))
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(crypted_text) + decryptor.finalize()
        unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
        text = unpadder.update(padded_data) + unpadder.finalize()
        return text