# client.py
import socket
from des import encrypt
from pka import get_public_key
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def client_program():
    host = '127.0.0.1'
    port = 65432
    des_key = '12345678'  # DES key (must be 8 characters)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    try:
        # Retrieve server's public key
        server_public_key = get_public_key("server")

        # Encrypt DES key with RSA
        encrypted_des_key = RSA.encrypt(des_key.encode('utf-8'), server_public_key)
        client_socket.send(encrypted_des_key)
        print("DES key encrypted and sent:", encrypted_des_key)

        while True:
            plaintext = input("Enter message to encrypt and send (or 'shutdown' to close, 'cut' to disconnect): ")

            if plaintext in ["shutdown", "cut"]:
                client_socket.send(plaintext.encode())
                break

            # Encrypt the message with DES
            encrypted_message = encrypt(plaintext, des_key)
            client_socket.send(encrypted_message)
            print("Encrypted message sent:", encrypted_message)

    except Exception as e:
        print(f"Client error: {e}")
    finally:
        client_socket.close()
        print("Client closed.")

if __name__ == "__main__":
    client_program()
