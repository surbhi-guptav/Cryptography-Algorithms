def text_to_binary(text):
    # Convert text to binary
    binary_string = ''.join(format(ord(char), '08b') for char in text)
    
    # If the binary string is not 32 bits long, pad with zeros
    if len(binary_string) < 32:
        binary_string = binary_string.zfill(32)
    # If the binary string is longer than 32 bits, truncate to 32 bits
    elif len(binary_string) > 32:
        binary_string = binary_string[:32]
    
    return binary_string

def mangler(input_bits):
    # Ensure input_bits is 32 bits long
    input_bits = input_bits.zfill(32)
    
    # Divide input into 8 4-bit chunks
    chunks = [input_bits[i:i+4] for i in range(0, 32, 4)]
    
    # Initialize the output bits
    output_bits = ""
    
    # Process the chunks and concatenate left and right bits
    for i in range(8):
        # For the first 4-bit chunk, concatenate a 0 to the left
        left_bit = '0' if i == 0 else chunks[i-1][0]
        # For the last 4-bit chunk, concatenate a 0 to the right
        right_bit = '0' if i == 7 else chunks[i+1][1]
        
        # Concatenate left and right bits from adjacent chunks
        output_bits += left_bit + chunks[i] + right_bit
    
    # Output 48 bits
    return output_bits

def reverse_mangler(output_bits):
    # Divide the output into 8 6-bit chunks
    chunks = [output_bits[i:i+6] for i in range(0, 48, 6)]
    
    # Initialize the input bits
    input_bits = ""
    
    # Process the chunks and retrieve original 32 bits
    for i in range(8):
        # Remove the left and right bits added by Mangler
        original_chunk = chunks[i][1:5]
        input_bits += original_chunk
    
    return input_bits

# Take text input
text_input = input("Enter text: ")

# Convert text to binary with padding
binary_output = text_to_binary(text_input)

# Apply Mangler function to the binary input
mangled_output = mangler(binary_output)
print("Binary representation after Mangler function (48 bits):", mangled_output)

# Reverse the Mangler function to retrieve original binary input
reversed_input = reverse_mangler(mangled_output)
print("Original binary input after reversing Mangler function (32 bits):", reversed_input)
