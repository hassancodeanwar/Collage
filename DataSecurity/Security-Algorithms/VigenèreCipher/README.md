# Vigenère Cipher Algorithm Documentation

## Overview


|------|-------|
| The **Vigenère Cipher** is a method of encrypting alphabetic text by using a series of different Caesar ciphers based on the letters of a keyword. This polyalphabetic substitution cipher enhances security compared to simple ciphers by using multiple shifting techniques, making it more resistant to frequency analysis. | <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Vigenere.jpg" alt="Vigenère Cipher"> |



## How It Works

### Key Concepts

1. **Polyalphabetic Cipher**: Unlike monoalphabetic ciphers, which use a single alphabet, the Vigenère cipher employs multiple alphabets based on the keyword.
2. **Keyword**: The keyword is repeated to match the length of the plaintext. Each letter in the keyword corresponds to a shift value based on its position in the alphabet (A=0, B=1, ..., Z=25).

### Encryption Process

1. **Padding the Key**: The keyword is repeated until it matches the length of the plaintext.
2. **Character Encryption**:
   - For each character in the plaintext, find its corresponding character in the padded key.
   - Calculate the new character using:
     $$
     E_i = (P_i + K_i) \mod 26
     $$
   - Here, $$E_i$$ is the encrypted character, $$P_i$$ is the plaintext character, and $$K_i$$ is the key character.

### Decryption Process

To retrieve the original message from the ciphertext:

1. **Padding the Key**: Repeat the keyword to match the length of the ciphertext.
2. **Character Decryption**:
   - For each character in the ciphertext, find its corresponding character in the padded key.
   - Calculate the original character using:
     $$
     D_i = (E_i - K_i + 26) \mod 26
     $$
   - Here, $$D_i$$ is the decrypted character.

### Example

- **Plaintext**: "HELLO"
- **Keyword**: "KEY"
- **Padded Keyword**: "KEYKE"

The encryption process would look like this:

| Plaintext | H | E | L | L | O |
|-----------|---|---|---|---|---|
| Keyword   | K | E | Y | K | E |
| Encrypted | R | I | J | V | S |

To decrypt "RIJVS" back to "HELLO", repeat "KEY" and apply the decryption formula.

## Implementation

The provided Python code implements both encryption and decryption functions for the Vigenère Cipher:

```python
def _pad_key(plaintext, key):
    """
    Pads the key to match the length of the plaintext.
    """
    key = key * (len(plaintext) // len(key)) + key[:len(plaintext) % len(key)]
    return key


def _encrypt_decrypt_char(char, key_char, mode="encrypt"):
    """
    Encrypts or decrypts a single character using a key character.
    Supports only alphabetic characters.
    """
    if char.isalpha():
        first_letter = 'A' if char.isupper() else 'a'
        char_pos = ord(char) - ord(first_letter)
        key_pos = ord(key_char.lower()) - ord('a')

        if mode == "encrypt":
            new_pos = (char_pos + key_pos) % 26
        else:  # decrypt
            new_pos = (char_pos - key_pos + 26) % 26

        return chr(new_pos + ord(first_letter))
    return char  # Non-alphabetic characters remain unchanged


def encrypt(plaintext, key):
    """
    Encrypts the plaintext using the Vigenère cipher and a given key.
    """
    padded_key = _pad_key(plaintext, key)
    ciphertext = ''.join(
        _encrypt_decrypt_char(pt_char, k_char, mode="encrypt")
        for pt_char, k_char in zip(plaintext, padded_key)
    )
    return ciphertext


def decrypt(ciphertext, key):
    """
    Decrypts the ciphertext using the Vigenère cipher and a given key.
    """
    padded_key = _pad_key(ciphertext, key)
    plaintext = ''.join(
        _encrypt_decrypt_char(ct_char, k_char, mode="decrypt")
        for ct_char, k_char in zip(ciphertext, padded_key)
    )
    return plaintext


# Main program
if __name__ == "__main__":
    plaintext = input("Enter a message: ")
    key = input("Enter a key: ")

    ciphertext = encrypt(plaintext, key)
    decrypted_plaintext = decrypt(ciphertext, key)

    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted Plaintext: {decrypted_plaintext}")
```

### Functions Explained

- **`_pad_key(plaintext, key)`**: Pads or repeats the keyword to match the length of the plaintext or ciphertext.
  
- **`_encrypt_decrypt_char(char, key_char, mode)`**: Encrypts or decrypts a single character based on its corresponding character in the keyword.

- **`encrypt(plaintext, key)`**: Takes a string `plaintext` and an integer `key`, returning the encrypted version.

- **`decrypt(ciphertext, key)`**: Takes a string `ciphertext` and an integer `key`, returning the decrypted version.

### Example Usage

```python
# Main program example
if __name__ == "__main__":
    plaintext = input("Enter a message: ")
    key = input("Enter a key: ")

    ciphertext = encrypt(plaintext, key)
    decrypted_plaintext = decrypt(ciphertext, key)

    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted Plaintext: {decrypted_plaintext}")
```

## Complexity Analysis

The time complexity for both encryption and decryption processes is $$O(N)$$, where $$N$$ is the length of the input text. Each character is processed individually.

## Advantages and Disadvantages

### Advantages
- **Increased Security**: More secure than simple ciphers due to multiple shifting techniques.
- **Flexibility**: Can use any length of keywords for varying levels of security.

### Disadvantages
- **Vulnerability to Frequency Analysis**: While more secure than monoalphabetic ciphers, it can still be broken with enough ciphertext and analysis.
- **Key Management**: Requires careful handling of keys to maintain security.

## Conclusion

The Vigenère Cipher is an essential tool in classical cryptography that combines simplicity with enhanced security through polyalphabetic encryption techniques. While not suitable for modern secure communications without additional measures, it serves as an excellent educational tool for understanding fundamental cryptographic principles.

Citations:
   - [1] https://dev.to/cognivibes/understanding-the-vigenere-cipher-16g5
   - [2] https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html
   - [3] https://brilliant.org/wiki/vigenere-cipher/
   - [4] https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher
   - [5] https://www.javatpoint.com/vigenere-cipher
