import hashlib

# Function to hash passwords
def hash_password(password):
    # Hash the password using SHA-256
    return hashlib.sha256(password.encode()).hexdigest()

# Dummy database for user credentials
user_database = {
    'user1': {
        'password': '5e88489803d0d6aabbf721d1542d8'  # Hashed password for 'password1'
    },
    'user2': {
        'password': '2a1a0e2692d0bc3b39982e4a0f4da'  # Hashed password for 'password2'
    }
}

# Function to authenticate users
def authenticate(username, password):
    # Check if the username exists in the database
    if username in user_database:
        # Hash the provided password
        hashed_password = hash_password(password)
        # Compare the hashed password with the one stored in the database
        if hashed_password == user_database[username]['password']:
            print("Login successful!")
        else:
            print("Incorrect password!")
    else:
        print("Username not found!")

# Main function
def main():
    username = input("Enter username: ")
    password = input("Enter password: ")
    authenticate(username, password)

if __name__ == "__main__":
    main()
