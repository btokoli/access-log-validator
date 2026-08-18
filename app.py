print("Access Log Validator is running")

print("Access Log Validator is running")


def validate_access(is_active):
    if is_active:
        return "access granted"
    return "access denied"


print(validate_access(True))
