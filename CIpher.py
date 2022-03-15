from email import message
from Crypto.Cipher import AES
import rsa 

 
#revisa las funciones definidas arriba
#Variables de configuracion
shift = 8
PublicKey = "sWdMGo"
PrivateKey = "TblmbR"

rsa.PrivateKey=PrivateKey
rsa.PublicKey=PublicKey

publicKey, privateKey = rsa.newkeys(512) 

Mensaje0="FLORES RUBIO KAREN                                ~"
Mensaje1="000000~FORK910405AG1~1311910642-8~10675~"
Mensaje2="FORK910405MHGLBR05~0002041.48~0000000.00~0001020.08~"
Mensaje3="0000000.00~0000000.66~0000000.00~0001020.08~"
Mensaje4="0000000.00~0000000.66~0000000.00~0000000.00~"
Mensaje5="0000000.00~0000000.00~0000000.00"

Mensaje0Codificado= rsa.encrypt(Mensaje0.encode(),publicKey) 
print(Mensaje0Codificado)


