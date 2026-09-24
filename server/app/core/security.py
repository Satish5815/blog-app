from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()


def hash_password(password: str) -> str:
    # Convert plain password into a secure hash
    return password_hash.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    # Compare plain password with stored hash
    return password_hash.verify(password, hashed_password)