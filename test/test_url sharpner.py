import unittest
import os
import sqlite3
import datetime
from Pyworks.url_sharpner import *

class TestURLShortenerFunctions(unittest.TestCase):
    def setUp(self):
        # Initialize the SQLite database
        self.conn = sqlite3.connect(':memory:')
        self.c = self.conn.cursor()
        self.c.execute('''CREATE TABLE IF NOT EXISTS urls
                         (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_url TEXT UNIQUE, created_at TIMESTAMP, expires_at TIMESTAMP, clicks INTEGER DEFAULT 0)''')
        self.conn.commit()

    def tearDown(self):
        # Close the database connection
        self.conn.close()

    def test_shorten_url(self):
        # Test data
        original_url = "https://www.example.com"
        custom_short = "custom"
        expiration_days = 7

        # Shorten the URL
        short_url = shorten_url(original_url)
        self.assertIsNotNone(short_url)

        # Shorten the URL with custom short URL
        custom_short_url = shorten_url(original_url, custom_short)
        self.assertIsNotNone(custom_short_url)
        self.assertEqual(custom_short_url, f"http://example.com/{custom_short}")

        # Shorten the URL with expiration days
        expiring_short_url = shorten_url(original_url, expiration_days=expiration_days)
        self.assertIsNotNone(expiring_short_url)

    def test_resolve_url(self):
        # Test data
        original_url = "https://www.example.com"
        short_url = shorten_url(original_url)

        # Resolve the short URL
        resolved_url = resolve_url(short_url)
        self.assertEqual(resolved_url, original_url)

        # Resolve non-existent short URL
        non_existent_url = resolve_url("nonexistent")
        self.assertIsNone(non_existent_url)

    def test_get_url_analytics(self):
        # Test data
        original_url = "https://www.example.com"
        short_url = shorten_url(original_url)

        # Get analytics for the short URL
        analytics = get_url_analytics(short_url)
        self.assertIsNotNone(analytics)
        self.assertEqual(analytics["original_url"], original_url)
        self.assertIsNotNone(analytics["created_at"])
        self.assertIsNone(analytics["expires_at"])
        self.assertEqual(analytics["clicks"], 0)

if __name__ == '__main__':
    unittest.main()
