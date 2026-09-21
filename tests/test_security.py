import sqlite3
import sys
import unittest

from sast_demo.security import get_user_by_email, safe_command, sanitize_upload_name


class SecurityFunctionsTest(unittest.TestCase):
    def test_sanitize_upload_name(self):
        self.assertEqual(sanitize_upload_name("../private.txt"), "private.txt")
        self.assertEqual(sanitize_upload_name("  report.csv  "), "report.csv")

    def test_safe_command(self):
        result = safe_command([sys.executable, "-c", "print('hello')"], {sys.executable})
        self.assertEqual(result, "hello")

    def test_get_user_by_email(self):
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT)")
        connection.execute("INSERT INTO users (email) VALUES (?)", ("demo@example.com",))
        connection.commit()

        user = get_user_by_email(connection, "demo@example.com")
        self.assertEqual(user, {"id": 1, "email": "demo@example.com"})

        connection.close()


if __name__ == "__main__":
    unittest.main()
