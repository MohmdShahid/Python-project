def encrypt(message):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a') + 1
            encrypted_message += str(char_value) + ' '
        else:
            encrypted_message += char

    return encrypted_message.strip()

# Original message
message_to_encrypt = "Hello, World!"

# Encrypt the message
encrypted_message = encrypt(message_to_encrypt)

# Print results
print(f"Original message: {message_to_encrypt}")
print(f"Encrypted message: {encrypted_message}")


##### output Original message: Hello, World!
#############Encrypted message: 8 5 12 12 15 , 23 15 18 12 4 !
