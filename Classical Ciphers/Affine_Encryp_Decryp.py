def gcd(a, b):
    """
    Computes the greatest common divisor (GCD) of two numbers using the Euclidean algorithm.
    
    Args:
    - a: First number.
    - b: Second number.

    Returns:
    - The GCD of a and b.
    """
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    """
    Computes the modular inverse of a number 'a' under modulo 'm'.
    This function uses a brute force approach to find the modular inverse.

    Args:
    - a: The number to find the inverse of.
    - m: The modulo.

    Returns:
    - The modular inverse of a under modulo m, if it exists.
    - None if no modular inverse exists.
    """
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def affine_encrypt(plain_text, a, b):
    """
    Encrypts a plaintext message using the Affine cipher.

    Args:
    - plain_text: The plaintext message to encrypt.
    - a: The multiplicative key parameter.
    - b: The additive key parameter.

    Returns:
    - The encrypted ciphertext.
    """
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                y = (a * x + b) % 26
                encrypted_text += chr(y + ord('a'))
            elif char.isupper():
                x = ord(char) - ord('A')
                y = (a * x + b) % 26
                encrypted_text += chr(y + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(cipher_text, a, b):
    """
    Decrypts a ciphertext message using the Affine cipher.

    Args:
    - cipher_text: The ciphertext message to decrypt.
    - a: The multiplicative key parameter.
    - b: The additive key parameter.

    Returns:
    - The decrypted plaintext message.
    - An error message if the modular inverse of 'a' does not exist.
    """
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)
    
    if a_inv is None:
        return "Inverse of 'a' does not exist. Choose another key."
    
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                y = ord(char) - ord('a')
                x = (a_inv * (y - b)) % 26
                decrypted_text += chr(x + ord('a'))
            elif char.isupper():
                y = ord(char) - ord('A')
                x = (a_inv * (y - b)) % 26
                decrypted_text += chr(x + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def main():
    """
    Main function to run the Affine cipher encryption and decryption based on user input.
    """
    choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()
    
    if choice == 'E':
        plain_text = input("Enter the plaintext: ")
        a = int(input("Enter the 'a' key parameter (must be coprime with 26): "))
        b = int(input("Enter the 'b' key parameter: "))
        
        if gcd(a, 26) == 1:
            encrypted_text = affine_encrypt(plain_text, a, b)
            print(f"Encrypted text: {encrypted_text}")
        else:
            print("'a' and 26 must be coprime for encryption.")
    elif choice == 'D':
        cipher_text = input("Enter the ciphertext: ")
        a = int(input("Enter the 'a' key parameter: "))
        b = int(input("Enter the 'b' key parameter: "))
        
        decrypted_text = affine_decrypt(cipher_text, a, b)
        print(f"Decrypted text: {decrypted_text}")
    else:
        print("Invalid choice. Enter 'E' for encryption or 'D' for decryption.")

if __name__ == "__main__":
    main()
