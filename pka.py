# pka.py
import rsa

# Generate public and private keys for both server and client
server_public_key, server_private_key = rsa.newkeys(1024)
client_public_key, client_private_key = rsa.newkeys(1024)

# Function to simulate PKA
def get_public_key(identifier):
    if identifier == "server":
        return server_public_key
    elif identifier == "client":
        return client_public_key
    else:
        raise ValueError("Unknown identifier")

# import rsa

# # Generate keys
# server_public_key, server_private_key = rsa.newkeys(1024)

# # DES key
# des_key = '12345678'
# print("DES Key:", des_key)

# # Encrypt
# print("Server Public Key:", server_public_key)
# encrypted_key = rsa.encrypt(des_key.encode('utf-8'), server_public_key)
# print("Encrypted DES Key:", encrypted_key)

# # Decrypt
# try:
#     print("Server Private Key:", server_private_key)
#     decrypted_key = rsa.decrypt(encrypted_key, server_private_key).decode('utf-8')
#     print("Decrypted DES Key:", decrypted_key)
# except rsa.pkcs1.DecryptionError as e:
#     print("Decryption failed:", e)
