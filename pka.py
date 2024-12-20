# pka.py
import rsa

# Generate or load RSA keys
server_public_key, server_private_key = rsa.newkeys(1024)
client_public_key, client_private_key = rsa.newkeys(1024)

def get_public_key(identifier):
    if identifier == "server":
        return server_public_key
    elif identifier == "client":
        return client_public_key
    else:
        raise ValueError("Unknown identifier")
