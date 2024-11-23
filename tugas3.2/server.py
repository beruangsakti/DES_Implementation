import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from des import decrypt

# RSA key generation
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

# Save public key for client
with open("public_key.pem", "wb") as f:
    f.write(public_key)

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
    cipher_rsa = PKCS1_OAEP.new(RSA.import_key(private_key))
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