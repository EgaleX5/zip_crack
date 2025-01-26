from cryptography.fernet import Fernet

# Read the key from the file
with open('encryption.key', 'rb') as key_file:
    key = key_file.read()

cipher_suite = Fernet(key)

# Encrypted message from the output of encrypt_script.py
encrypted_message = b'gAAAAABnf35ffyjvmWDJHfhUaqChufcHyGAB0RlLMoiwIe3uEszIDHmXfpXdKWSPWDNlcyUkqQycbl29UGBPHdy2qgMuj1_LG0tRzrN83N-9tyVRwLJ6hWs='  # Your encrypted message here
decrypted_message = cipher_suite.decrypt(encrypted_message)

print(f"Decrypted Message: {decrypted_message.decode()}")
