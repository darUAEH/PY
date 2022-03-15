
import sys
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw.encode())
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]


if __name__ == '__main__':

    Mensaje0="FLORES RUBIO KAREN                                ~"
    Mensaje1="000000~FORK910405AG1~1311910642-8~10675~"
    Mensaje2="FORK910405MHGLBR05~0002041.48~0000000.00~0001020.08~"
    Mensaje3="0000000.00~0000000.66~0000000.00~0001020.08~"
    Mensaje4="0000000.00~0000000.66~0000000.00~0000000.00~"
    Mensaje5="0000000.00~0000000.00~0000000.00"


    key = b'xwibsSiSdDRbOeDe'
    cipher = AESCipher(key)

    encrypted0 = cipher.encrypt(Mensaje0)
    encrypted1 = cipher.encrypt(Mensaje1)
    encrypted2 = cipher.encrypt(Mensaje2)
    encrypted3 = cipher.encrypt(Mensaje3)
    encrypted4 = cipher.encrypt(Mensaje4)
    encrypted5 = cipher.encrypt(Mensaje5)


    print('Encrypted0: %s' % encrypted0)
    print('Encrypted1: %s' % encrypted1)
    print('Encrypted2: %s' % encrypted2)
    print('Encrypted3: %s' % encrypted3)
    print('Encrypted4: %s' % encrypted4)
    print('Encrypted5: %s' % encrypted5)

    cadena = encrypted0+"*"+encrypted1+"*"+encrypted2+"*"+encrypted3+"*"+encrypted4+"*"+encrypted5
    cadena_bytes = cadena.encode('ascii')
    base64_bytes = base64.b64encode(cadena_bytes)
    print("*********************")
    print(base64_bytes)
    base64_message = base64_bytes.decode('ascii')
    print("*********************")
    base64_bytes_ = base64_message.encode('ascii')
    message_bytes_ = base64.b64decode(base64_bytes_)
    message_ = message_bytes_.decode('ascii')


    print(message_)
    print("*********************")
    mensajes = message_.split('*')

    men0 = mensajes[0]
    men1 = mensajes[1]
    men2 = mensajes[2]
    men3 = mensajes[3]
    men4 = mensajes[4]
    men5 = mensajes[5]

    print('Decrypted0: %s' % men0)
    print('Decrypted1: %s' % men1)
    print('Decrypted2: %s' % men2)
    print('Decrypted3: %s' % men3)
    print('Decrypted4: %s' % men4)
    print('Decrypted5: %s' % men5)

    me0=cipher.decrypt(men0)
    me1=cipher.decrypt(men1)
    me2=cipher.decrypt(men2)
    me3=cipher.decrypt(men3)
    me4=cipher.decrypt(men4)
    me5=cipher.decrypt(men5)

    print('Decrypted0: %s' % me0)
    print('Decrypted1: %s' % me1)
    print('Decrypted2: %s' % me2)
    print('Decrypted3: %s' % me3)
    print('Decrypted4: %s' % me4)
    print('Decrypted5: %s' % me5)

    

    #ciphertext = '1rNHCdmEyyfXREw82sgfs4wzRebrC8HviwGHbrruqq3tybHwyldnG71ginwo8wqzdMX7MLk61qTkiNW29AKrDmZwh48qEmSr/+yJj71OLJeuNjdUpGvSe1poe4c6z5K5ZH6pD142AJwOBUyKP0TBjB1MvhoKMaQ6oeHMSigLmRuURh4b4zywBV2JM4UUIPXyKSwtbZ6yOyQAPLxaxEhPemf/pzq1Jz7YTnnEt5YL69TMXaiSpl7P2hEnPZfYwHuHI1g2yWWs6JkljeKMvtQHfVCloKqpSicT05hd//QJAJD2U7EdSQn3XWtjfyvvzlgRa9i4PadeWJ0EJYcP//fYrw7ILzi02Sr+kFhdr8W3pQs='
    #assert encrypted == ciphertext

    """
    decrypted = cipher.decrypt(encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == Mensaje0+Mensaje1+Mensaje2+Mensaje3+Mensaje4+Mensaje5
    """