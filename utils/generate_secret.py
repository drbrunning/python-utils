import secrets

# Generate a 64-character hex string
cookie_secret = secrets.token_hex(32)
print(cookie_secret)