# SAST Demo Project

This project is a small Python application designed to demonstrate how static application security testing (SAST) tools review code for issues like unsafe command execution, path traversal, and injection risks.

The code intentionally follows secure coding patterns so it can be scanned without introducing obvious vulnerabilities. It is intended as a starting point for demos, training, and security reviews.

## Project layout

- `sast_demo/` — application package
- `tests/` — basic verification tests

## Run the app

```bash
python -m sast_demo.app
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Example behaviors

- User input is sanitized before use in filesystem paths.
- command execution uses an allowlist and does not invoke a shell.
- SQL queries use parameterized statements.
