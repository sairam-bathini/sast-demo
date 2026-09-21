"""Intentionally vulnerable examples for SAST scanner demonstrations.

Do not use these helpers in production code.
"""

import hashlib
import os
import sqlite3
import subprocess


def run_untrusted_command(command: str) -> str:
    """Command injection: the caller controls a shell command."""
    completed = subprocess.run(command, capture_output=True, text=True, shell=True, check=True)
    return completed.stdout


def find_user_vulnerable(connection: sqlite3.Connection, email: str):
    """SQL injection: user input is concatenated into a query."""
    query = "SELECT id, email FROM users WHERE email = '" + email + "'"
    return connection.execute(query).fetchone()


def read_upload_vulnerable(upload_dir: str, filename: str) -> str:
    """Path traversal: the filename is not constrained to upload_dir."""
    with open(os.path.join(upload_dir, filename), encoding="utf-8") as upload:
        return upload.read()


def checksum_vulnerable(value: str) -> str:
    """Weak cryptography: MD5 is unsuitable for security-sensitive checksums."""
    return hashlib.md5(value.encode()).hexdigest()