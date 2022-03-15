#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def generate_keys():
    modulus_length = 1024

    key = RSA.generate(modulus_length)
    #print (key.exportKey())

    pub_key = key.publickey()
    #print (pub_key.exportKey())

    return key, pub_key

def encrypt_private_key(a_message, private_key):
    encryptor = PKCS1_OAEP.new(private_key)
    encrypted_msg = encryptor.encrypt(a_message)
    print(encrypted_msg)
    encoded_encrypted_msg = base64.b64encode(encrypted_msg)
    print(encoded_encrypted_msg)
    return encoded_encrypted_msg

def decrypt_public_key(encoded_encrypted_msg, public_key):
    encryptor = PKCS1_OAEP.new(public_key)
    decoded_encrypted_msg = base64.b64decode(encoded_encrypted_msg)
    print(decoded_encrypted_msg)
    decoded_decrypted_msg = encryptor.decrypt(decoded_encrypted_msg)
    print(decoded_decrypted_msg)
    #return decoded_decrypted_msg

def main():
    Mensaje0=b"FLORES RUBIO KAREN                                ~"
    Mensaje1=b"000000~FORK910405AG1~1311910642-8~10675~"
    Mensaje2=b"FORK910405MHGLBR05~0002041.48~0000000.00~0001020.08~"
    Mensaje3=b"0000000.00~0000000.66~0000000.00~0001020.08~"
    Mensaje4=b"0000000.00~0000000.66~0000000.00~0000000.00~"
    Mensaje5=b"0000000.00~0000000.00~0000000.00"



    private, public = generate_keys()
    print (private)
    message = b'Hello world'
    encoded = encrypt_private_key(Mensaje2, public)
    decrypt_public_key(encoded, private)

if __name__== "__main__":
  main()