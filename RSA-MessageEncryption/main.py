
"""
Ashton Mahatoo
8/23

This sample code is an example of asymmetric cryptography using the RSA algorithm in python. 
RSA will generate two different keys,a Public Key which will be openly available to anyone for 
the encryption of data, and a Private key which will be used for decryption of data and needs 
to be kept private by its owner.

"""
import rsa , os


# This block of code creates a new public.pem and private.pem files!!


public_key, private_key = rsa.newkeys(1024)

with open("public_key.pem", "wb") as file:
    file.write(public_key.save_pkcs1("PEM"))

with open("private_key.pem", "wb") as file:
    file.write(private_key.save_pkcs1("PEM"))


with open("public_key.pem", "rb")as file:
    public_key = rsa.PublicKey.load_pkcs1(file.read())

with open("private_key.pem", "rb") as file:
    private_key = rsa.PrivateKey.load_pkcs1(file.read())


# Message to encrypt below!!
user_plain_text_message = input (b"Enter a message to be encrypted!!")

# Encrypt the plain text message below!!
encrypted_message = rsa.encrypt(user_plain_text_message.encode(), public_key)

# This line of code prints the encrypted messageprint(encrypted_plain_text_message)
with open("encrypted_plain_text_message.txt", "wb") as file:
    file.write(encrypted_message)

decrypted_message = rsa.decrypt(encrypted_message, private_key)
with open("decrypted_message.txt", "wb") as file:
    file.write(decrypted_message)
