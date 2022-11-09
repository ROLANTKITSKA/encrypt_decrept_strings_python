from cryptography.fernet import Fernet

text="hello world"

#generate a key
key=Fernet.generate_key()

#Instance the Fernet class with the key
fernet=Fernet(key)

#use the fernet class to encrypt the string
encText=fernet.encrypt(text.encode())

print("original string: ",text)
print("encrypted string: ",encText)

#decrypt the encrypted key with the Fernet instance of the key
decText=fernet.decrypt(encText).decode()
print("decrypted string: ",decText)
