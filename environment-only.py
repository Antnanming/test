"""Negative control: reference environment variables without committing values."""

import os


def read_credentials():
    return {
        "github_token": os.environ.get("GITHUB_TOKEN"),
        "database_password": os.environ.get("DATABASE_PASSWORD"),
    }


if __name__ == "__main__":
    print("Environment-only example; credential values are never printed.")
