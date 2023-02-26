import math
from BitVector import *
import time

def genprimenumber(k):
    a=1
    while a==1 :
        b = BitVector(intVal=0)
        b = b.gen_rand_bits_for_prime(int(k/2))
        check = b.test_for_primality()
        #print(check)
        if check > 0.99:
            return b.get_bitvector_in_hex()

def find_e(phi_n):
    for i in range(3,phi_n):
        if math.gcd(i,phi_n) == 1:
            return i
    return 0

def find_d(phi_n, e):
    b1 = BitVector(intVal=e)
    b2 = BitVector(intVal=phi_n)
    b3 = b1.multiplicative_inverse(b2)
    if b3 is not None:
        return int(b3)
    else:
        print("No MI")
        return 0

def keyGeneration(k):
    #print(k)
    p = int(genprimenumber(int(k)), 16)
    q = int(genprimenumber(int(k)), 16)
    #print("p is : ", p)
    #print("q is : ", q)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = find_e(phi_n)
    d = find_d(phi_n, e)
    #print("e is : ", e)
    #print("d is : ", d)
    public_key = (e, n)
    private_key = (d, n)
    #print(public_key)
    #print(private_key)
    keys = (public_key,private_key)
    return keys


def rsaEncryption(plain_text,e,n):
    list=[]
    for i in range(0,len(plain_text)):
        c = pow(ord(plain_text[i]),e,n)
        list.append(c)
    return list

def rsaDecryption(ciphertext,d,n):
    str=""
    for i in range(0,len(ciphertext)):
        p = pow(ciphertext[i],d,n)
        #print(chr(p))
        str = str + chr(p)
    return str

def rsaImplementation():
    k = input("Enter the value of K : ")
    plain_text = input("Enter the plain text : ")
    #print(k)
    #print(plain_text)
    print()
    print("Plain Text : ", plain_text)
    start = time.perf_counter_ns()
    keys = keyGeneration(k)
    end = time.perf_counter_ns()
    n = keys[0][1]
    e = keys[0][0]
    d = keys[1][0]
    start2 = time.perf_counter_ns()
    ciphertext = rsaEncryption(plain_text,e,n)
    end2 = time.perf_counter_ns()

    print("CipherText is : ")
    print(ciphertext)
    start3 = time.perf_counter_ns()
    decypher_text = rsaDecryption(ciphertext,d,n)
    end3 = time.perf_counter_ns()
    print("Deciphered Text : ")
    print(decypher_text)
    print()
    print("Key generation time : ", end - start, " ns")
    print("Encryption time : ", end2 - start2, " ns")
    print("Decryption time : ", end3 - start3, " ns")


if __name__ == '__main__':
    rsaImplementation()