# SAST Demo Project

This project is a small Python application designed to demonstrate how static application security testing (SAST) tools review code for issues like unsafe command execution, path traversal, and injection risks.

The secure examples are paired with intentionally vulnerable examples so a SAST scanner can report findings during demos. The vulnerable module is for training only and must not be used in production.

## Project layout

- `sast_demo/` — application package
- `sast_demo/vulnerable_examples.py` — deliberate CodeQL findings for demonstrations
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

## Intentional findings

`sast_demo/vulnerable_examples.py` contains examples of command injection, SQL injection, path traversal, and weak MD5 hashing. Scan the repository with CodeQL to review the resulting alerts, then compare them with the secure implementations in `sast_demo/security.py`.
