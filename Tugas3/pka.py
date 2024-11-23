# pka.py
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# Generate or load RSA keys
server_public_key, server_private_key = RSA.newkeys(1024)
client_public_key, client_private_key = RSA.gennewkeyserate(1024)

def get_public_key(identifier):
    if identifier == "server":
        return server_public_key
    elif identifier == "client":
        return client_public_key
    else:
        raise ValueError("Unknown identifier")
