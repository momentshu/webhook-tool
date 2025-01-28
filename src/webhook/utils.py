import random
import string

def generate_random_name(length=8):
    """Generate a random webhook name if none is provided."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))