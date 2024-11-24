import socket
from Crypto.Cipher import PKCS1_OAEP
from pka import get_private_key, get_public_key
from des import decrypt  # Ensure this is your DES implementation

def handle_client(conn, private_key):
    try:
        # Send public key to client
        public_key = get_public_key()
        conn.send(public_key.export_key())
        print("Public key sent to client.")

        # Receive and decrypt the DES key
        encrypted_des_key = conn.recv(256)  # Adjust size to fit RSA key length
        cipher_rsa = PKCS1_OAEP.new(private_key)
        des_key = cipher_rsa.decrypt(encrypted_des_key).decode()
        print(f"Decrypted DES key: {des_key}")

        while True:
            # Receive message from client
            received_data = conn.recv(1024)

            # Decode text message
            try:
                message = received_data.decode("utf-8")
                if message.lower() == "cut":
                    print("Client requested to cut the connection.")
                    break
                elif message.lower() == "shutdown":
                    print("Shutdown command received.")
                    return "shutdown"

                # If not a command, treat as an encrypted message
                decrypted_message = decrypt(message, des_key)
                print(f"Decrypted message: {decrypted_message}")
            except UnicodeDecodeError:
                # Handle cases where data is not UTF-8 (likely encrypted message)
                encrypted_message = received_data.decode()
                decrypted_message = decrypt(encrypted_message, des_key)
                print(f"Decrypted message: {decrypted_message}")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        conn.close()
        print("Client disconnected.")

def server_program():
    passphrase = input("Enter the passphrase for the private key: ")
    private_key = get_private_key(passphrase)

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("localhost", 12345))
    server.listen(5)
    print("Server is listening on port 12345...")

    try:
        while True:
            conn, addr = server.accept()
            print(f"Connection established with {addr}")

            # Handle client in a separate function
            if handle_client(conn, private_key) == "shutdown":
                break

    except KeyboardInterrupt:
        print("Server interrupted manually.")

    finally:
        server.close()
        print("Server shut down.")

if __name__ == "__main__":
    server_program()
