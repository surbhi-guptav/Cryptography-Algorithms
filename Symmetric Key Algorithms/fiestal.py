# Feistel structure implementation with step-by-step output

def feistel_round(left, right, round_key):
    # Simulated Feistel round function
    new_left = right
    new_right = left ^ round_key  # Use XOR for simplicity
    return new_left, new_right

def feistel_cipher(plain_text, key, rounds):
    # Convert plain text to integer for processing
    plain_text_int = int.from_bytes(plain_text.encode(), 'big')

    left, right = divmod(plain_text_int, 2**(len(bin(plain_text_int)) // 2))  # Split the input into two halves

    print(f"Initial Left: {left}, Right: {right}")

    for round_num in range(rounds):
        round_key = key[round_num % len(key)]  # Use a round-dependent key from the key list
        left, right = feistel_round(left, right, round_key)
        print(f"Round {round_num + 1} - Left: {left}, Right: {right}, Round Key: {round_key}")

    # Swap the halves before returning the ciphertext
    cipher_text_int = (right << (len(bin(plain_text_int)) // 2)) | left
    cipher_text = cipher_text_int.to_bytes((cipher_text_int.bit_length() + 7) // 8, 'big').decode()
    return cipher_text

def main():
    plain_text = input("Enter the plain text: ")
    key = [0x01, 0x23, 0x45, 0x67]  # Example key (you can change this)
    rounds = 16 # Number of rounds (you can change this)

    cipher_text = feistel_cipher(plain_text, key, rounds)
    print("Ciphertext:", cipher_text)

if __name__ == "__main__":
    main()
# 28264, Right: 27236