import random
max_PrimLength = 1000000000000


## calculates the modular inverse from e and phi

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def gcd(a, b):               # #   calculates the gcd of two ints
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(num):           ## checks if a number is a prime
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    print("n =",n)          # # phi(n) = phi(p)*phi(q)
    
    phi = (p-1) * (q-1) 
    print("phi =",phi)
    
        
    e = random.randint(1, phi)    # # '''choose e coprime to n and 1 > e > phi
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e =",e)
    
    d = egcd(e, phi)[1]         #  # d[1] = modular inverse of e and phi
    
    d = d % phi    # # make sure d is positive
    if(d < 0):
        d += phi
        
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

if __name__ == '__main__':
    public_key,private_key = generate_keyPairs() 
    print("Public: ",public_key)
    print("Private: ",private_key)
    
    ctext = encrypt("AliceBobJohn",public_key)
    print("encrypted Text =",ctext)
    plaintext = decrypt(ctext, private_key)
    print("decrypted TEXT  =",plaintext)
  