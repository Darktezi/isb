from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

class RSACipher:
    """Class for asymmetric cryptography operations."""
    def generate_key_pair(self, key_size: int) -> tuple:
        """
        Generate an RSA key pair.
        """
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=key_size)
        public_key = private_key.public_key()
        return private_key, public_key
    

    def encrypt_with_public_key(self, text: bytes, public_key: rsa.RSAPublicKey) -> bytes:
        """
        Encrypts text using public key.
        """
        return public_key.encrypt(text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(), 
                                                    label=None))


    def decrypt_with_private_key(self, crypted_text: bytes, private_key: rsa.RSAPrivateKey) -> bytes:
        """
        Decrypts crypted text using private key.
        """
        return private_key.decrypt(crypted_text, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                            algorithm=hashes.SHA256(), 
                                                            label=None))