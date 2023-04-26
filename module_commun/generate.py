from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

def gen_RSA_keys():
    # Création de P et Q, deux nombres
    P = getPrime(512)
    Q = getPrime(512)
    assert P != Q, "P et Q ne peuvent pas être égaux"

    N = P * Q

    e1 = 65537
    e2 = 71


    return e1, e2, N

def RSA_crypt(E,N,M):
    assert M < N, "Le message doit être inférieur à N"

    C = pow(M,E,N)

    return C

def RSA_decrypt(C, D, N):
    return pow(C, D, N)

e1, e2, N = gen_RSA_keys()

print(f"{e1 = }\n{e2 = }\n{N = }")
print()

M = b'HackUTT{C0mmon_M0dulus}'
print(f"[+] Chiffrement du message : {M}")

c1 = RSA_crypt(e1, N, bytes_to_long(M))
c2 = RSA_crypt(e2, N, bytes_to_long(M))
print(f"[+] Message chiffré: \n{c1 = }\n{c2 = }")
