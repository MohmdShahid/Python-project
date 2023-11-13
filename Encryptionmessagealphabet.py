def encrypt(message, shift):
    encrypted_message = ""

    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_message += encrypted_char
        else:
            encrypted_message += char

    return encrypted_message

# Original message
message_to_encrypt = "how are you and what are you doing "

# Encryption shift
shift_amount = 3

# Encrypt the message
encrypted_message = encrypt(message_to_encrypt, shift_amount)

# Print results
print(f"Original message: {message_to_encrypt}")
print(f"Encrypted message: {encrypted_message}")





############output Original message: how are you and what are you doing
###################Encrypted message: krz duh brx dqg zkdw duh brx grlqj
