import socket
from Crypto.Cipher import PKCS1_OAEP
from pka import get_private_key, get_public_key
from des import decrypt  # Ensure this is your DES implementation

def server_program():
    passphrase = input("Enter the passphrase for the private key: ")
    private_key = get_private_key(passphrase)
    public_key = get_public_key()

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server.accept()
    print(f"Connection established with {addr}")

    # Send public key to client
    conn.send(public_key.export_key())
    print("Public key sent to client.")

    try:
        # Receive encrypted DES key
        encrypted_des_key = conn.recv(1024)
        cipher_rsa = PKCS1_OAEP.new(private_key)
        des_key = cipher_rsa.decrypt(encrypted_des_key).decode()
        print(f"Decrypted DES key: {des_key}")

        # Receive encrypted message
        encrypted_message = conn.recv(1024).decode()
        print(f"Encrypted message received: {encrypted_message}")

        # Decrypt the message using the DES key
        decrypted_message = decrypt(encrypted_message, des_key)
        print(f"Decrypted message: {decrypted_message}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
        server.close()

if __name__ == "__main__":
    server_program()
