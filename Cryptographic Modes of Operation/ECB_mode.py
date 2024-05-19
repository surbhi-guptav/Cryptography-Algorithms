from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import time

def encrypt(plain_text, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()
    cipher_text = encryptor.update(plain_text) + encryptor.finalize()
    return cipher_text

def decrypt(cipher_text, key):
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()
    plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    return plain_text

def main():
    key = b'\x80\xf6\x93@\xb1\xd0\xa6\xd1\xe1\xef}\xed\x95g#'

    start_time = time.time()

    plain_text = "Hello, ECB encryption!"
    plain_text_bytes = plain_text.encode('utf-8')
    
    encrypted_text = encrypt(plain_text_bytes, key)
    encrypted_text_base64 = base64.b64encode(encrypted_text).decode('utf-8')
    print("Encrypted Text: " + encrypted_text_base64)

    decrypted_text_bytes = decrypt(base64.b64decode(encrypted_text_base64), key)
    decrypted_text = decrypted_text_bytes.decode('utf-8')
    print("Decrypted Text: " + decrypted_text)

    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    print("Execution Time: {:.2f} milliseconds".format(execution_time))

if __name__ == "__main__":
    main()
