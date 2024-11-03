import socket
from des import decrypt

# DES encryption and decryption functions would go here (assuming they are defined)

def start_server():
    key = "12345678"  # Example key for DES
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 65432))
    server_socket.listen()
    print("Server is listening for connections...")

    # Flag to indicate server should shut down
    should_shutdown = False

    while not should_shutdown:
        # Accept a new connection from a client
        client_socket, address = server_socket.accept()
        print(f"Connected to client at {address}")

        while True:
            # Receive the encrypted message
            encrypted_message = client_socket.recv(1024).decode()
            print("Encrypted message received:", encrypted_message)

            # Check if the received message is a "shutdown" command
            if encrypted_message == "shutdown":
                print("Shutdown command received. Server is closing.")
                client_socket.close()
                should_shutdown = True  # Set the shutdown flag to True
                break  # Break out of the inner loop

            elif encrypted_message == "cut":
                print("Cut command received. Closing connection.")
                client_socket.close()
                break  # Break out of the inner loop to close the specific connection

            # Decrypt the message
            decrypted_message = decrypt(encrypted_message, key)
            print("Decrypted message:", decrypted_message)

        # Close the client connection after handling the inner loop
        client_socket.close()

    # Close the server socket after breaking out of the loop
    server_socket.close()
    print("Server has been shut down.")

# Run the server
start_server()
