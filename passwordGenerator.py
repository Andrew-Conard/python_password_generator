import random

def generate_password(length=16):
    """
    Generates a random password containing letters, digits, and special characters.
    
    :param length: Length of the password to be generated (default is 16)
    :return: A string representing the generated password
    """
    chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?{}[]<>'
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = 16  # You can change this to any desired password length
    print('Your password: ', generate_password(password_length))
