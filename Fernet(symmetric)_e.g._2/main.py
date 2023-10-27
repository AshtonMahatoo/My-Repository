
# Ashton Mahatoo Sr
# 7/2023


import os
import fileinput
from cryptography.fernet import Fernet



# Fernet uses symmetric encryption where only one key (a secret key) is used to both encrypt and decrypt electronic data. 
# The entities communicating via symmetric encryption must exchange the key so that it can also be used in the decryption process. 

############################################ Start of Encryption #########################################

### This block of code takes in a file from the user 
inputFileName = input(" Please enter the source filename you would like to encrypt!!: ")
inputFile = open(inputFileName, "rb")

read_content = inputFile.read()

# This New_File_Output.txt stores the content of the file entered in the Terminal
with open("New_File_Output.txt", "wb")as file: 
    file.write(read_content)

#file_Input()

###### Creates key ######
key = Fernet.generate_key() 

####### This stores the "Fernet.generate_key()"" in the "key_file.key" file ######
with open('key_file.key', 'wb') as key_file:
    key_file.write(key) 


####### We created the encrypted key and the file to be encrypted above, Now to encrypt the file:

#1 Open the file that contains the key.
#2 Initialize the Fernet object and store it in the fernet variable.
#3 Read the original file.
#4 Encrypt the file and store it into an object.
#5 Then write the encrypted data into the Cipher_Text.encrypted file.


#1
with open('key_file.key', 'rb')as filekey:
    key = filekey.read()


#2
fernet_key = Fernet(key)


#3
with open('New_File_Output.txt','rb')as file:
    original= file.read()

#4
encrypted_file = fernet_key.encrypt(original)

#5
with open('Cipher_Text.encrypted','wb')as encrypted:
    encrypted.write(encrypted_file)


############################################    DECRYPTING FERNET    ######################################################

###### Time to decrypt the Cipher_Text.encrypted file:

#1 Initialize the Fernet object and store it in the fernet variable.
#2 Read the encrypted file.
#3 Decrypt the file and store it into an object.
#4 Then write the decrypted data into the Plain_Text.decrypted file.

#1 
fernet_key = Fernet(key)

#2
with open('Cipher_Text.encrypted','rb')as encr_file:
    encrypted_file = encr_file.read()


#3
decrypted = fernet_key.decrypt(encrypted_file)

#4
with open('Plain_Text.decrypted','wb')as decr_file:
    decr_file.write(decrypted)