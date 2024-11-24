from Crypto.PublicKey import RSA

def generate_keys(passphrase):
    # Generate RSA key pair
    key = RSA.generate(2048)
    private_key = key.export_key(passphrase=passphrase, pkcs=8, protection="scryptAndAES128-CBC")
    public_key = key.publickey().export_key()

    # Save private key securely
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key)

    # Save public key
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key)

    print("RSA keys generated and saved securely.")

def get_private_key(passphrase):
    # Load the private key securely
    with open("private_key.pem", "rb") as private_file:
        return RSA.import_key(private_file.read(), passphrase=passphrase)

def get_public_key():
    # Load the public key
    with open("public_key.pem", "rb") as public_file:
        return RSA.import_key(public_file.read())

if __name__ == "__main__":
    passphrase = input("Enter a strong passphrase to protect the private key: ")
    generate_keys(passphrase)
