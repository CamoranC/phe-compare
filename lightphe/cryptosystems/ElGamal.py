"""
Original from LightPHE https://github.com/serengil/LightPHE by Sefik Ilkin Serengil 

Modified Key Generation and changed reencryption to rerandomization
Added scalar multiplication
Changed naiive decryption to start from highest possible m.

"""

import random
import math
from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from lightphe.commons.logger import Logger
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime

logger = Logger(module="lightphe/cryptosystems/ElGamal.py")
class ElGamal(Homomorphic):
    """
    ElGamal algorithm is either multiplicatively or additively homomorphic
    Ref: https://sefiks.com/2023/03/27/a-step-by-step-partially-homomorphic-encryption-example-with-elgamal-in-python/
    """

    def __init__(self, keys: Optional[dict] = None, exponential=False, key_size: int = 1024, key_sizeq:int=160):
        """
        Args:
            keys (dict): private - public key pair.
                set this to None if you want to generate random keys.
            key_size (int): key size in bits
            exponential (boolean): set this to True to make cryptosystem exponential ElGamal.
                Regular ElGamal is homomorphic with respect to the multiplication whereas
                exponential ElGamal is homomorphic with respect to the addition
        """
        self.exponential = exponential
        self.keys = keys or self.generate_keys(key_size, key_sizeq)
        self.plaintext_modulo = self.keys["public_key"]["p"]
        self.ciphertext_modulo = self.keys["public_key"]["p"]

    def generate_keys(self, key_size: int, key_sizeq) -> dict:
        """
        Generate public and private keys of ElGamal cryptosystem
        Args:
            key_size (int): key size in bits
        Returns:
            keys (dict): having private_key and public_key keys
        """
        keys = {}
        keys["private_key"] = {}
        keys["public_key"] = {}

        # picking a prime q and p
        pt=getPrime(key_size-key_sizeq-1)
        while True:     
            
            q = getPrime(key_sizeq)            
            p = 2*pt*q+1
            #print(p.bit_length())
            if p.bit_length()==key_size and isPrime(p) :
                break
        
        # picking a generator g
        while True:
            y=random.randint(2, p-1)
            if math.gcd(y,p) != 1:
                continue
            g = pow(y,2*pt,p)
            if g!=1:
                break
        # picking a private key x
        xy = random.randint(1, p-1)
        x=pow(g,xy,p)

        # public key
        h = pow(g, x, p)

        keys["public_key"] = {
            "p": p,
            "q": q,
            "g": g,
            "h": h,
        }

        keys["private_key"] = {"x": x}

        return keys

    def generate_random_key(self) -> int:
        """
        ElGamal requires to generate one-time random key per encryption
        Returns:
            random key (int): one time random key for encryption
        """
        p = self.keys["public_key"]["p"]
        g = self.keys["public_key"]["g"]
        xy = random.randint(1, p-1)
        return pow(g,xy,p)

    def encrypt(self, plaintext: int, random_key: Optional[int] = None) -> tuple:
        """
        Encrypt plaintext with ElGamal
        Args:
            plaintext (int): message to encrypt
            random_key (int): random key for encryption. Do not set this to a static value.
        Returns
            ciphertext (tuple): c1 and c2
        """
        p = self.keys["public_key"]["p"]
        g = self.keys["public_key"]["g"]
        h = self.keys["public_key"]["h"]
        r = random_key or self.generate_random_key()

        if plaintext > p:
            plaintext = plaintext % p
            logger.debug(
                f"ElGamal can encrypt messages [1, {p}]. "
                f"Seems you exceeded this limit. New plaintext is {plaintext}"
            )

        c1 = pow(g, r, p)
        if self.exponential is False:
            c2 = (plaintext * pow(h, r, p)) % p
        else:
            c2 = (pow(g, plaintext, p) * pow(h, r, p)) % p

        return c1, c2

    def decrypt(self, ciphertext: tuple) -> int:
        """
        Decrypt ciphertext with ElGamal
        Args:
            ciphertext (tuple): c1 and c2
        Returns:
            plaintext (int): restored message
        """
        c1, c2 = ciphertext

        x = self.keys["private_key"]["x"]
        p = self.keys["public_key"]["p"]
        q = self.keys["public_key"]["q"]
        g = self.keys["public_key"]["g"]

        m_prime = (c2 * pow(c1, -1 * x, p)) % p

        if self.exponential is False:
            return m_prime

        if self.exponential is True:
            # m_prime = g^m . Find m for known m_prime and known g (DLP).
            m = q
            while True:
                if pow(g, m, p) == m_prime:
                    return m
                m -= 1
                if m <= 0:
                    raise ValueError(f"Cannot restore the message in [0, {p}]")

        return -1

    def multiply(self, ciphertext1: tuple, ciphertext2: tuple) -> tuple:
        """
        Perform homomorphic multiplication on encrypted data
        Result of this must be equal to E(m1 * m2)
        Args:
            ciphertext1 (dict): ElGamal ciphertext consisting of c1 and c2 keys
            ciphertext2 (dict): ElGamal ciphertext consisting of c1 and c2 keys
        Returns
            ciphertext (dict): ElGamal ciphertext consisting of c1 and c2 keys
        """
        if self.exponential is True:
            raise ValueError("Exponential ElGamal is not homomorphic with respect to the addition")
        p = self.keys["public_key"]["p"]
        return (ciphertext1[0] * ciphertext2[0]) % p, (ciphertext1[1] * ciphertext2[1]) % p

    def add(self, ciphertext1: tuple, ciphertext2: tuple) -> tuple:
        """
        Perform homomorphic addition on encrypted data
        Result of this must be equal to E(m1 + m2)
        Args:
            ciphertext1 (dict): ElGamal ciphertext consisting of c1 and c2 keys
            ciphertext2 (dict): ElGamal ciphertext consisting of c1 and c2 keys
        Returns
            ciphertext (dict): ElGamal ciphertext consisting of c1 and c2 keys
        """
        if self.exponential is False:
            raise ValueError("Regular ElGamal is not homomorphic with respect to the addition")
        p = self.keys["public_key"]["p"]
        return (ciphertext1[0] * ciphertext2[0]) % p, (ciphertext1[1] * ciphertext2[1]) % p

    def xor(self, ciphertext1: tuple, ciphertext2: tuple) -> int:
        raise ValueError("ElGamal is not homomorphic with respect to the exclusive or")

    def multiply_by_contant(self, ciphertext: tuple, constant: int) -> tuple:
        #if self.exponential is False:
            #raise ValueError("ElGamal is not supporting multiplying ciphertext by a known constant")
        q = self.keys["public_key"]["q"]
        p = self.keys["public_key"]["p"]
        if constant > q:
            constant = constant % q
            logger.debug(
                f"ElGamal can encrypt messages [1, {p}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )

        return pow(ciphertext[0], constant, p), pow(ciphertext[1], constant, p)
    
    def reencrypt(self, ciphertext: tuple) -> tuple:
        """
        Re-generate ciphertext with re-encryption. Many ciphertext will be decrypted to same plaintext.
        Args:
            ciphertext (int): given ciphertext
        Returns:
            new ciphertext (int): different ciphertext for same plaintext
        """
        #if self.exponential is True:
            # then this is additively homomorphic
           # neutral_element = 0
        #else:
            # then this is multiplicatively homomorphic
            #neutral_element = 1

        #neutral_encrypted = self.encrypt(plaintext=neutral_element)

        #if self.exponential is True:
            #reencrypted_value = self.add(ciphertext1=ciphertext, ciphertext2=neutral_encrypted)
        #else:
            #reencrypted_value = self.multiply(ciphertext1=ciphertext, ciphertext2=neutral_encrypted)
        #return reencrypted_value
        p = self.keys["public_key"]["p"]
        g = self.keys["public_key"]["g"]
        h = self.keys["public_key"]["h"]
        r=self.generate_random_key()
        c0=(ciphertext[0]*pow(g,r,p))%p
        c1=(ciphertext[1]*pow(h,r,p))%p
        return c0,c1

        
    

        
