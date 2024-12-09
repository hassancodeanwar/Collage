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



# Input text
plaintext = "Hello, World!"
shift = 3

# Encrypt the plaintext
encrypted_text = encrypt(plaintext, shift)
print(f"Encrypted: {encrypted_text}")

# Decrypt the ciphertext
decrypted_text = decrypt(encrypted_text, shift)
print(f"Decrypted: {decrypted_text}")
