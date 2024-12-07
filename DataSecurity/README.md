# Understanding the Simplified DES (SDES) Encryption Algorithm

## Introduction to Symmetric Encryption

Symmetric encryption is a fundamental cryptographic technique where the same key is used for both encryption and decryption. The Simplified Data Encryption Standard (SDES) is a simplified version of the Data Encryption Standard (DES), designed to teach the core principles of block cipher encryption.

## Key Characteristics of SDES

- **Block Size**: 8 bits
- **Key Size**: 10 bits
- **Number of Rounds**: 2
- **Purpose**: Educational tool to demonstrate encryption principles

## Key Generation Process

The key generation is a critical first step in the SDES algorithm:

1. **Initial Key Permutation (P10)**
   - Takes the 10-bit master key
   - Rearranges bits according to a predefined permutation table
   - Example: [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]

2. **Key Division**
   - Splits the permuted key into two 5-bit halves
   - Left half (Ls) and Right half (Rs)

3. **Circular Left Shift**
   - Performs a circular left shift on both halves
   - First round: 1-bit shift
   - Second round: 2-bit shift

4. **Key Compression (P8)**
   - Compresses the shifted key to 8 bits
   - Creates two subkeys (K1 and K2)

## Encryption Process

The encryption follows a systematic approach:

### 1. Initial Permutation (IP)
- Rearranges the 8-bit input block
- Uses a specific permutation table
- Helps distribute bits across the block

### 2. Feistel Function (F-function)
A complex transformation involving multiple steps:

a) **Expansion Permutation**
   - Expands the 4-bit right half to 8 bits
   - Uses an expansion permutation table
   - Increases the bit spread

b) **Key Mixing (XOR)**
   - XORs the expanded block with the current round key
   - Introduces key-dependent confusion

c) **S-Box Substitution**
   - Splits the XORed block into two 4-bit halves
   - Uses two predefined S-Boxes (S0 and S1)
   - Performs non-linear substitution
   - Converts 4-bit input to 2-bit output based on row and column lookup

d) **Permutation (P4)**
   - Rearranges the 4 bits from S-Boxes
   - Further distributes bit positions

e) **XOR with Left Half**
   - XORs the transformed right half with the original left half

### 3. Swap Operation
- Swaps left and right halves after the first round
- Creates additional complexity

### 4. Second Round
- Repeats the process with the second subkey (K2)

### 5. Final Permutation (Inverse IP)
- Performs a final bit rearrangement
- Completes the encryption process

## Decryption Process

Decryption is the exact reverse of encryption:
1. Use the same steps
2. Apply keys in reverse order (K2 first, then K1)
3. Ensures perfect reconstruction of the original plaintext

## Example Walkthrough

```python
# Master Key: [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
# Plaintext:  [1, 0, 0, 1, 0, 1, 1, 1]

# 1. Key Generation
# Generates K1 and K2 using permutations and shifts

# 2. Encryption Steps
# - Initial Permutation
# - First round with K1
# - Swap
# - Second round with K2
# - Final Permutation

# Result is the encrypted ciphertext
```

## Strengths and Limitations

### Strengths
- Illustrates encryption principles
- Simple to understand
- Demonstrates key concepts of block ciphers

### Limitations
- Very small key and block size
- Weak against modern cryptanalysis
- Not suitable for real-world security

## Mathematical Foundations

SDES demonstrates key cryptographic principles:
- Confusion: Obscuring relationship between key and ciphertext
- Diffusion: Spreading input bits across the output
- Non-linearity: Using S-Boxes to introduce complex transformations

## Educational Significance

SDES serves as a perfect educational tool to understand:
- Symmetric encryption mechanics
- Key generation processes
- Block cipher design
- Bit manipulation techniques

## Conclusion

While Simplified DES is not a practical encryption method, it provides an invaluable learning experience in understanding the fundamental mechanisms of symmetric encryption algorithms.
