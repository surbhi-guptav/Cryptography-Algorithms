import random

def generate_key(message):
    key = ""
    for char in message:
        key = key + chr(random.randint(0, 255))
    return key

'''
This function generates a random key based on the input message.
It initializes an empty string key.
It iterates through each character in the message and appends a random character with an ASCII value between 0 and 255 to the key.
The result is a random key of the same length as the input message.
This key will be used for both encryption and decryption.

'''

def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_char = chr((ord(message[i]) + ord(key[i])) % 256)
        encrypted_message = encrypted_message + encrypted_char
    return encrypted_message

'''
This function takes two arguments: message and key.
It initializes an empty string encrypted_message.
It iterates through each character of the message.
For each character, it calculates the ASCII value of the character in the message and the ASCII value of the corresponding character in the key.
It adds these ASCII values together and takes the modulo 256 to ensure that the result remains within the valid ASCII range (0-255).
It converts the result back to a character using chr and appends it to the encrypted_message.
This process is repeated for each character in the message, resulting in an encrypted message.

'''

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_char = chr((ord(encrypted_message[i]) - ord(key[i])) % 256)
        decrypted_message = decrypted_message + decrypted_char
    return decrypted_message

'''
This function is responsible for decrypting an encrypted message using the provided key.
It follows a similar process to the encrypt function but in reverse.
It iterates through each character in the encrypted_message.
For each character, it calculates the difference between the ASCII value of the character in the encrypted_message and the ASCII value of the corresponding character in the key.
It takes the modulo 256 to ensure that the result remains within the valid ASCII range (0-255).
It converts the result back to a character using chr and appends it to the decrypted_message.
This process is repeated for each character in the encrypted_message, resulting in the original message being decrypted.

'''

# Example usage
message = "thisonetimepadprogram"
key = generate_key(message)
encrypted_message = encrypt(message, key)
decrypted_message = decrypt(encrypted_message, key)

print("Original message:", message)
print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)

# when encrypted data is displayed, you might see a combination of printable and non-printable 
# characters, as shown in your encrypted message. These characters are not meant to be directly 
# readable by humans but can be decrypted back to the original message using the correct decryption key and algorithm