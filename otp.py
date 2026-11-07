import secrets
import string


def generate_otp(length: int = 6, numeric_only: bool = True) -> str:
    """Generate a cryptographically secure One-Time Password (OTP).

    :param length: Number of characters/digits in the OTP (default is 6).
    :param numeric_only: If True, uses digits 0-9; if False, uses
      alphanumeric.
    :return: Generated OTP string.
    """
    characters = (
        string.digits
        if numeric_only
        else string.digits + string.ascii_uppercase
    )
    return "".join(secrets.choice(characters) for _ in range(length))


if __name__ == "__main__":
    # 6-digit numeric OTP
    print(f"6-digit numeric OTP: {generate_otp()}")

    # 4-digit numeric OTP
    print(f"4-digit numeric OTP: {generate_otp(length=4)}")

    # 8-character alphanumeric OTP
    print(
        f"8-char alphanumeric OTP: {generate_otp(length=8, numeric_only=False)}"
    )
