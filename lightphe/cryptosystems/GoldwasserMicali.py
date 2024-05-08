"""
Original from Light-PHE by serengil at: https://github.com/serengil/LightPHE.
Modified Key Generation and changed reencryption to rerandomization.
Changed XOR to work for bit-lists of diffrent lengths 
"""
import random
from typing import Optional
import math
from sympy import legendre_symbol
from lightphe.models.Homomorphic import Homomorphic
from lightphe.commons.logger import Logger
from Crypto.Util.number import getPrime

logger = Logger(module="lightphe/cryptosystems/GoldwasserMicali.py")

# pylint:disable=consider-using-enumerate

def ceildiv(a, b):
    return -(a // -b)

class GoldwasserMicali(Homomorphic):
    """
    Goldwasser-Micali algorithm is homomorphic with respect to the Exclusively OR (XOR).
    Ref: https://sefiks.com/2023/10/27/a-step-by-step-partially-homomorphic-encryption-example-with-goldwasser-micali-in-python/
    """

    def __init__(self, keys: Optional[dict] = None, key_size=1024):
        """
        Args:
            keys (dict): private - public key pair.
                set this to None if you want to generate random keys.
            key_size (int): key size in bits
        """
        self.keys = keys or self.generate_keys(key_size)
        self.ciphertext_modulo = self.keys["public_key"]["n"]
        # TODO: not sure about the plaintext modulo
        self.plaintext_modulo = self.keys["public_key"]["n"]

    def generate_keys(self, key_size: int) -> dict:
        """
        Generate public and private keys of Goldwasser-Micali cryptosystem
        Args:
            key_size (int): key size in bits
        Returns:
            keys (dict): having private_key and public_key keys
        """
        keys = {}
        keys["private_key"] = {}
        keys["public_key"] = {}
        while True:
            # picking a prime p
            p = getPrime(key_size // 2)
    
            # picking a prime q
            q = getPrime(key_size//2)
    
            n = p * q
            if n.bit_length()==key_size:
                break
        # find non-residue x
        while True:
            x = random.randint(1, n - 1)
            if legendre_symbol(x, p) == -1 and legendre_symbol(x, q) == -1:
                break

        keys["public_key"]["n"] = n
        keys["public_key"]["x"] = x

        keys["private_key"]["p"] = p
        keys["private_key"]["q"] = q

        return keys

    def generate_random_key(self) -> int:
        """
        Goldwasser-Micali requires to generate one-time random key that co-prime to n
        Returns:
            random key (int): one time random key for encryption
        """
        n = self.keys["public_key"]["n"]
        while True:
            r = random.randint(1, n)
            if math.gcd(r, n) == 1:
                break
        return r

    def encrypt(self, plaintext: int, random_key: Optional[int] = None) -> list:
        """
        Encrypt a given plaintext for optionally given random key with Goldwasser-Micali
        Args:
            plaintext (int): message to encrypt
            random_key (int): Goldwasser-Micali requires a random key
                Random key will be generated automatically if you do not set this.
        Returns:
            ciphertext (int): encrypted message
        """
        n = self.keys["public_key"]["n"]
        x = self.keys["public_key"]["x"]

        m_binary = bin(plaintext)[2:]

        # number of bits
        k = len(m_binary)

        if random_key and len(random_key) != k:
            raise ValueError(f"Random key must be length of {k}")

        c = []
        for i in range(0, k):
            mi = int(m_binary[i])

            if random_key:
                ri = random_key[i]
            else:
                ri = self.generate_random_key()

            ci = (pow(ri, 2, n) * pow(x, mi, n)) % n
            c.append(ci)

        return c

    def decrypt(self, ciphertext: list) -> int:
        """
        Decrypt a given ciphertext with Goldwasser-Micali
        Args:
            ciphertext (int): encrypted message
        Returns:
            plaintext (int): restored message
        """
        m_binaries = []

        p = self.keys["private_key"]["p"]
        q = self.keys["private_key"]["q"]

        for i in ciphertext:
            #xp = i % p
            #xq = i % q

            #if pow(xp, int((p - 1) / 2), p) == 1 and pow(xq, int((q - 1) / 2), q) == 1:
                #m_binaries.append("0")
            if legendre_symbol(i,p) == 1 and legendre_symbol(i,q) ==1:
                m_binaries.append("0")
            else:
                m_binaries.append("1")

        m_binary = "".join(m_binaries)
        return int(m_binary, 2)

    def add(self, ciphertext1: list, ciphertext2: list) -> list:
        raise ValueError("Goldwasser-Micali is not homomorphic with respect to the addition")

    def multiply(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Goldwasser-Micali is not homomorphic with respect to the multiplication")

    def xor(self, ciphertext1: int, ciphertext2: int) -> list:
        """
        Perform homomorphic xor on encrypted data.
        Result of this must be equal to E(m1 ^ m2) = E(m1) ^ E(m2)
        Encryption calculations are done in module n
        Args:
            ciphertext1 (int): 1st ciphertext created with Goldwasser-Micali
            ciphertext2 (int): 2nd ciphertext created with Goldwasser-Micali
        Returns:
            ciphertext3 (int): 3rd ciphertext created with Goldwasser-Micali
        """
        if isinstance(ciphertext1,int):
            ciphertext1=[ciphertext1]
        if isinstance(ciphertext2,int):
            ciphertext2=[ciphertext2]
        
        ciphertext3 = []
        if len(ciphertext1) < len(ciphertext2):
            minc=ciphertext1
            maxc=ciphertext2
        else:
            minc=ciphertext2
            maxc=ciphertext1
        diff=len(maxc)-len(minc)
        for i in range(0, len(maxc)):
            if i<diff:
                c1 = 1
            else:
                c1 = minc[i-diff]
            c2 = maxc[i]
            ciphertext3.append((c1 * c2) % self.ciphertext_modulo)

        return ciphertext3

    def multiply_by_contant(self, ciphertext: int, constant: int):
        raise ValueError("Goldwasser-Micali does not support multiplying with constant")

    def reencrypt(self, ciphertext: int):
        n = self.keys["public_key"]["n"]
        res=[]
        for i in ciphertext:
            x=self.generate_random_key()
            c=((x**2)*i)%n
            res.append(c)
        return res
        
