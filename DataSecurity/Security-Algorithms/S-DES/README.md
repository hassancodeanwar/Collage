# Simplified DES (S-DES) Algorithm Documentation

## Overview

**Simplified Data Encryption Standard (S-DES)** is a simplified version of the Data Encryption Standard (DES) designed for educational purposes. It operates on 8-bit blocks of plaintext and uses a 10-bit key to generate two 8-bit subkeys for encryption and decryption. S-DES maintains the fundamental principles of DES but with reduced complexity, making it an excellent tool for understanding symmetric key cryptography.

## Key Components

### Key Generation

1. **Input Key**: A 10-bit key is provided as input.
2. **P10 Permutation**: The key undergoes a permutation based on the P10 table.
3. **Left Shifts**: The permuted key is split into two halves, which are then subjected to circular left shifts.
4. **Subkey Generation**: Two subkeys (K1 and K2) are generated from the shifted halves using the P8 permutation.

### Permutations and Functions

S-DES employs several permutations and functions during encryption and decryption:

- **Initial Permutation (IP)**: Rearranges the bits of the input plaintext.
- **Expansion/Permutation (EP)**: Expands the right half of the data block before applying the subkey.
- **S-Boxes (S0 and S1)**: Perform substitution based on input bits, providing non-linear transformation.
- **P4 Permutation**: Rearranges the output from the S-Boxes before XORing with the left half of the data.
- **Switch Function (SW)**: Swaps the left and right halves of the data block after the first round of processing.

### Encryption Process

The encryption process consists of several steps:

1. **Initial Permutation (IP)**: Apply IP to the plaintext.
2. **First Round with K1**: Use K1 in the function fK, which includes EP, S-Box substitutions, P4 permutation, and XOR with the left half.
3. **Swap Halves**: Swap the left and right halves of the result.
4. **Second Round with K2**: Use K2 in fK on the swapped output.
5. **Final Permutation (IP⁻¹)**: Apply inverse initial permutation to produce ciphertext.

### Decryption Process

Decryption follows a similar structure but uses K2 first and then K1:

1. **Initial Permutation (IP)**: Apply IP to the ciphertext.
2. **First Round with K2**: Use K2 in fK.
3. **Swap Halves**: Swap the halves.
4. **Second Round with K1**: Use K1 in fK on the swapped output.
5. **Final Permutation (IP⁻¹)**: Apply inverse initial permutation to retrieve plaintext.

## Implementation

The provided Python code implements S-DES as follows:

```python
class SDES:
    def __init__(self):
        # Key
        self.key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]
        
        # Permutation Tables
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        
        # Block Permutation Tables
        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]
        self.IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
        self.EP = [4, 1, 2, 3, 2, 3, 4, 1]
        self.P4 = [2, 4, 3, 1]
        
        # S-Boxes
        self.S0 = [
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 2]
        ]
        self.S1 = [
            [0, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3]
        ]
        
        # Generated keys will be stored here
        self.key1 = [0] * 8
        self.key2 = [0] * 8

    def shift(self):
        """Circular left shift"""
        return ar[n:] + ar[:n]

    def key_generation(self):
        """Generate subkeys K1 and K2"""
        # Apply P10 permutation
        key_ = [self.key[self.P10[i] - 1] for i in range(10)]
        
        # Split into left and right halves
        Ls = key_[:5]
        Rs = key_[5:]
        
        # Generate first subkey (K1)
        Ls_1 = self.shift(Ls)
        Rs_1 = self.shift(Rs)
        key_ = Ls_1 + Rs_1
        self.key1 = [key_[self.P8[i] - 1] for i in range(8)]
        
        # Generate second subkey (K2)
        Ls_2 = self.shift(Ls)
        Rs_2 = self.shift(Rs)
        key_ = Ls_2 + Rs_2
        self.key2 = [key_[self.P8[i] - 1] for i in range(8)]
        
    def binary_(self):
       """Convert decimal to binary string"""
       return f"{val:02b}"

    def function_(self):
       """Core encryption/decryption function"""
       # Split into left and right halves
       l = ar[:4]
       r = ar[4:]
       
       # Expansion Permutation
       ep = [r[self.EP[i] - i] for i in range(8)]
       
       # XOR with key
       xor_result = [key_[i] ^ ep[i] for i in range(8)]
       
       # Split XOR result
       l_1 = xor_result[:4]
       r_1 = xor_result[4:]
       
       # S-Box substitution
       row_l = int(f"{l_1[0]}{l_1[3]}", base=2)
       col_l = int(f"{l_1[1]}{l_1[2]}", base=2)
       val_l = self.S0[row_l][col_l]
       str_l = self.binary_(val_l)
       
       row_r = int(f"{r_1[0]}{r_1[3]}", base=2)
       col_r = int(f"{r_1[1]}{r_1[2]}", base=2)
       val_r = self.S1[row_r][col_r]
       str_r = self.binary_(val_r)
       
       # Combine S-Box outputs
       r_ = [int(str_l[0]), int(str_l[1]), 
             int(str_r[0]), int(str_r[1])]
       
       # P4 Permutation
       r_p4 = [r_[self.P4[i] - i] for i in range(4)]
       
       # XOR with left half
       l = [l[i] ^ r_p4[i] for i in range(4)]
       
       return l + r

    def swap(self):
      """Swap left and right halves"""
      n=len(array)//2
      return array[n:] + array[:n]

    def encryption(self):
      """Encrypt an block"""
      arr=[plaintext[self.IP[i]-i] for i in range(8)]
      
      arr=self.function_(arr,self.key)

      after_swap=self.swap(arr)

      arr=self.function_(after_swap,self.key)

      ciphertext=[arr[self.IP_inv[i]-i] for i in range(8)]

      return ciphertext

    def decryption(self):
      """Decrypt an block"""
      arr=[ciphertext[self.IP[i]-i] for i in range(8)]

      arr=self.function_(arr,self.key)

      after_swap=self.swap(arr)

      arr=self.function_(after_swap,self.key)

      decrypted=[arr[self.IP_inv[i]-i] for i in range(8)]

      return decrypted

def main():
    sdes=SDES()
    
    sdes.key_generation()
    
    plaintext=[int(x) for x in input("Enter an binary message (8 bits): ")]
    
    print("\nPlain Text:", ' '.join(map(str , plaintext)))
    
    ciphertext=sdes.encryption(plaintext)
    print("Cipher Text:", ' '.join(map(str , ciphertext)))
    
    decrypted=sdes.decryption(ciphertext)
    print("Decrypted Text:", ' '.join(map(str , decrypted)))
    
    print("Decryption Successful:", plaintext == decrypted)

if __name__ == "__main__":
    main()
```

### Functions Explained

- **`__init__()`**: Initializes key parameters and permutation tables used throughout S-DES operations.
  
- **`shift(ar,n)`**: Performs a circular left shift on an array `ar` by `n` positions.

- **`key_generation()`**: Generates two subkeys (K1 and K2) from the original key through permutations and shifts.

- **`binary_(val)`**: Converts a decimal value to a binary string formatted as a two-bit representation.

- **`function_(ar,key_)`**: Implements the core encryption/decryption function using permutations and S-Boxes.

- **`swap(array)`**: Swaps the left and right halves of an array.

- **`encryption(plaintext)`**: Encrypts an input plaintext block using S-DES algorithm steps.

- **`decryption(ciphertext)`**: Decrypts an input ciphertext block using reverse S-DES algorithm steps.

### Example Usage

```python
def main():
    sdes = SDES()
    
    sdes.key_generation()
    
    plaintext = [int(x) for x in input("Enter a binary message (8 bits): ")]
    
    print("\nPlain Text:", ' '.join(map(str , plaintext)))
    
    ciphertext = sdes.encryption(plaintext)
    print("Cipher Text:", ' '.join(map(str , ciphertext)))
    
    decrypted = sdes.decryption(ciphertext)
    print("Decrypted Text:", ' '.join(map(str , decrypted)))
    
    print("Decryption Successful:", plaintext == decrypted)

if __name__ == "__main__":
    main()
```

## Complexity Analysis

The time complexity of both encryption and decryption processes is $$O(N)$$, where $$N$$ is fixed at $$8$$ bits due to constant input size.

## Advantages and Disadvantages

### Advantages
- **Educational Tool**: Provides insight into how symmetric key algorithms function without overwhelming complexity.
- **Simple Structure**: Easy to understand due to its limited size compared to full DES.

### Disadvantages
- **Limited Security**: Not suitable for real-world applications; easily broken with modern techniques.
- **Small Key Size**: The small key size makes it vulnerable to brute-force attacks.

## Conclusion

Simplified DES serves as a fundamental learning tool that illustrates core concepts of symmetric encryption algorithms. While it lacks robustness against modern cryptographic attacks due to its simplicity and small parameter sizes compared to its full counterpart DES or AES algorithms today.

Citations:
[1] https://myethiolectures.files.wordpress.com/2015/06/simplified-des.pdf
[2] https://www.uomustansiriyah.edu.iq/media/lectures/6/6_2022_05_15!02_16_49_PM.pdf
[3] https://opencourses.emu.edu.tr/pluginfile.php/47494/mod_resource/content/3/Block%20ciphers%20(Simplified%20DES).pdf
[4] https://www.geeksforgeeks.org/simplified-data-encryption-standard-set-2/
