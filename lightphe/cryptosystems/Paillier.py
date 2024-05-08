"""
Original from Light-PHE by serengil at: https://github.com/serengil/LightPHE.
Modified Key Generation and changed reencryption to rerandomization.
"""

import random
import math
from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from lightphe.commons.logger import Logger
from Crypto.Util.number import getPrime

logger = Logger(module="lightphe/cryptosystems/Paillier.py")


class Paillier(Homomorphic):
    """
    Paillier algorithm is homomorphic with respect to the addition.
    Also, it supports power operation for ciphertext base and plaintext exponent
    Ref: https://sefiks.com/2023/04/03/a-step-by-step-partially-homomorphic-encryption-example-with-paillier-in-python/
    """

    def __init__(self, keys: Optional[dict] = None, key_size=1024):
        """
        Args:
            keys (dict): private - public key pair.
                set this to None if you want to generate random keys.
            key_size (int): key size in bits
        """
        self.keys = keys or self.generate_keys(key_size)
        n = self.keys["public_key"]["n"]
        self.plaintext_modulo = n
        self.ciphertext_modulo = n * n

    def generate_keys(self, key_size: int):
        """
        Generate public and private keys of Paillier cryptosystem
        Args:
            key_size (int): key size in bits
        Returns:
            keys (dict): having private_key and public_key keys
        """
        keys = {}
        keys["private_key"] = {}
        keys["public_key"] = {}
        while True:
            # picking a prime modulus p
            p = getPrime(key_size//2)
    
            # picking a prime modulus q
            q = getPrime(key_size//2)
    
            n = p * q
            if p!=q and n.bit_length()==key_size:
                break
        phi = (p - 1) * (q - 1)
        g = 1 + n

        keys["private_key"]["phi"] = phi
        keys["public_key"]["g"] = g
        keys["public_key"]["n"] = n

        return keys

    def generate_random_key(self) -> int:
        """
        Paillier requires to generate one-time random key per encryption
        Returns:
            random key (int): one time random key for encryption
        """
        n = self.keys["public_key"]["n"]
        while True:
            r = random.randint(0, n)
            if math.gcd(r, n) == 1:
                break
        return r

    def encrypt(self, plaintext: int, random_key: Optional[int] = None) -> int:
        """
        Encrypt a given plaintext for optionally given random key with Paillier
        Args:
            plaintext (int): message to encrypt
            random_key (int): Paillier requires a random key that co-prime to n.
                Random key will be generated automatically if you do not set this.
        Returns:
            ciphertext (int): encrypted message
        """
        g = self.keys["public_key"]["g"]
        n = self.keys["public_key"]["n"]
        r = random_key or self.generate_random_key()
        assert math.gcd(r, n) == 1
        return (pow(g, plaintext, self.ciphertext_modulo) * pow(r, n, self.ciphertext_modulo)) % (self.ciphertext_modulo)

    def decrypt(self, ciphertext: int):
        """
        Decrypt a given ciphertext with Paillier
        Args:
            ciphertext (int): encrypted message
        Returns:
            plaintext (int): restored message
        """
        phi = self.keys["private_key"]["phi"]
        n = self.keys["public_key"]["n"]
        mu = pow(phi, -1, n)

        return (self.lx(pow(ciphertext, phi, self.ciphertext_modulo)) * mu) % (n)
        

    def add(self, ciphertext1: int, ciphertext2: int) -> int:
        """
        Perform homomorphic addition on encrypted data.
        Result of this must be equal to E(m1 + m2)
        Encryption calculations are done in module n squared.
        Args:
            ciphertext1 (int): 1st ciphertext created with Paillier
            ciphertext2 (int): 2nd ciphertext created with Paillier
        Returns:
            ciphertext3 (int): 3rd ciphertext created with Paillier
        """
        #n = self.keys["public_key"]["n"]
        return (ciphertext1 * ciphertext2) % (self.ciphertext_modulo)

    def multiply(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Paillier is not homomorphic with respect to the multiplication")

    def xor(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Paillier is not homomorphic with respect to the exclusive or")

    def multiply_by_contant(self, ciphertext: int, constant: int) -> int:
        """
        Multiply a ciphertext with a plain constant.
        Result of this must be equal to E(m1 * m2) where E(m1) = ciphertext
        Encryption calculations are done in module n squared.
        Args:
            ciphertext (int): ciphertext created with Paillier
            constant (int): known plain constant
        Returns:
            ciphertext (int): new ciphertext created with Paillier
        """
        n = self.keys["public_key"]["n"]

        if constant > self.plaintext_modulo:
            constant = constant % self.plaintext_modulo
            logger.debug(
                f"Paillier can encrypt messages [1, {n}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )

        return pow(ciphertext, constant, n * n)

    def reencrypt(self, ciphertext: int) -> int:
        """
        Re-generate ciphertext with re-encryption. Many ciphertext will be decrypted to same plaintext.
        Args:
            ciphertext (int): given ciphertext
        Returns:
            new ciphertext (int): different ciphertext for same plaintext
        """
        r=self.generate_random_key()
        n=self.keys["public_key"]["n"]
        return (pow(r,n,self.ciphertext_modulo)*ciphertext) % self.ciphertext_modulo

    def lx(self, x: int) -> int:
        """
        Find logarithm over cyclic group
        Args:
            x (int): some integer
        Returns:
            lx (int): (x-1) / n
        """
        n = self.keys["public_key"]["n"]
        y = (x - 1) // n
        assert y - int(y) == 0
        return int(y)
