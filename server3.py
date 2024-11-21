# server.py
import socket
from des import decrypt
from pka import server_private_key
import rsa

def start_server():
    key_received = None

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen()
    print("Server is listening for connections...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected to client at {address}")

        # Receive the encrypted DES key from the client
        encrypted_key = client_socket.recv(1024)
        print("Encrypted key received:", encrypted_key)
        decrypted_key = rsa.decrypt(encrypted_key, server_private_key).decode('utf-8')
        print("DES key received and decrypted:", key_received)

        while True:
            encrypted_message = client_socket.recv(1024).decode()

            if encrypted_message == "shutdown":
                print("Shutdown command received. Server is closing.")
                client_socket.close()
                server_socket.close()
                return

            elif encrypted_message == "cut":
                print("Cut command received. Closing connection.")
                client_socket.close()
                break

            decrypted_message = decrypt(encrypted_message, key_received)
            print("Decrypted message:", decrypted_message)

        client_socket.close()

if __name__ == "__main__":
    start_server()
