"""Public test fixture: deliberately hardcoded official dummy token.

This module makes no requests and never prints the token.
"""

GITHUB_TOKEN = "secret_scanning_ab85fc6f8d7638cf1c11da812da308d43_abcde"


if __name__ == "__main__":
    print("Secret scanning fixture only; no authentication or network request.")
