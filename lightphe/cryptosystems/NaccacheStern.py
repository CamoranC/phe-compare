"""
Original from Light-PHE by serengil at: https://github.com/serengil/LightPHE.
Modified Key Generation, decryption and changed reencryption to rerandomization.
"""
import random
from typing import Optional
import math
import sympy
from sympy import nextprime
from sympy.ntheory.modular import crt
from lightphe.models.Homomorphic import Homomorphic
from lightphe.commons.logger import Logger
from Crypto.Util.number import getPrime
from Crypto.Util.number import isPrime

logger = Logger(module="lightphe/cryptosystems/NaccacheStern.py")

# pylint: disable=simplifiable-if-expression, consider-using-enumerate


class NaccacheStern(Homomorphic):
    """
    Naccache-Stern algorithm is homomorphic with respect to the addition.
    It is a generaliation of Benaloh cryptosystem
    Ref: https://sefiks.com/2023/10/26/a-step-by-step-partially-homomorphic-encryption-example-with-naccache-stern-in-python/
    Original paper: https://dl.acm.org/doi/pdf/10.1145/288090.288106
    """

    def __init__(self, keys: Optional[dict] = None, key_sizen: int=1024, key_sizes: int=160, deterministic: bool = False):
        """
        Args:
            keys (dict): private - public key pair.
                set this to None if you want to generate random keys.
            key_size (int): key size in bits. Less than many cryptosystems because
                decryption requires to solve DLP.
            deterministic (boolean): deterministic or probabilistic version of
                cryptosystem
        """
        self.keys = keys or self.generate_keys(key_sizen, key_sizes)
        self.plaintext_modulo = self.keys["public_key"]["sigma"]
        self.ciphertext_modulo = self.keys["public_key"]["n"]
        self.deterministic = deterministic

    def generate_keys(self, key_sizen: int, key_sizes: int) -> dict:
        """
        Generate public and private keys of Naccache-Stern cryptosystem
        Args:
            key_size (int): key size in bits
        Returns:
            keys (dict): having private_key and public_key keys
        """
        keys = {}
        keys["private_key"] = {}
        keys["public_key"] = {}

        # pick a family of small primes. the largest one is 10-bits
        # TODO: do something generic instead of constant primes
        prime_set = []
        sigma=1
        prime=2
        while sigma.bit_length() < key_sizes:
            #bit=random.randint(2,10)
            pi=nextprime(prime)
            #pi=getPrime(bit)
            prime=pi+1
            #if pi in prime_set:
                #continue
            prime_set.append(pi)
            sigma=sigma*pi
        k = len(prime_set)
        if k%2 != 0:
            pi=nextprime(prime)
            prime_set.append(pi)
            sigma=sigma*pi
            k = len(prime_set)
        #print(prime_set)
        #print(sigma.bit_length())
        if all(sympy.isprime(prime) is True for prime in prime_set) is False:
            raise ValueError("All items of prime set must be prime!")
        #print(sigma.bit_length())
        # divide the set in half and find products of primes
        u = 1
        v = 1

        for i, prime in enumerate(prime_set):
            if i < len(prime_set) / 2:
                u = u * prime
            else:
                v = v * prime

        # product of all primes
        #sigma = u * v

        # pick large prime numbers
        bita=(key_sizen // 2)-u.bit_length()-24
        bitb=(key_sizen // 2)-v.bit_length()-24
        # calculate two primes from chosen ones
       
        a = getPrime(bita)
        b = getPrime(bitb)
        #print(f"a={a}")
        #print(f"b={b}")
        #print(f"u={u}")
        #print("v={v}")
        while True:
            while True:
                ptp=getPrime(24)
                p=2*a*u*ptp+1
                if isPrime(p):
                    break
            #print(p-1)
            while True:
               qtp=getPrime(24) 
               q=2*b*v*qtp+1
               if isPrime(q):
                    break
            if ptp==qtp or math.gcd(ptp*qtp,sigma)!=1:
                continue
            n = p * q
            if n.bit_length()!=key_sizen:
                bita=(key_sizen // 2)-u.bit_length()-24
                bitb=(key_sizen // 2)-v.bit_length()-24
                # calculate two primes from chosen ones
               
                a = getPrime(bita)
                b = getPrime(bitb)
                continue
            #print(n.bit_length())    
            phi = (p - 1) * (q - 1)

            if phi % sigma != 0:
                logger.debug("canceled because phi cannot be divisible by sigma")
                continue

            if math.gcd(sigma, phi // sigma) != 1:
                logger.debug("canceled because sigma and phi/sigma are not coprime")
                continue

            p_conditions = []
            for i in range(0, k // 2):
                pi = prime_set[i]
                if (
                    (p - 1) % pi == 0
                    and math.gcd(pi, (p - 1) // pi) == 1
                    and math.gcd(pi, q - 1) == 1
                ):
                    p_conditions.append(1)
                else:
                    p_conditions.append(0)
            p_satisfied = True if len(p_conditions) == sum(p_conditions) else False
            if p_satisfied is False:
                logger.debug("canceled because p_conditions are not satisfied")
                continue

            q_conditions = []
            for i in range(k // 2, k):
                pi = prime_set[i]
                if (
                    (q - 1) % pi == 0
                    and math.gcd(pi, (q - 1) // pi) == 1
                    and math.gcd(pi, p - 1)
                ):
                    q_conditions.append(1)
                else:
                    q_conditions.append(0)

            q_satisfied = True if len(q_conditions) == sum(q_conditions) else False
            if q_satisfied is False:
                logger.debug("canceled because q_conditions are not satisfied")
                continue
            break
            # p and q must be primes
            #if not (sympy.isprime(p) and sympy.isprime(q)):
                #continue
        while True:
            # choose a generator g
            g = random.randint(2, n-1)
            #it must be co-prime to n
            if math.gcd(g, n) != 1:
                logger.debug("canceled becuase g is not co-prime with ne")
                continue
            # the order of g modulo n must be phi/4
            if pow(g, phi // 4, n) != 1:
                continue
            # guarantee it is not pi-th power.
            power=False
            for pi in prime_set:
                #logger.debug("canceled because g is a pi-th power")
                if pow(g, phi // pi, n) == 1:
                    power=True
                    break
            if power==True:
                continue
            else:
                break

            

            # check decryption is guaranteed similar to benaloh
            # ps: this is not mentioned in the original paper
            #is_decryption_guaranteed = True
            #for pi in prime_set:
               # prime_factors = sympy.factorint(pi).keys()
                #for prime_factor in prime_factors:
                   #if pow(g, int(phi / prime_factor), n) == 1:
                       # is_decryption_guaranteed = False
            #if is_decryption_guaranteed is True:
                #break

        logger.debug(f"n bits is {len(bin(n)[2:])}")

        keys["public_key"]["g"] = g
        keys["public_key"]["n"] = n
        # sigma can optionally be secret in deterministic version
        keys["public_key"]["sigma"] = sigma

        keys["private_key"]["p"] = p
        keys["private_key"]["q"] = q
        #keys["private_key"]["phi"] = phi
        keys["private_key"]["prime_set"] = prime_set

        return keys

    def generate_random_key(self) -> int:
        """
        Naccache-Stern requires to generate one-time random key per encryption
        Returns:
            random key (int): one time random key for encryption
        """
        n = self.keys["public_key"]["n"]
        return random.randint(1, n - 1)

    def encrypt(self, plaintext: int, random_key: Optional[int] = None) -> int:
        """
        Encrypt a given plaintext for optionally given random key with Naccache-Stern
        Args:
            plaintext (int): message to encrypt
            random_key (int): Naccache-Stern requires a random key
                Random key will be generated automatically if you do not set this.
        Returns:
            ciphertext (int): encrypted message
        """
        g = self.keys["public_key"]["g"]
        n = self.keys["public_key"]["n"]
        if self.deterministic is False:
            r = random_key or self.generate_random_key()
        sigma = self.keys["public_key"]["sigma"]
        if plaintext > self.plaintext_modulo:
            plaintext = plaintext % self.plaintext_modulo
            logger.debug(
                f"plaintext must be in scale [0, {self.plaintext_modulo}] "
                "but this is exceeded. New plaintext is {plaintext}"
            )

        if self.deterministic is True:
            return pow(g, plaintext, n)

        # Probabilistic
        return (pow(r, sigma, n) * pow(g, plaintext, n)) % n

    def decrypt(self, ciphertext: int):
        """
        Decrypt a given ciphertext with Naccache-Stern
        Args:
            ciphertext (int): encrypted message
        Returns:
            plaintext (int): restored message
        """
        p = self.keys["private_key"]["p"]
        q = self.keys["private_key"]["q"]
        n = self.keys["public_key"]["n"]
        g = self.keys["public_key"]["g"]
        sigma = self.keys["public_key"]["sigma"]
        prime_set = self.keys["private_key"]["prime_set"]

        phi=(q-1)*(p-1)
        remainders = []
        for i, prime in enumerate(prime_set):
            ci = pow(ciphertext, phi // prime, n)
            logger.debug(f"c_{i} = {ci}")

            j = 0
            while True:
                if ci == pow(g, (j * phi) // prime, n):
                    logger.debug(f"m_{i} = {j}")
                    remainders.append(j)
                    break
                j = j + 1
                if j > prime-1:
                    raise ValueError(
                        f"c_{i} cannot be restored from {ci} = {g}^(j*{phi}/{prime}) mod {n}"
                    )
        #congruences = []
        #for i in range(0, len(prime_set)):
            #logger.debug(f"m mod {prime_set[i]} = {remainders[i]}")
            #congruences.append((remainders[i], prime_set[i]))

        # chinese remainder problem
        ms = crt(prime_set,remainders,False,False)
        if not ms:
            raise ValueError("message cannot be restored with Chinese Remainder!")
        return ms[0]

    def add(self, ciphertext1: int, ciphertext2: int) -> int:
        """
        Perform homomorphic addition on encrypted data.
        Result of this must be equal to E(m1 + m2)
        Encryption calculations are done in module n
        Args:
            ciphertext1 (int): 1st ciphertext created with Naccache-Stern
            ciphertext2 (int): 2nd ciphertext created with Naccache-Stern
        Returns:
            ciphertext3 (int): 3rd ciphertext created with Naccache-Stern
        """
        return (ciphertext1 * ciphertext2) % self.ciphertext_modulo

    def multiply(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Naccache-Stern is not homomorphic with respect to the multiplication")

    def xor(self, ciphertext1: int, ciphertext2: int) -> int:
        raise ValueError("Naccache-Stern is not homomorphic with respect to the exclusive or")

    def multiply_by_contant(self, ciphertext: int, constant: int) -> int:
        """
        Multiply a ciphertext with a plain constant.
        Result of this must be equal to E(m1 * constant) where E(m1) = ciphertext
        Encryption calculations are done in module n squared.
        Args:
            ciphertext (int): ciphertext created with Naccache-Stern
            constant (int): known plain constant
        Returns:
            ciphertext (int): new ciphertext created with Naccache-Stern
        """
        if constant > self.plaintext_modulo:
            constant = constant % self.plaintext_modulo
            logger.debug(
                f"Naccache-Stern can encrypt messages [1, {self.plaintext_modulo}]. "
                f"Seems constant exceeded this limit. New constant is {constant}"
            )

        return pow(ciphertext, constant, self.ciphertext_modulo)
    
    def add_with_constant(self, ciphertext: int, constant: int) -> int:
        constant = constant % self.plaintext_modulo
        logger.debug(
            f"Naccache-Stern can encrypt messages [1, {self.plaintext_modulo}]. "
            f"Seems constant exceeded this limit. New constant is {constant}"
        )
        g=self.keys["public_key"]["g"]
        return ((ciphertext*pow(g,constant,self.ciphertext_modulo))%self.ciphertext_modulo)

    def reencrypt(self, ciphertext: int) -> int:
        """
        Re-generate ciphertext with re-encryption. Many ciphertext will be decrypted to same plaintext.
        Args:
            ciphertext (int): given ciphertext
        Returns:
            new ciphertext (int): different ciphertext for same plaintext
        """
        if self.deterministic is True:
            raise ValueError(
                "Deterministic version of Naccache-Stern does not support reencryption."
                "If you still want to perform ciphertext regeneration, then you may "
                "consider to use its probabilistic version."
            )
        #neutral_element = 0
        #neutral_encrypted = self.encrypt(plaintext=neutral_element)
        #return self.add(ciphertext1=ciphertext, ciphertext2=neutral_encrypted)
        n = self.keys["public_key"]["n"]
        sigma = self.keys["public_key"]["sigma"]
        while True:
            x=self.generate_random_key()
            if math.gcd(x,n)==1:
                break
        return (pow(x,sigma,n)*ciphertext)%n
