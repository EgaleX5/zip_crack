from cryptography.fernet import Fernet

# Generate a key and instantiate a Fernet instance
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Save the key in a file
with open('encryption.key', 'wb') as key_file:
    key_file.write(key)

# Encrypt a message
message = "This is a secret message"
encrypted_message = cipher_suite.encrypt(message.encode())

print(f"Encrypted Message: {encrypted_message}")
