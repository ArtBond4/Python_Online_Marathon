def valid_email(email):
    import re
    pattern = r"[a-zA-Z0-9]+@[a-z.]+"
    result = re.fullmatch(pattern, email)
    try:

        if result is not None:
            return f"Email is valid"
            
        else:
            raise Exception(f"Email is not valid")
            
    except Exception as e:
        return e
