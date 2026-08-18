print("Access Log Validator is running")


def validate_access(is_active):
    if is_active:
        return "access granted"
    return "access denied"


def summarize_event(username, is_active):
    status = validate_access(is_active)
    return f"{username}: {status}"


print(validate_access(True))
print(summarize_event("dennis", True))
