import rsa 
  
publicKey, privateKey = rsa.newkeys(512) 
  
message = "NTWZMAvZCJQWvSIZMVvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvl"
print("tipo")
print(type(message))
encMessage = rsa.encrypt(message.encode(),  
                         publicKey) 
  
print("original string: ", message) 
print("encrypted string: ", encMessage) 
  
decMessage = rsa.decrypt(encMessage, privateKey).decode() 
  
print("decrypted string: ", decMessage)