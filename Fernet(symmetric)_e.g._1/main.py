
"""
# by: Ashton Mahatoo
# 7/23

This is example of Symmetric Key Encryption using the Cryptography Module in Python!!
We will be performing encryption and decryption on date. 
"""

# We are importing the Fernet class.
from cryptography.fernet import Fernet

#We are creating an encryption key and storing it in the variable "symmetric_key"
symmetric_key = Fernet.generate_key()

# This "fernet_key" variable will store an instance of the "symmetric_key" variable created eariler.  
fernet_key = Fernet(symmetric_key)

#The encrypt() method is used to encode the message and store the output in the "message_for_encryption" variable. 
#This message is stored in bites and represented in ASCii code 
encrypted_message = fernet_key.encrypt(b"This is the message we are going to encrypt and decrypt!!")

#This will decrypt() the message above. 
decrypted_message = fernet_key.decrypt(encrypted_message)

#This will decode() the decrypted_message from ASCII code to human readable words. 
origional_message = decrypted_message.decode()

print("This is the original message: ", origional_message)
print("\nThis is the encrypted_message : ", encrypted_message)
print("\nThis in the decrypted_message : ", decrypted_message)



