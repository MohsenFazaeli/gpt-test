"""Tests for the local GPT test starter."""

import unittest

from gpt_test import smoke_test_message


class SmokeTest(unittest.TestCase):
    def test_smoke_test_message(self) -> None:
        self.assertEqual(smoke_test_message(), "GPT test starter is ready.")


if __name__ == "__main__":
    unittest.main()
