import secrets
import string


def generate_password(min_length=8, max_length=15):
    """Generate a single random password between min_length and max_length characters."""
    length = secrets.randbelow(max_length - min_length + 1) + min_length
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def generate_unique_passwords(count=5, min_length=8, max_length=15):
    """Generate a set of unique passwords."""
    passwords = set()
    max_attempts = count * 100
    attempts = 0
    while len(passwords) < count and attempts < max_attempts:
        passwords.add(generate_password(min_length, max_length))
        attempts += 1
    if len(passwords) < count:
        raise RuntimeError("Could not generate enough unique passwords.")
    return list(passwords)


if __name__ == "__main__":
    passwords = generate_unique_passwords()
    print("5 unikaalset parooli (8–15 sümbolit):")
    for i, pwd in enumerate(passwords, start=1):
        print(f"  {i}. {pwd}")
