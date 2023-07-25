
def validate_password(password):
    # Check length
    if len(password) < 8:
        return False

    # Check for uppercase letter
    if not any(char.isupper() for char in password):
        return False

    # Check for lowercase letter
    if not any(char.islower() for char in password):
        return False

    # Check for digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for spaces
    if ' ' in password:
        return False

    return True
 