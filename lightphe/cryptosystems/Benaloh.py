"""
Original from LightPHE https://github.com/serengil/LightPHE by Sefik Ilkin Serengil 

Modified Key Generation and changed reencryption to rerandomization
Added scalar multiplication

"""

import random
from math import gcd
from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from lightphe.commons.logger import Logger
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
import math
from Crypto.Util.number import getRandomNBitInteger

logger = Logger(module="lightphe/cryptosystems/Benaloh.py")

def ceildiv(a, b):
    return -(a // -b)

class Benaloh(Homomorphic):
    def __init__(self, keys: Optional[dict] = None, key_size: int = 50, r:int=None):
        """
        Args:
            keys (dict): private - public key pair.
                set this to None if you want to generate random keys.
            key_size (int): key size in bits. default is less than other cryptosystems
                because decryption of Benaloh requires to solve DLP :/
        """
        self.keys = keys or self.generate_keys(key_size,r)
        self.plaintext_modulo = self.keys["public_key"]["r"]
        self.ciphertext_modulo = self.keys["public_key"]["n"]

    def generate_keys(self, key_size: int, bit:int) -> dict:
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
        
        
        r=getPrime(bit)
        while True:
            q=getPrime(key_size//3)
            if math.gcd(r,q-1)==1:
                break
        rest=key_size-bit-q.bit_length()
        while True:
            x=getRandomNBitInteger(rest+1)
            if math.gcd(x,r) != 1:
                continue
            p=x*r+1
            n = p * q
            if isPrime(p) and n.bit_length()==key_size:
                break
            
        phi = (p - 1) * (q - 1)

        while True:
            y = random.randint(2, n)
            if gcd(y,n) == 1 and pow(y, phi // r, n) != 1:
                    break

        keys["public_key"]["y"] = y
        keys["public_key"]["r"] = r
        keys["public_key"]["n"] = n

        keys["private_key"]["p"] = p
        keys["private_key"]["q"] = q
        #keys["private_key"]["phi"] = phi
        #keys["private_key"]["x"] = x

        return keys

    def generate_random_key(self) -> int:
        """
        Generate random key for encryption
        """
        n = self.keys["public_key"]["n"]
        while True:
            u = random.randint(1, n)
            if gcd(u, n) == 1:
                break
        return u

    def encrypt(self, plaintext: int, random_key: Optional[int] = None) -> int:
        """
        Encrypt a given plaintext for optionally given random key with Benaloh
        Args:
            plaintext (int): message to encrypt
            random_key (int): Benaloh requires a random key
                Random key will be generated automatically if you do not set this.
        Returns:
            ciphertext (int): encrypted message
        """
        y = self.keys["public_key"]["y"]
        r = self.keys["public_key"]["r"]
        n = self.keys["public_key"]["n"]

        u = random_key or self.generate_random_key()

        if plaintext > r:
            plaintext = plaintext % r
            logger.debug(
                f"Benaloh lets you to encrypt messages in [0, {r=}]."
                f"But your plaintext exceeds this limit."
                f"New plaintext is {plaintext}"
            )

        c = (pow(y, plaintext, n) * pow(u, r, n)) % n

        if gcd(c, n) != 1:
            logger.debug("ciphertext is not co-prime with n!")

        return c

    def decrypt(self, ciphertext: int) -> int:
        """
        Decrypt a given ciphertext with Benaloh
        Args:
            ciphertext (int): encrypted message
        Returns:
            plaintext (int): restored message
        """
        n = self.keys["public_key"]["n"]
        r = self.keys["public_key"]["r"]
        y = self.keys["public_key"]["y"]
        p = self.keys["private_key"]["p"]
        q = self.keys["private_key"]["q"] 
        phi=(p-1)*(q-1)
        x=pow(y,phi//r,n)
        a = pow(ciphertext, phi//r, n)

        md = r
        while True:
            if pow(x, md, n) == a:
                break
            md = md - 1
            if md < 0:
                raise ValueError(f"Message cannot be restored in [{0}, {n}]")
        return md

    def add(self, ciphertext1: int, ciphertext2: int) -> int:
        """
        Perform homomorphic addition on encrypted data.
        Result of this must be equal to E(m1 + m2)
        Encryption calculations are done in module n
        Args:
            ciphertext1 (int): 1st ciphertext created with Benaloh
            ciphertext2 (int): 2nd ciphertext created with Benaloh
        Returns:
            ciphertext3 (int): 3rd ciphertext created with Benaloh
        """
        n = self.keys["public_key"]["n"]
        return (ciphertext1 * ciphertext2) % n

    def multiply(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Benaloh is not homomorphic with respect to the multiplication")

    def xor(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Benaloh is not homomorphic with respect to the exclusive or")

    def multiply_by_contant(self, ciphertext: int, constant: int) -> int:
        """
        Multiply a ciphertext with a plain constant.
        Result of this must be equal to E(m1 * constant) where E(m1) = ciphertext
        Encryption calculations are done in module n squared.
        Args:
            ciphertext (int): ciphertext created with Benaloh
            constant (int): known plain constant
        Returns:
            ciphertext (int): new ciphertext created with Benaloh
        """
        # raise ValueError("Benaloh is not supporting multiplying by a constant")
        n = self.keys["public_key"]["n"]
        if constant > self.plaintext_modulo:
            constant = constant % self.plaintext_modulo
            logger.debug(
                f"Benaloh can encrypt messages [1, {self.plaintext_modulo}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )
        return pow(ciphertext, constant, n)
    
    def add_with_constant(self, ciphertext: int, constant:int) -> int:
        n = self.keys["public_key"]["n"]
        y = self.keys["public_key"]["y"]
        if constant > self.plaintext_modulo:
            constant = constant % self.plaintext_modulo
            logger.debug(
                f"Benaloh can encrypt messages [1, {self.plaintext_modulo}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )
        return (ciphertext*pow(y,constant,n))%n

    def reencrypt(self, ciphertext: int) -> int:
        """
        Re-generate ciphertext with re-encryption. Many ciphertext will be decrypted to same plaintext.
        Args:
            ciphertext (int): given ciphertext
        Returns:
            new ciphertext (int): different ciphertext for same plaintext
        """
        #neutral_element = 0
        #neutral_encrypted = self.encrypt(plaintext=neutral_element)
        #return self.add(ciphertext1=ciphertext, ciphertext2=neutral_encrypted)
        r = self.keys["public_key"]["r"]
        n = self.keys["public_key"]["n"]
        x=self.generate_random_key()
        return (pow(x,r,n)*ciphertext)%n
