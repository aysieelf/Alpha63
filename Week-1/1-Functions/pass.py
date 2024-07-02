import string
import random

def generate_password(n: int) -> str:
    """
    Generates a password of random upper and lowercase letters and digits with the length of an input number.
    
    Parameters:
        n (int) : Length of password.
    
    Returns:
        password (str) : String of random letters and digits with length n.
    """
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(n))

    return password


# Test cases
x = generate_password(8)  # password could be "aB3dE4fG"
print(x)
x = generate_password(12) # password could be "Hk9Pv4wBz2Lq"
print(x)
