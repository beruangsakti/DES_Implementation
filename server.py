import socket
from des import decrypt  # Import your DES decryption function

def server_program():
    host = '127.0.0.1'  # Server IP
    port = 65432        # Server port
    key = '12345678'    # 64-bit key (8 characters)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print("Waiting for connection...")
    conn, address = server_socket.accept()  # Accept new connection
    print(f"Connection from {address} established.")

    encrypted_text = conn.recv(1024).decode()  # Receive encrypted text
    decrypted_text = decrypt(encrypted_text, key)  # Decrypt the message
    print(f"Encrypted message received: {encrypted_text}")
    print(f"Decrypted message: {decrypted_text}")

    conn.close()

if __name__ == '__main__':
    server_program()
