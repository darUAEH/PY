
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

    plaintext = '542#1504891440039'
    encrypted = cipher.encrypt(Mensaje0+Mensaje1+Mensaje2+Mensaje3+Mensaje4+Mensaje5)
    print('Encrypted: %s' % encrypted)
    ciphertext = '1rNHCdmEyyfXREw82sgfs4wzRebrC8HviwGHbrruqq3tybHwyldnG71ginwo8wqzdMX7MLk61qTkiNW29AKrDmZwh48qEmSr/+yJj71OLJeuNjdUpGvSe1poe4c6z5K5ZH6pD142AJwOBUyKP0TBjB1MvhoKMaQ6oeHMSigLmRuURh4b4zywBV2JM4UUIPXyKSwtbZ6yOyQAPLxaxEhPemf/pzq1Jz7YTnnEt5YL69TMXaiSpl7P2hEnPZfYwHuHI1g2yWWs6JkljeKMvtQHfVCloKqpSicT05hd//QJAJD2U7EdSQn3XWtjfyvvzlgRa9i4PadeWJ0EJYcP//fYrw7ILzi02Sr+kFhdr8W3pQs='
    assert encrypted == ciphertext
    
    """
    decrypted = cipher.decrypt(encrypted)
    print('Decrypted: %s' % decrypted)
    assert decrypted == Mensaje0+Mensaje1+Mensaje2+Mensaje3+Mensaje4+Mensaje5
    """