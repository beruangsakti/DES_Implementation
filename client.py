import socket
from des import encrypt  # Import your DES encryption function

def client_program():
    host = '127.0.0.1'  # server IP address
    port = 65432        # server port
    key = '12345678'    # 64-bit key (8 characters)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    plaintext = input("Enter message to encrypt and send: ")
    encrypted_text = encrypt(plaintext, key)  # Encrypt the plaintext

    client_socket.send(encrypted_text.encode())  # Send encrypted text
    print("Encrypted message sent. (" + encrypted_text + ")")

    client_socket.close()

if __name__ == '__main__':
    client_program()
