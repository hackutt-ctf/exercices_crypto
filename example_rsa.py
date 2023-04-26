from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

def gcdExtended(a, b):
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
     
    return gcd,x,y

def modinv(a, m):
    g, x, y = gcdExtended(a, m)
    if g != 1:
        raise ValueError('Modular inverse does not exist.')
    else:
        return x % m

def gen_RSA_keys():
    # Création de P et Q, deux nombres
    P = getPrime(20)
    Q = getPrime(20)
    assert P != Q, "P et Q ne peuvent pas être égaux"

    N = P * Q
    phi = (P-1) * (Q-1)

    # e doit être inférieur à phi(n) et premier avec lui
    # un nombre premier est premier avec n'importe quel nombre donc on choisis e premier
    E = 65537
    assert E < phi, "E doit être inférieur à phi"

    D = modinv(E,phi)

    return ((E,N),(D))

def RSA_crypt(E,N,M):
    assert M < N, "Le message doit être inférieur à N"

    C = pow(M,E,N)

    return C

def RSA_decrypt(C, D, N):
    return pow(C, D, N)

public_key, private_key = gen_RSA_keys()
E, N = public_key
D = private_key

print(f"[+] Public key :\n\t- E = {E}\n\t- N = {N}")
print(f"[+] Private key :\n\t- D = {D}")
print()

M = b'toto'
print(f"[+] Chiffrement du message : {M}")

C = RSA_crypt(E, N, bytes_to_long(M))
print(f"[+] Message chiffré: {C}")

assert bytes_to_long(M) == RSA_decrypt(C, D, N), "Le déchiffrement s'est mal passé"