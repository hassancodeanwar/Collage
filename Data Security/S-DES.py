import numpy as np

class SDES:
    def __init__(self):
        # Key Generation Tables
        self.table_p10 = np.array([3, 5, 2, 7, 4, 10, 1, 9, 8, 6])
        self.table_p8 = np.array([6, 3, 7, 4, 8, 5, 10, 9])
        
        # Encryption/Decryption Tables
        self.table_ip = np.array([2, 6, 3, 1, 4, 8, 5, 7])
        self.table_ip_inv = np.array([4, 1, 3, 5, 7, 2, 8, 6])
        self.table_ep = np.array([4, 1, 2, 3, 2, 3, 4, 1])
        self.table_p4 = np.array([2, 4, 3, 1])
        
        # S-Boxes
        self.s0 = np.array([
            [1, 0, 3, 2],
            [3, 2, 1, 0],
            [0, 2, 1, 3],
            [3, 1, 3, 2]
        ])
        
        self.s1 = np.array([
            [0, 1, 2, 3],
            [2, 0, 1, 3],
            [3, 0, 1, 0],
            [2, 1, 0, 3]
        ])

    def table_shift(self, array, table_array):
        """Apply permutation table to array"""
        array_shifted = np.zeros(table_array.shape[0], dtype='int')
        for index, value in enumerate(table_array):
            array_shifted[index] = array[value - 1]
        return array_shifted

    def array_split(self, array):
        """Split array into two equal parts"""
        mid = len(array) // 2
        return array[:mid], array[mid:]

    def shifting_LtoR(self, array):
        """Perform left circular shift"""
        return np.roll(array, -1)

    def split_and_merge(self, key, shifts=1):
        """Split key, shift both halves, and merge"""
        left_split, right_split = self.array_split(key)
        
        # Apply shifts
        for _ in range(shifts):
            left_split = self.shifting_LtoR(left_split)
            right_split = self.shifting_LtoR(right_split)
            
        return np.concatenate((left_split, right_split))

    def key_generation(self, key):
        """Generate both subkeys"""
        # Convert string key to numpy array if necessary
        if isinstance(key, str):
            key = np.array([int(bit) for bit in key])
            
        # Generate K1
        k10 = self.table_shift(key, self.table_p10)
        k1_temp = self.split_and_merge(k10, shifts=1)
        k1 = self.table_shift(k1_temp, self.table_p8)
        
        # Generate K2
        k2_temp = self.split_and_merge(k1_temp, shifts=2)
        k2 = self.table_shift(k2_temp, self.table_p8)
        
        return k1, k2

    def sbox_lookup(self, input_bits, sbox):
        """Perform S-box substitution"""
        row = input_bits[0] * 2 + input_bits[-1]
        col = input_bits[1] * 2 + input_bits[2]
        value = sbox[row, col]
        return np.array([value // 2, value % 2])

    def feistel_function(self, right_half, subkey):
        """Implement the Feistel function"""
        # Expansion
        expanded = self.table_shift(right_half, self.table_ep)
        
        # XOR with subkey
        xored = np.bitwise_xor(expanded, subkey)
        
        # Split for S-box substitution
        left_xored, right_xored = self.array_split(xored)
        
        # Apply S-boxes
        s0_out = self.sbox_lookup(left_xored, self.s0)
        s1_out = self.sbox_lookup(right_xored, self.s1)
        
        # Combine and apply P4
        combined = np.concatenate((s0_out, s1_out))
        return self.table_shift(combined, self.table_p4)

    def encrypt_block(self, plaintext, key):
        """Encrypt 8-bit block using SDES"""
        # Convert string plaintext to numpy array if necessary
        if isinstance(plaintext, str):
            plaintext = np.array([int(bit) for bit in plaintext])
            
        # Generate subkeys
        k1, k2 = self.key_generation(key)
        
        # Initial permutation
        ip_out = self.table_shift(plaintext, self.table_ip)
        left, right = self.array_split(ip_out)
        
        # First round
        f1_out = self.feistel_function(right, k1)
        new_right = np.bitwise_xor(left, f1_out)
        new_left = right
        
        # Second round
        f2_out = self.feistel_function(new_right, k2)
        final_left = np.bitwise_xor(new_left, f2_out)
        final_right = new_right
        
        # Final permutation
        pre_output = np.concatenate((final_left, final_right))
        output = self.table_shift(pre_output, self.table_ip_inv)
        
        return ''.join(map(str, output))

    def decrypt_block(self, ciphertext, key):
        """Decrypt 8-bit block using SDES"""
        # Convert string ciphertext to numpy array if necessary
        if isinstance(ciphertext, str):
            ciphertext = np.array([int(bit) for bit in ciphertext])
            
        # Generate subkeys
        k1, k2 = self.key_generation(key)
        
        # Initial permutation
        ip_out = self.table_shift(ciphertext, self.table_ip)
        left, right = self.array_split(ip_out)
        
        # First round (using K2)
        f1_out = self.feistel_function(right, k2)
        new_right = np.bitwise_xor(left, f1_out)
        new_left = right
        
        # Second round (using K1)
        f2_out = self.feistel_function(new_right, k1)
        final_left = np.bitwise_xor(new_left, f2_out)
        final_right = new_right
        
        # Final permutation
        pre_output = np.concatenate((final_left, final_right))
        output = self.table_shift(pre_output, self.table_ip_inv)
        
        return ''.join(map(str, output))

def main():
    # Create SDES instance
    sdes = SDES()
    
    # Test key generation
    key = '0001101101'
    k1, k2 = sdes.key_generation(key)
    print("Key Generation Test:")
    print(f"Original Key: {key}")
    print(f"Key 1: {''.join(map(str, k1))}")
    print(f"Key 2: {''.join(map(str, k2))}")
    
    # Test encryption/decryption
    plaintext = '11010111'
    print("\nEncryption/Decryption Test:")
    print(f"Plaintext: {plaintext}")
    
    # Encrypt
    ciphertext = sdes.encrypt_block(plaintext, key)
    print(f"Ciphertext: {ciphertext}")
    
    # Decrypt
    decrypted = sdes.decrypt_block(ciphertext, key)
    print(f"Decrypted: {decrypted}")
    print(f"Successful: {plaintext == decrypted}")

if __name__ == "__main__":
    main()
