import re

def is_valid_email(email):
    """
    Validate an email address using a regular expression.
    """
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None

