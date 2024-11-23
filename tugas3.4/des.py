# Initial Permutation Table (IP)
# This table tells us how to rearrange the bits at the start of encryption. 
# It takes the original input and scrambles the bits in a specific way.

IP = [58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table (FP)
# This is like IP, but it's applied at the end of the encryption process. 
# It unscrambles the bits to finish the encryption.
FP = [40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25]

# Expansion Table (E)
# This takes a smaller chunk of data (32 bits) and expands it into 48 bits. 
# It does this by repeating some of the bits in a specific order.
E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# S-Boxes (Substitution Boxes)
# These are used to scramble small chunks of data in a tricky way. 
# Each S-Box is like a little lookup table that changes 6 bits of input into 4 bits of output.
# S2, S3, ..., S8 are similar but with different numbers
S_BOX = [
    # S1
    [[ 14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

    # S2
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

    # S3
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    # S4
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    # S5
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    # S6
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    # S7
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    # S8
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]

# Permutation Table (P)
# This table rearranges the bits again after they have been scrambled by the S-Boxes.
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

# Permuted Choice 1 Table (PC1)
# This table picks out bits from the key and rearranges them in a new way to start creating the subkeys.
PC1 = [57, 49, 41, 33, 25, 17, 9,
     1, 58, 50, 42, 34, 26, 18,
     10, 2, 59, 51, 43, 35, 27,
     19, 11, 3, 60, 52, 44, 36,
     63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
     14, 6, 61, 53, 45, 37, 29,
     21, 13, 5, 28, 20, 12, 4]

# Permuted Choice 2 Table (PC2)
# After some shifts, this table is used to pick and rearrange bits from the key to form the final subkeys.
PC2 = [14, 17, 11, 24, 1, 5,
     3, 28, 15, 6, 21, 10,
     23, 19, 12, 4, 26, 8,
     16, 7, 27, 20, 13, 2,
     41, 52, 31, 37, 47, 55,
     30, 40, 51, 45, 33, 48,
     44, 49, 39, 56, 34, 53,
     46, 42, 50, 36, 29, 32]

# Number of bit shifts (SHIFT)
# This array tells how many times to shift the key bits to the left during subkey generation.
SHIFT = [1, 1, 2, 2, 2, 2, 2, 2,
       1, 2, 2, 2, 2, 2, 2, 1]

# Permutes the input block according to the given table
# This function takes a block of bits and rearranges them according to a table like IP or FP.
def permute(block, table):
    return [block[x - 1] for x in table]

# Performs bitwise XOR between two lists of bits
# XOR is a bitwise operation that compares bits. If the bits are the same, the result is 0; if different, the result is 1.
def xor(t1, t2):
    return [x ^ y for x, y in zip(t1, t2)]

# Shifts the bits in the block to the left by n positions
# This shifts the bits in the key left by a certain number of positions.
def shift_left(block, n):
    return block[n:] + block[:n]

# Substitutes the input block using the S-Boxes
# This function takes the input, breaks it into 6-bit chunks, uses the S-Boxes to scramble each chunk, and combines the results.
def sbox_substitution(block):
    sub_blocks = [block[i:i + 6] for i in range(0, len(block), 6)]
    result = []
    for i, block in enumerate(sub_blocks):
        row = int(f"{block[0]}{block[5]}", 2)  # First and last bits form the row
        col = int("".join([str(x) for x in block[1:5]]), 2)  # Middle four bits form the column
        val = S_BOX[i][row][col]  # Lookup in the S-Box
        bin_val = bin(val)[2:].zfill(4)  # Convert to 4-bit binary
        result += [int(x) for x in bin_val]  # Append to result
    return result

# The F function used in the Feistel structure
# This function takes the right half of the data and one key, scrambles the data, and returns the result.
def f_function(r, k):
    r = permute(r, E)  # Expand R using the E table
    r = xor(r, k)  # XOR with the key
    r = sbox_substitution(r)  # Substitute using S-Boxes
    r = permute(r, P)  # Permute using the P table
    return r

# Generates 16 subkeys from the main key
def generate_keys(key):
    key = permute(key, PC1)  # Initial permutation using PC1
    c, d = key[:28], key[28:]  # Split into two halves
    keys = []
    for shift in SHIFT:  # For each shift value
        c, d = shift_left(c, shift), shift_left(d, shift)  # Shift both halves
        keys.append(permute(c + d, PC2))  # Permute using PC2 and store the subkey
    return keys

# Encrypts a block of plaintext using the generated keys
def des_encrypt(block, keys):
    block = permute(block, IP)  # Initial permutation using IP
    l, r = block[:32], block[32:]  # Split into two halves
    for key in keys:  # For each subkey
        l, r = r, xor(l, f_function(r, key))  # Apply the Feistel function and swap
    block = permute(r + l, FP)  # Final permutation using FP
    return block

# Decrypts a block of ciphertext using the generated keys
def des_decrypt(block, keys):
    block = permute(block, IP)  # Initial permutation using IP
    l, r = block[:32], block[32:]  # Split into two halves
    for key in reversed(keys):  # For each subkey in reverse order
        l, r = r, xor(l, f_function(r, key))  # Apply the Feistel function and swap
    block = permute(r + l, FP)  # Final permutation using FP
    return block

# Converts a string to a list of bits
def str_to_bit_array(text):
    array = list()
    for char in text:
        binval = bin(ord(char))[2:].zfill(8)  # Convert each character to 8-bit binary
        array.extend([int(x) for x in binval])  # Append to the array
    return array

# Converts a list of bits to a string
def bit_array_to_str(array):
    res = ''.join([chr(int(''.join([str(x) for x in _bytes]), 2)) for _bytes in nsplit(array, 8)])  # Convert each 8 bits to a character
    return res

# Splits a list into sublists of length n
def nsplit(s, n):
    return [s[k:k + n] for k in range(0, len(s), n)]

# Pads the plaintext to make its length a multiple of 8
def pad(text):
    pad_len = 8 - (len(text) % 8)
    return text + chr(pad_len) * pad_len

# Removes the padding from the plaintext
def unpad(text):
    pad_len = ord(text[-1])
    return text[:-pad_len]

# Encrypts the plaintext using the DES algorithm
def encrypt(plaintext, key):
    plaintext = pad(plaintext)  # Pad the plaintext
    key = str_to_bit_array(key)  # Convert the key to a bit array
    keys = generate_keys(key)  # Generate the subkeys
    plaintext_blocks = nsplit(str_to_bit_array(plaintext), 64)  # Split the plaintext into 64-bit blocks
    ciphertext = []
    for block in plaintext_blocks:
        ciphertext += des_encrypt(block, keys)  # Encrypt each block
    return bit_array_to_str(ciphertext)  # Convert the ciphertext to a string

# Decrypts the ciphertext using the DES algorithm
def decrypt(ciphertext, key):
    key = str_to_bit_array(key)  # Convert the key to a bit array
    keys = generate_keys(key)  # Generate the subkeys
    ciphertext_blocks = nsplit(str_to_bit_array(ciphertext), 64)  # Split the ciphertext into 64-bit blocks
    plaintext = []
    for block in ciphertext_blocks:
        plaintext += des_decrypt(block, keys)  # Decrypt each block
    return unpad(bit_array_to_str(plaintext))  # Convert the plaintext to a string and unpad it
