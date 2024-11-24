import socket
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from des import encrypt  

# Hardcoded DES key for demonstration purposes
DES_KEY = "12345678"

def load_public_key():
    # Load the public key
    with open("public_key.pem", "rb") as public_file:
        return RSA.import_key(public_file.read())

def client_program():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 12345))

    # Load public key from file
    rsa_public_key = load_public_key()
    cipher_rsa = PKCS1_OAEP.new(rsa_public_key)

    # Encrypt the hardcoded DES key
    encrypted_des_key = cipher_rsa.encrypt(DES_KEY.encode())
    client.send(encrypted_des_key)
    print("Encrypted DES key sent to server.")

    try:
        while True:
            # Input message
            message = input("Enter a message to send ('cut' to disconnect, 'shutdown' to stop the server): ")

            # Encrypt and send the message
            if message.lower() == "shutdown":
                client.send(message.encode())
                print("Shutdown command sent to server.")
                break

            elif message.lower() == "cut":
                client.send(message.encode())
                print("Cut command sent. Disconnecting from the server.")
                break

            # Encrypt the message using the DES key
            encrypted_message = encrypt(message, DES_KEY)
            client.send(encrypted_message.encode())
            print(f"Encrypted message sent: {encrypted_message}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client.close()
        print("Disconnected from the server.")

if __name__ == "__main__":
    client_program()
