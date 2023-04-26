from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long, long_to_bytes
import socket
import threading
import string

FLAG = open('flag.txt','r').read().strip().encode()
printable_chars = set(bytes(string.printable, 'ascii'))

def is_printable(m):
    return all(char in printable_chars for char in m)

def RSA_encrypt(m,e,n):
    m = bytes_to_long(m)
    return long_to_bytes(pow(m, e,n))

def RSA_decrypt(m, d, n):
    m = bytes_to_long(m)
    return long_to_bytes(pow(m, d,n))

def thread_function(s, address):

    key = RSA.generate(1024)
    encryptor = PKCS1_OAEP.new(key.public_key())
    encrypted = encryptor.encrypt(FLAG)

    decryptor = PKCS1_OAEP.new(key)

    enc_flag_hex = RSA_encrypt(FLAG, key.public_key().e, key.public_key().n).hex()

    print(f"Received client {address}")
    s.send(f'Public key :\nN={key.public_key().n}\nE={key.public_key().e}\n'.encode())
    s.send(f'c={enc_flag_hex}\n\n'.encode())
    s.send(f"Give encrypted message (in hex format) and I will decrypt it\nExample: {encryptor.encrypt(b'toto').hex()}\n".encode())

    data = b' '
    while data != b'':
        s.send(b'\n> ')
        data = s.recv(1024).decode().strip()
        print(data)
        if data == enc_flag_hex:
            s.send(b"Sorry h4cker, I'm smarter than you think ;)\n")
        else:
            try:
                data = bytes.fromhex(data)
                data = RSA_decrypt(data, key.d, key.public_key().n)
                if is_printable(data):
                    s.send(f'The decrypted content is: {data.decode()}\n'.encode())
                else:
                    s.send(f'The decrypted content is: {data.hex()}\n'.encode())
            except Exception as e:
                s.send(b'Invalid hex format\n')
                print(e)


if __name__=="__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('0.0.0.0',8080))

    s.listen(0)

    while True:
        (clientSocket, address) = s.accept()
        x = threading.Thread(target=thread_function, args=(clientSocket,address))
        x.start()