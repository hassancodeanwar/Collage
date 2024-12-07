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

    def shift(self, ar, n):
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
        Ls_1 = self.shift(Ls, 1)
        Rs_1 = self.shift(Rs, 1)
        key_ = Ls_1 + Rs_1
        self.key1 = [key_[self.P8[i] - 1] for i in range(8)]
        
        # Generate second subkey (K2)
        Ls_2 = self.shift(Ls, 2)
        Rs_2 = self.shift(Rs, 2)
        key_ = Ls_2 + Rs_2
        self.key2 = [key_[self.P8[i] - 1] for i in range(8)]
        
        print("Key-1:", ' '.join(map(str, self.key1)))
        print("Key-2:", ' '.join(map(str, self.key2)))

    def binary_(self, val):
        """Convert decimal to 2-bit binary string"""
        return f"{val:02b}"

    def function_(self, ar, key_):
        """Core encryption/decryption function"""
        # Split into left and right halves
        l = ar[:4]
        r = ar[4:]
        
        # Expansion Permutation
        ep = [r[self.EP[i] - 1] for i in range(8)]
        
        # XOR with key
        xor_result = [key_[i] ^ ep[i] for i in range(8)]
        
        # Split XOR result
        l_1 = xor_result[:4]
        r_1 = xor_result[4:]
        
        # S-Box substitution
        row_l = int(f"{l_1[0]}{l_1[3]}", 2)
        col_l = int(f"{l_1[1]}{l_1[2]}", 2)
        val_l = self.S0[row_l][col_l]
        str_l = self.binary_(val_l)
        
        row_r = int(f"{r_1[0]}{r_1[3]}", 2)
        col_r = int(f"{r_1[1]}{r_1[2]}", 2)
        val_r = self.S1[row_r][col_r]
        str_r = self.binary_(val_r)
        
        # Combine S-Box outputs
        r_ = [int(str_l[0]), int(str_l[1]), 
              int(str_r[0]), int(str_r[1])]
        
        # P4 Permutation
        r_p4 = [r_[self.P4[i] - 1] for i in range(4)]
        
        # XOR with left half
        l = [l[i] ^ r_p4[i] for i in range(4)]
        
        return l + r

    def swap(self, array):
        """Swap left and right halves"""
        n = len(array) // 2
        return array[n:] + array[:n]

    def encryption(self, plaintext):
        """Encrypt 8-bit block"""
        # Initial Permutation
        arr = [plaintext[self.IP[i] - 1] for i in range(8)]
        
        # First round with K1
        arr1 = self.function_(arr, self.key1)
        
        # Swap
        after_swap = self.swap(arr1)
        
        # Second round with K2
        arr2 = self.function_(after_swap, self.key2)
        
        # Final Permutation
        ciphertext = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        
        return ciphertext

    def decryption(self, ciphertext):
        """Decrypt 8-bit block"""
        # Initial Permutation
        arr = [ciphertext[self.IP[i] - 1] for i in range(8)]
        
        # First round with K2
        arr1 = self.function_(arr, self.key2)
        
        # Swap
        after_swap = self.swap(arr1)
        
        # Second round with K1
        arr2 = self.function_(after_swap, self.key1)
        
        # Final Permutation
        decrypted = [arr2[self.IP_inv[i] - 1] for i in range(8)]
        
        return decrypted

def main():
    # Create SDES instance
    sdes = SDES()
    
    # Generate keys
    sdes.key_generation()
    
    # Plaintext
    plaintext = [1, 0, 0, 1, 0, 1, 1, 1]
    
    print("\nPlain Text:", ' '.join(map(str, plaintext)))
    
    # Encrypt
    ciphertext = sdes.encryption(plaintext)
    print("Cipher Text:", ' '.join(map(str, ciphertext)))
    
    # Decrypt
    decrypted = sdes.decryption(ciphertext)
    print("Decrypted Text:", ' '.join(map(str, decrypted)))
    
    # Verify
    print("Decryption Successful:", plaintext == decrypted)

if __name__ == "__main__":
    main()
