import io
import unittest
from contextlib import redirect_stdout

import hello


class HelloTests(unittest.TestCase):
    def test_main_prints_greeting(self):
        output = io.StringIO()
        with redirect_stdout(output):
            hello.main()

        self.assertEqual(output.getvalue().strip(), "Hello from feature/x!")


if __name__ == "__main__":
    unittest.main()
