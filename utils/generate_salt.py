import secrets

# Generate a 16-byte hex string for a password salt
password_salt = secrets.token_hex(16)
print(password_salt)