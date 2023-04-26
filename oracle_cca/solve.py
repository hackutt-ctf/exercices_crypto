from pwn import *
from Crypto.Util.number import long_to_bytes, bytes_to_long

def send_to_oracle(i):
    io.sendlineafter(b'> ', long_to_bytes(i).hex().encode())


io = remote('localhost', 8080)

## Récupération de la clé publique
io.recvuntil(b'N=')
N = int(io.recvline())

io.recvuntil(b'E=')
E = int(io.recvline())

io.recvuntil(b'c=')
c = int(io.recvline(),16)

# On envoie c*2^e
send_to_oracle(c*pow(2,E,N))

# On récupère 2*M
io.recvuntil(b'is: ')
m = int(io.recvline(),16)

print(long_to_bytes(m//2))