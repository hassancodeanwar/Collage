# Caesar Cipher Algorithm Documentation

## Overview

The **Caesar Cipher** is one of the simplest and most well-known encryption techniques. Named after Julius Caesar, who reportedly used it to communicate with his generals, this method involves shifting the letters of the plaintext by a fixed number of positions down or up the alphabet. For example, with a shift of 3, 'A' becomes 'D', 'B' becomes 'E', and so forth. This substitution cipher is a type of monoalphabetic cipher where each letter is replaced by another letter based on the specified shift.

## How It Works

### Encryption Process

1. **Choose a Shift Value**: The user selects an integer value, known as the shift or key, which determines how many positions each letter in the plaintext will be moved.
2. **Transform Letters**: Each letter in the plaintext is replaced by a letter that is a fixed number of positions down the alphabet. If the end of the alphabet is reached, it wraps around to the beginning.
3. **Mathematical Representation**:
   - For encryption: 
     $$
     E_n(x) = (x + n) \mod 26
     $$
   - Here, $$x$$ represents the position of the letter in the alphabet (A=0, B=1, ..., Z=25), and $$n$$ is the shift value.

### Decryption Process

To retrieve the original message from the encrypted text, the decryption process involves shifting letters back by the same amount:

1. **Reverse Shift**: Each letter is shifted back by the same number of positions used during encryption.
2. **Mathematical Representation**:
   - For decryption:
     $$
     D_n(x) = (x - n) \mod 26
     $$

### Example

- **Plaintext**: "HELLO"
- **Shift**: 3
- **Encrypted Text**: "KHOOR"

To decrypt "KHOOR" back to "HELLO", each letter is shifted back by 3.

## Implementation

The provided Python code implements both encryption and decryption functions for the Caesar Cipher:

```python
def caesar_cipher_char(char, shift, mode='encrypt'):
    if char.isalpha():
        base_char = 'a' if char.islower() else 'A'
        char_position = ord(char) - ord(base_char)
        
        if mode == 'encrypt':
            new_position = (char_position + shift) % 26
        else:
            new_position = (char_position - shift) % 26
        
        return chr(new_position + ord(base_char))
    return char


def encrypt(plaintext, shift):
    return ''.join(caesar_cipher_char(char, shift, mode='encrypt') for char in plaintext)


def decrypt(ciphertext, shift):
    return ''.join(caesar_cipher_char(char, shift, mode='decrypt') for char in ciphertext)
```

### Functions Explained

- **`caesar_cipher_char(char, shift, mode)`**: 
  - Takes a character `char`, an integer `shift`, and a string `mode` ('encrypt' or 'decrypt').
  - Returns the encrypted or decrypted character based on the specified mode.

- **`encrypt(plaintext, shift)`**: 
  - Takes a string `plaintext` and an integer `shift`.
  - Returns the encrypted version of `plaintext`.

- **`decrypt(ciphertext, shift)`**: 
  - Takes a string `ciphertext` and an integer `shift`.
  - Returns the decrypted version of `ciphertext`.

### Example Usage

```python
# Input text
plaintext = "Hello, World!"
shift = 3

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, shift)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted: {decrypted_text}")
```

## Complexity Analysis

The time complexity for both encryption and decryption processes is $$O(N)$$, where $$N$$ is the length of the input text. Each character is processed individually.

## Advantages and Disadvantages

### Advantages
- **Simplicity**: Easy to understand and implement.
- **Low Resource Requirement**: Requires minimal computational resources.

### Disadvantages
- **Vulnerability**: Easily broken with modern techniques; frequency analysis can reveal patterns.
- **Limited Security**: Only offers basic security; not suitable for serious applications.

## Conclusion

The Caesar Cipher serves as an excellent introduction to cryptography concepts. While it may not provide strong security in contemporary contexts, its simplicity makes it a valuable educational tool for understanding basic encryption techniques.

Citations:
[1] https://www.splunk.com/en_us/blog/learn/caesar-cipher.html
[2] https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/
[3] https://codedamn.com/news/cryptography/caesar-cipher-introduction
[4] https://www.javatpoint.com/caesar-cipher-technique
[5] https://brilliant.org/wiki/caesar-cipher/
[6] https://en.wikipedia.org/wiki/Caesar_cypher
