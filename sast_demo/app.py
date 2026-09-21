from __future__ import annotations

import os
import sys

from .security import safe_command, sanitize_upload_name


def handle_upload(filename: str) -> str:
    """Normalize the upload name and return a safe value."""
    return sanitize_upload_name(filename)


def run_allowed_command(raw_command: list[str]) -> str:
    """Run a pre-approved command while enforcing a strict allowlist."""
    allowed = {sys.executable, os.path.basename(sys.executable)}
    return safe_command(raw_command, allowed)


def main() -> None:
    print("SAST demo app is running.")
    print(handle_upload("report-final.csv"))
    print(run_allowed_command([sys.executable, "-c", "print('demo-ready')"]))


if __name__ == "__main__":
    main()
