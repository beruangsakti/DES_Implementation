import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from des import decrypt

# Load RSA keys from files
with open("private_key.pem", "rb") as private_file:
    private_key = RSA.import_key(private_file.read())  # Already an RsaKey object

with open("public_key.pem", "rb") as public_file:
    public_key = public_file.read()  # Raw public key data

def server_program():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server.accept()
    print(f"Connection established with {addr}")

    # Send public key to client
    conn.send(public_key)
    print("Public key sent to client.")

    # Receive encrypted DES key
    encrypted_des_key = conn.recv(1024)
    cipher_rsa = PKCS1_OAEP.new(private_key)  # Use the already imported RsaKey object
    des_key = cipher_rsa.decrypt(encrypted_des_key).decode()
    print(f"Decrypted DES key: {des_key}")

    # Receive encrypted message
    encrypted_message = conn.recv(1024).decode()
    print(f"Encrypted message received: {encrypted_message}")

    # Decrypt the message using the received DES key
    decrypted_message = decrypt(encrypted_message, des_key)
    print(f"Decrypted message: {decrypted_message}")

    conn.close()
    server.close()

if __name__ == "__main__":
    server_program()
