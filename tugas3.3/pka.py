from Crypto.PublicKey import RSA

def generate_rsa_keys():
    # Generate RSA keys
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    
    # Save private key to a file
    with open("private_key.pem", "wb") as private_file:
        private_file.write(private_key)
    print("Private key saved to 'private_key.pem'")
    
    # Save public key to a file
    with open("public_key.pem", "wb") as public_file:
        public_file.write(public_key)
    print("Public key saved to 'public_key.pem'")

if __name__ == "__main__":
    generate_rsa_keys()
