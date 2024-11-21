# client.py
import socket
from des import encrypt
from pka import get_public_key
import rsa

def client_program():
    host = '127.0.0.1'
    port = 65432
    des_key = '12345678'  # DES key

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    # Retrieve server's public key from PKA
    server_public_key = get_public_key("server")

    # Encrypt the DES key with the server's public key and send it
    encrypted_des_key = rsa.encrypt(des_key.encode('utf-8'), server_public_key)
    client_socket.send(encrypted_des_key)
    print("Encrypted key sent:", encrypted_des_key)

    print("DES key encrypted and sent.")

    while True:
        plaintext = input("Enter message to encrypt and send (or 'shutdown' to close): ")

        if plaintext == "shutdown":
            client_socket.send("shutdown".encode())
            break

        encrypted_message = encrypt(plaintext, des_key)
        client_socket.send(encrypted_message.encode())
        print("Encrypted message sent. (" + encrypted_message + ")")

    client_socket.close()
    print("Client closed.")

if __name__ == "__main__":
    client_program()
