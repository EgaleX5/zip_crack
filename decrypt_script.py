from cryptography.fernet import Fernet

# Read the key from the file
with open('encryption.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Decrypt the message
encrypted_message = b'Encrypted message here'  # Replace with actual encrypted message
decrypted_message = cipher_suite.decrypt(encrypted_message)

print(f"Decrypted Message: {decrypted_message.decode()}")
