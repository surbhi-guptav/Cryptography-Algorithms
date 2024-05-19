# Initial permutation for the datas
PI = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

# Initial permutation for the key
CP_1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63,
        55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6,
        61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]

# Permutation applied on shifted key to get Ki+1
CP_2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

# Expand matrix to get a 48-bit matrix of data to apply the XOR with Ki
E = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

# S-Box
S_BOX = [
         
[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
 [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
],

[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
],

[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
],

[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
],  

[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
], 

[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
], 

[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
],
   
[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
]

# Permutation made after each S-Box substitution for each round
P = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

# Final permutation for data after the 16 rounds
PI_1 = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

# Matrix that determines the shift for each round of keys
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

ENCRYPT = 1
DECRYPT = 0


class TripleDES:
    def __init(self):
        self.keys1 = list()
        self.keys2 = list()
        self.keys3 = list()
        self.text = None

    def run(self, key1, key2, key3, text, action=ENCRYPT, padding=False):
        if len(key1) < 8 or len(key2) < 8 or len(key3) < 8:
            raise ValueError("Keys should be 8 bytes long")
        elif len(key1) > 8 or len(key2) > 8 or len(key3) > 8:
            key1 = key1[:8]
            key2 = key2[:8]
            key3 = key3[:8]

        self.keys1 = self.generate_keys(key1)
        self.keys2 = self.generate_keys(key2)
        self.keys3 = self.generate_keys(key3)

        self.text = text

        if padding and action == ENCRYPT:
            self.add_padding()
        elif len(self.text) % 8 != 0:
            raise ValueError("Data size should be multiple of 8")

        text_blocks = self.nsplit(self.text, 8)
        result = list()

        for block in text_blocks:
            block = self.string_to_bit_array(block)
            block = self.permut(block, PI)
            g, d = self.nsplit(block, 32)
            tmp = None
            for i in range(16):
                d_e = self.expand(d, E)
                if action == ENCRYPT:
                    tmp = self.xor(self.keys1[i], d_e)
                else:
                    tmp = self.xor(self.keys1[15 - i], d_e)
                tmp = self.substitute(tmp)
                tmp = self.permut(tmp, P)
                tmp = self.xor(g, tmp)
                g = d
                d = tmp
            result += self.permut(d + g, PI_1)
        final_res = self.bit_array_to_string(result)
        if padding and action == DECRYPT:
            return self.remove_padding(final_res)
        else:
            return final_res

    def substitute(self, d_e):
        subblocks = self.nsplit(d_e, 6)
        result = list()
        for i in range(len(subblocks)):
            block = subblocks[i]
            row = int(str(block[0]) + str(block[5]), 2)
            column = int(''.join([str(block[j]) for j in range(1, 5)]), 2)
            val = S_BOX[i][row][column]
            bin = self.int_to_bit_array(val, 4)
            result += bin
        return result

    def permut(self, block, table):
        return [block[x - 1] for x in table]

    def expand(self, block, table):
        return [block[x - 1] for x in table]

    def xor(self, t1, t2):
        return [x ^ y for x, y in zip(t1, t2)]

    def generate_keys(self, key):
        keys = [self.string_to_bit_array(key)]
        keys[0] = self.permut(keys[0], CP_1)
        g, d = self.nsplit(keys[0], 28)
        for i in range(16):
            g, d = self.shift(g, d, SHIFT[i])
            tmp = g + d
            keys.append(self.permut(tmp, CP_2))
        return keys

    def shift(self, g, d, n):
        return g[n:] + g[:n], d[n:] + d[:n]

    def add_padding(self):
        pad_len = 8 - (len(self.text) % 8)
        self.text += pad_len * chr(pad_len)

    def remove_padding(self, data):
        pad_len = ord(data[-1])
        return data[:-pad_len]

    def bit_array_to_string(self, array):
        result = list()
        for i in range(len(array) // 8):
            byte = array[i * 8:(i + 1) * 8]
            result.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
        return ''.join(result)

    def string_to_bit_array(self, string):
        array = list()
        for char in string:
            binval = binvalue(char, 8)
            array.extend([int(x) for x in list(binval)])
        return array

    def nsplit(self, s, n):
        return [s[k:k + n] for k in range(0, len(s), n)]

    def int_to_bit_array(self, val, bitsize):
        binval = binvalue(val, bitsize)
        return [int(x) for x in list(binval)]


def binvalue(val, bitsize):
    binval = bin(val)[2:] if isinstance(val, int) else bin(ord(val))[2:]
    if len(binval) > bitsize:
        raise ValueError("Value in bit size")
    while len(binval) < bitsize:
        binval = "0" + binval
    return binval


# Example usage:
if __name__ == '__main__':
    key1 = "secret_k"
    key2 = "second_k"
    key3 = "third_ke"
    text = "ThisistheTripleDESimplementation"
    
    des = TripleDES()
    encrypted_text = des.run(key1, key2, key3, text, action=ENCRYPT)
    decrypted_text = des.run(key1, key2, key3, encrypted_text, action=DECRYPT)

    print("Original text:", text)
    print("Encrypted text:", encrypted_text)       # this is in binary form
    print("Decrypted text:", decrypted_text)

# convert the encrypted binary to ASCII value or Alphabetic value 

def binary_to_text(binary_string):
    # Convert binary string to integer
    int_value = int(binary_string, 2)
    # Convert integer to ASCII character
    ascii_char = chr(int_value)
    return ascii_char

# Encrypted binary text obtained from the previous steps
encrypted_binary_text = "01001000011001010110110001101100011011110010000001101001011011110111010100100000011100110111010001110000011001010111001000100000011011010110100101100011011101000110111101110010011010010110111001110100"

# Split the binary string into 8-bit chunks
binary_chunks = [encrypted_binary_text[i:i + 8] for i in range(0, len(encrypted_binary_text), 8)]

# Convert each 8-bit chunk to ASCII character
encrypted_text = ''.join([binary_to_text(chunk) for chunk in binary_chunks])

print("Encrypted text in alphabetic format:", encrypted_text)
