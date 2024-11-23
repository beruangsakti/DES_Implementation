# server.py
import socket
from des import decrypt
from pka import server_private_key
import rsa
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def start_server():
    key_received = None
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen()
    print("Server is listening for connections...")

    try:
        while True:
            client_socket, address = server_socket.accept()
            print(f"Connected to client at {address}")

            try:
                # Receive the encrypted DES key
                encrypted_key = client_socket.recv(1024)
                if not encrypted_key:
                    print("No key received, closing connection.")
                    client_socket.close()
                    continue

                print("Encrypted key received:", encrypted_key)

                # Decrypt DES key using the server's private RSA key
                key_received = RSA.decrypt(encrypted_key, server_private_key).decode('utf-8')
                print("DES key received and decrypted:", key_received)

                while True:
                    # Receive encrypted messages
                    encrypted_message = client_socket.recv(1024)
                    if not encrypted_message:
                        print("Client disconnected.")
                        break

                    command = encrypted_message.decode()
                    if command == "shutdown":
                        print("Shutdown command received. Server is closing.")
                        client_socket.send("Server shutting down.".encode())
                        client_socket.close()
                        return
                    elif command == "cut":
                        print("Cut command received. Closing connection.")
                        client_socket.close()
                        break

                    # Decrypt and display the message
                    decrypted_message = decrypt(encrypted_message, key_received)
                    print("Decrypted message:", decrypted_message)

            except Exception as e:
                print(f"Error during communication: {e}")
            finally:
                client_socket.close()

    except Exception as e:
        print(f"Server error: {e}")
    finally:
        server_socket.close()
        print("Server has been shut down.")

if __name__ == "__main__":
    start_server()
