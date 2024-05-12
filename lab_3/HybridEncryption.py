import logging

from Symmetric import AESCipher
from Assymetric import RSACipher
import Work_with_files


logging.basicConfig(level=logging.INFO)

class HybridCryptoSystem:
    """
    Class for hybrid encryption using both symmetric and asymmetric keys.
    """


    def generate_keys(rsa_key_size: int = 2048, rsa_private_key_path: str = "lab_3/keys/private.pem",
                      rsa_public_key_path: str = "lab_3/keys/public.pem", symmetric_key_path: str = "lab_3/keys/symmetric.key"):
        """
        Generate RSA key pair and symmetric key and save them to files.
        """
        rsa_cipher = RSACipher()
        aes_cipher = AESCipher()

        rsa_private_key, rsa_public_key = rsa_cipher.generate_key_pair(rsa_key_size)
        symmetric_key = aes_cipher.generate_key()

        Work_with_files.serialization_private_key(rsa_private_key, rsa_private_key_path)
        Work_with_files.serialization_public_key(rsa_public_key, rsa_public_key_path)
        Work_with_files.serialization_symmetric_key(symmetric_key, symmetric_key_path)


    def encrypt_text(text: str, public_key_path: str = "lab_3/keys/public.pem", symmetric_key_path: str = "lab_3/keys/symmetric.key",
                     encrypted_text_path: str = "lab_3/texts/encrypted_text.txt"):
        """
        Encrypt text using hybrid encryption and save the result to a file.
        """
        rsa_cipher = RSACipher()
        aes_cipher = AESCipher()

        rsa_public_key = Work_with_files.deserialization_public_key(public_key_path)
        symmetric_key = Work_with_files.deserialization_symmetric_key(symmetric_key_path)

        encrypted_text = aes_cipher.encrypt_text(text.encode('utf-8'), symmetric_key)

        encrypted_symmetric_key = rsa_cipher.encrypt_with_public_key(symmetric_key, rsa_public_key)

        Work_with_files.serialization_symmetric_key(encrypted_symmetric_key, symmetric_key_path)
        Work_with_files.write_data_bytes(encrypted_text, encrypted_text_path)


    def decrypt_text(symmetric_key_path: str = "lab_3/keys/symmetric.key", encrypted_text_path: str = "lab_3/texts/encrypted_text.txt",
                     decrypted_text_path: str = "lab_3/texts/decrypted_text.txt"):
        """
        Decrypt text using hybrid decryption and save the result to a file.
        """
        rsa_cipher = RSACipher()
        aes_cipher = AESCipher()

        encrypted_symmetric_key = Work_with_files.deserialization_symmetric_key(symmetric_key_path)
        encrypted_text = Work_with_files.read_data_bytes(encrypted_text_path)

        rsa_private_key = Work_with_files.deserialization_private_key("lab_3/keys/private.pem")
        symmetric_key = rsa_cipher.decrypt_with_private_key(encrypted_symmetric_key, rsa_private_key)

        decrypted_text = aes_cipher.decrypt_text(encrypted_text, symmetric_key)

        Work_with_files.write_data(decrypted_text.decode('utf-8'), decrypted_text_path)