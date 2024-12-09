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
