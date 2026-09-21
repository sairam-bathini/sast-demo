import os
import sqlite3
import subprocess


def sanitize_upload_name(filename: str) -> str:
    """Return a safe file name without directory traversal payloads."""
    cleaned = os.path.basename(filename.strip())
    if not cleaned or cleaned in {".", ".."}:
        raise ValueError("Invalid file name")
    return cleaned


def safe_command(command: list[str], allowed: set[str]) -> str:
    """Execute a command only when it matches an allowlist."""
    if not command:
        raise ValueError("Command cannot be empty")

    executable = os.path.basename(command[0])
    normalized_allowed = {os.path.basename(item) for item in allowed}
    if executable not in normalized_allowed and command[0] not in allowed:
        raise ValueError(f"Command not allowed: {command[0]}")

    completed = subprocess.run(
        command,
        capture_output=True,
        text=True,
        shell=False,
        check=True,
    )
    return completed.stdout.strip()


def get_user_by_email(connection: sqlite3.Connection, email: str) -> dict[str, str | int] | None:
    """Look up a user using a parameterized query to avoid injection."""
    row = connection.execute(
        "SELECT id, email FROM users WHERE email = ?",
        (email,),
    ).fetchone()

    if row is None:
        return None

    return {"id": row[0], "email": row[1]}
