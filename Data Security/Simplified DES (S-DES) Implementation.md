# Simplified DES (S-DES) Implementation

This project implements a simplified version of the Data Encryption Standard (S-DES) algorithm in Python using the **NumPy** library. The program performs key generation, encryption, and decryption of 8-bit blocks, following the principles of symmetric key cryptography.

---

## Features
- **Key Generation**:
  - Generates two subkeys \( K1 \) and \( K2 \) from a 10-bit key using permutation and left circular shifts.
  
- **Encryption**:
  - Encrypts an 8-bit plaintext using \( K1 \) and \( K2 \) with the Feistel network structure.
  
- **Decryption**:
  - Decrypts an 8-bit ciphertext using the subkeys in reverse order.
  
- **Utility Functions**:
  - Modular functions for permutations, splitting arrays, circular shifts, and S-box lookups.

---

## Algorithm Overview

1. **Key Generation**:
   - A 10-bit key is permuted using \( P10 \), split into two halves, left-shifted, recombined, and reduced to 8 bits using \( P8 \) to form \( K1 \).
   - Another round of left shifts and \( P8 \) generates \( K2 \).

2. **Encryption**:
   - The plaintext is permuted with \( IP \) (Initial Permutation).
   - Two rounds of Feistel functions are applied:
     - The right half is expanded, XORed with the subkey, substituted via S-boxes, permuted with \( P4 \), and XORed with the left half.
     - The halves are swapped after the first round.
   - \( IP^{-1} \) is applied to the final block to produce the ciphertext.

3. **Decryption**:
   - Decrypts by reversing the key order in the Feistel rounds: \( K2 \) is applied first, then \( K1 \).

---

## Files in the Repository

- **`sdes.py`**:
  - The main implementation of the S-DES algorithm, including classes and functions for key generation, encryption, and decryption.
  
- **`README.md`**:
  - Documentation explaining the implementation and usage.

---

## Dependencies

This project requires **Python 3.x** and **NumPy**.

Install NumPy if not already installed:
```bash
pip install numpy
```

---

## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/sdes-implementation.git
   cd sdes-implementation
   ```

2. **Run the Script**:
   Use the provided `main()` function in the script to test the algorithm:
   ```bash
   python sdes.py
   ```

3. **Key Generation Example**:
   - Input: `0001101101`
   - Outputs:
     - \( K1 = 10100100 \)
     - \( K2 = 01000011 \)

4. **Encryption Example**:
   - Plaintext: `11010111`
   - Key: `0001101101`
   - Ciphertext: `10111101`

5. **Decryption Example**:
   - Ciphertext: `10111101`
   - Key: `0001101101`
   - Decrypted Plaintext: `11010111`

---

## Code Structure

### **Class: `SDES`**

1. **Key Tables and Constants**:
   - \( P10, P8, IP, IP^{-1}, EP, P4 \)
   - S-Boxes: \( S0 \), \( S1 \)

2. **Key Functions**:
   - `key_generation(key: str)`: Generates \( K1 \) and \( K2 \).
   - `table_shift(array, table_array)`: Applies permutation tables.

3. **Encryption/Decryption**:
   - `encrypt_block(plaintext, key)`: Encrypts an 8-bit plaintext.
   - `decrypt_block(ciphertext, key)`: Decrypts an 8-bit ciphertext.

4. **Utilities**:
   - `array_split(array)`: Splits an array into two halves.
   - `shifting_LtoR(array)`: Performs left circular shifts.
   - `sbox_lookup(input_bits, sbox)`: Substitutes bits using S-boxes.

---

## Sample Output

```plaintext
Key Generation Test:
Original Key: 0001101101
Key 1: 10100100
Key 2: 01000011

Encryption/Decryption Test:
Plaintext: 11010111
Ciphertext: 10111101
Decrypted: 11010111
Successful: True
```

---

## Debugging and Customization

1. **Debugging**:
   - Add `debug=True` in the `encrypt_block` or `decrypt_block` method to print intermediate results.

2. **Customization**:
   - Modify S-boxes, permutation tables, or key lengths for experimentation.

---

## Limitations

- **Key Size**: Limited to 10-bit keys, making it insecure for real-world applications.
- **Block Size**: Operates only on 8-bit plaintext blocks.
- **Purpose**: Educational; not suitable for practical encryption.

---

## Learning Outcomes

This implementation demonstrates:
- Fundamentals of symmetric key cryptography.
- Key scheduling and Feistel networks.
- Use of substitution and permutation for diffusion and confusion.

---

## Author

Your Name  
[Your GitHub Profile](https://github.com/your-username)

For questions or suggestions, feel free to open an issue in the repository.

--- 

Feel free to customize this README file further to suit your repository and personal preferences.
