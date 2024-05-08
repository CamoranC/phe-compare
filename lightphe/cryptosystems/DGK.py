# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 23:52:18 2024

@author: Christian

Based on the DGK Implementation in TNO PET Lab https://github.com/TNO-MPC by Bart Kamphorst and Thomas Rooijakkers
"""
import random
from typing import Optional
from lightphe.models.Homomorphic import Homomorphic
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime
from sympy import nextprime
from lightphe.commons.logger import Logger
from typing import Iterable, Tuple
from Crypto.Util.number import getRandomNBitInteger

logger = Logger(module="lightphe/cryptosystems/DGK.py")

def ceildiv(a, b):
    return -(a // -b)

class DGK (Homomorphic):
    def __init__(self, keys: Optional[dict] = None, key_sizek: int = 1024, key_sizet: int = 80, key_sizel: int=16):
        self.keys = keys or self.generate_keys(key_sizek,key_sizet,key_sizel)
        self.plaintext_modulo = self.keys["public_key"]["u"]
        self.ciphertext_modulo = self.keys["public_key"]["n"]
    
    def generate_keys(self, key_sizek: int,key_sizet: int,key_sizel: int)  ->dict:
        
        keys = {}
        keys["private_key"] = {}
        keys["public_key"] = {}
        
        u=nextprime(2**key_sizel+2)
        while True:
            vp = getPrime(key_sizet)
            while True:
                vq= getPrime(key_sizet)
                if vq != vp:
                    break
            pb = 2*u*vp
            qb = 2*u*vq
            if key_sizek - pb.bit_length() - qb.bit_length() < 4:
                raise ValueError(
                    f"n_bits is too small, it should be at least {4 + pb.bit_length() + qb.bit_length()}"
                )
            while True:
                pr=getPrime(key_sizek // 2 - pb.bit_length())
                p = pb * pr + 1
                if isPrime(p):
                    break

            while True:
                qr=getPrime(key_sizek // 2 - qb.bit_length()+1)
                if qr==pr:
                    continue
                q = qb * qr + 1 
                if isPrime(q):
                    break
            if (q - 1) % vp == 0 or (p - 1) % vq == 0:
                continue
            
            n=p*q
            if n.bit_length() == key_sizek:
               break
           
        p_min_1_prime_factors = (2, u, vp, pr)
        q_min_1_prime_factors = (2, u, vq, qr)

        # Construct random generators g, h in Z_n^*, such that g has order u * v_p * v_q and h has order v_p * v_q.
        g = DGK.get_composite_generator(p, q, p_min_1_prime_factors, q_min_1_prime_factors)
            
        while True:
            h = DGK.get_composite_generator(p, q, p_min_1_prime_factors, q_min_1_prime_factors)
            if g != h:
                break
        # g and h now both have order  2 * p_random * q_random * v_p * v_q * u
        remove_order_factors = 2 * pr * qr
        g = pow(g, remove_order_factors, n)  # make g of order v_p * v_q * u
        h = pow(h, remove_order_factors * u, n)  # make h of order v_p * v_q
            
        keys["public_key"]["n"] = n
        keys["public_key"]["g"] = g
        keys["public_key"]["h"] = h
        keys["public_key"]["u"] = u

        keys["private_key"]["p"] = p
        keys["private_key"]["q"] = q
        keys["private_key"]["vp"] = vp
        keys["private_key"]["vq"] = vq
        
        return keys
        
    def generate_random_key(self) -> int:
        """
        Generate random key for encryption
        """
        vp = self.keys["private_key"]["vp"]
        return getRandomNBitInteger(int(2.5*vp.bit_length()))

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
        g = self.keys["public_key"]["g"]
        h = self.keys["public_key"]["h"]
        n = self.keys["public_key"]["n"]
        u = self.keys["public_key"]["u"]

        r = random_key or self.generate_random_key()

        if plaintext > u:
            plaintext = plaintext % u
            logger.debug(
                f"Benaloh lets you to encrypt messages in [0, {r=}]."
                f"But your plaintext exceeds this limit."
                f"New plaintext is {plaintext}"
            )

        c = (pow(g, plaintext, n) * pow(h, r, n)) % n

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
        u = self.keys["public_key"]["u"]
        g = self.keys["public_key"]["g"]
        p = self.keys["private_key"]["p"]
        vp = self.keys["private_key"]["vp"]
        vq = self.keys["private_key"]["vq"]
        
        a = pow(ciphertext, vp, p)

        md = u
        while True:
            if pow(g, vp*vq*md, n) == a:
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
        g = self.keys["public_key"]["g"]
        if constant > self.plaintext_modulo:
            constant = constant % self.plaintext_modulo
            logger.debug(
                f"Benaloh can encrypt messages [1, {self.plaintext_modulo}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )
        return (ciphertext*pow(g,constant,n))%n

    def reencrypt(self, ciphertext: int) -> int:
        h = self.keys["public_key"]["h"]
        n = self.keys["public_key"]["n"]
        r=self.generate_random_key()
        return (pow(h,r,n)*ciphertext)%n
    
    @staticmethod
    def extended_euclidean(num_a: int, num_b: int) -> Tuple[int, int, int]:
        """
        Perform the extended euclidean algorithm on the input numbers.
        The method returns gcd, x, y, such that a*x + b*y = gcd.

        :param num_a: First number a.
        :param num_b: Second number b.
            :return: Tuple containing gcd, x, and y, such that  a*x + b*y = gcd.
            """
        # a*x + b*y = gcd
        x_old, x_cur, y_old, y_cur = 0, 1, 1, 0
        while num_a != 0:
            quotient, num_b, num_a = num_b // num_a, num_a, num_b % num_a
            y_old, y_cur = y_cur, y_old - quotient * y_cur
            x_old, x_cur = x_cur, x_old - quotient * x_cur
        return num_b, x_old, y_old
    
    @staticmethod
    def get_composite_generator(
        p: int,
        q: int,
        p_min_1_prime_factors: Iterable[int],
        q_min_1_prime_factors: Iterable[int],
    ) -> int:
        r"""
        Sample a random generator of the non-cyclic group $\mathbb{Z}_n^*$, with $n=p\cdot q$, and $p$, $q$ prime of
        maximum order $\text{lcm}(p - 1, q - 1)$. This algorithm requires the primes $p$ and $q$ and the prime factors
        of $p - 1$ and $q - 1$.

        This is based on Algorithm 4.83 of 'Handbook of Applied Cryptography' by Menzes, Oorschot, and Vanstone.

        :param p: First prime factor of the group modulus $n=p\cdot q$.
        :param q: Second prime factor of the group modulus $n=p\cdot q$.
        :param p_min_1_prime_factors: Prime factors of $p - 1$.
        :param q_min_1_prime_factors: Prime factors of $q - 1$.
        :return: Generator of maximum order $\text{lcm}(p - 1, q - 1)$ from $\mathbb{Z}^*_n$.
        """
        generator_z_p = DGK.get_cyclic_generator(p, p_min_1_prime_factors)
        generator_z_q = DGK.get_cyclic_generator(q, q_min_1_prime_factors)
        _gcd, bezout_coeff_p, bezout_coeff_q = DGK.extended_euclidean(p, q)
        # _gcd is 1, since p and q are both prime
        return (
            generator_z_p * q * bezout_coeff_q + generator_z_q * p * bezout_coeff_p
        ) % (p * q)
            
    @staticmethod
    def get_cyclic_generator(modulus: int, prime_factors: Iterable[int]) -> int:
        r"""
        Given a cylic group with the given modulus, that has order modulus - 1. This function obtains a random generator
        of this cyclic group.
        I.e. the output is the generator of $\mathbb{Z}_p^*$ with the modulus $p$ prime. The order of the group equals
        $p - 1$ and its prime factors are given.

        This is based on Algorithm 4.80 of 'Handbook of Applied Cryptography' by Menzes, Oorschot, and Vanstone.

        :param modulus: Prime modulus of the cyclic group.
        :param prime_factors: Prime factors of modulus - 1.
        :return: Generator of $\mathbb{Z}_p^*$.
        """
        while True:
            generator = random.randint(0,modulus - 1) + 1
            if all(
                map(
                    lambda factor: pow(generator, (modulus - 1) // factor, modulus)
                    != 1,
                    prime_factors,
                )
            ):
                return generator
        
    def isZero(self, ciphertext: int) -> bool:
        p = self.keys["private_key"]["p"]
        vp = self.keys["private_key"]["vp"]
        return pow(ciphertext,vp,p)==1
            