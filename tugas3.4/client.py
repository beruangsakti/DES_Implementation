import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from des import encrypt  # Ensure this is your DES implementation

# Hardcoded DES key (you could generate this dynamically instead)
DES_KEY = "12345678"

def load_public_key():
    # Load the public key
    with open("public_key.pem", "rb") as public_file:
        return RSA.import_key(public_file.read())

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    # Load public key from file
    rsa_public_key = load_public_key()
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)

    # Encrypt the hardcoded DES key
    encrypted_des_key = cipher_rsa.encrypt(DES_KEY.encode())
    client.send(encrypted_des_key)
    print("Encrypted DES key sent to server.")

    # Input message (more than 8 characters)
    message = input("Enter a message to send: ")

    # Encrypt the message using the DES key
    encrypted_message = encrypt(message, DES_KEY)
    print(f"Encrypted message: {encrypted_message}")

    # Send the encrypted message to the server
    client.send(encrypted_message.encode())
    print("Encrypted message sent.")

    client.close()

if __name__ == "__main__":
    client_program()
