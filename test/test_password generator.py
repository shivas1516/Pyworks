import unittest
import string
from Pyworks.password_generator import *

class TestPasswordGenerator(unittest.TestCase):
    def test_generate_personalized_password(self):
        password = generate_personalized_password("JohnDoe", length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_memorable_password(self):
        password = generate_memorable_password(length=15, num_words=3, delimiter='-', include_digits=True, include_special_chars=True)
        self.assertEqual(len(password), 15)
        self.assertTrue('-' in password)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_pronounceable_password(self):
        password = generate_pronounceable_password(length=10, include_digits=True, include_special_chars=True)
        self.assertEqual(len(password), 10)
        self.assertTrue(password[0] not in 'aeiou')
        self.assertTrue(password[-1] not in 'aeiou')
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_score_password_strength(self):
        weak_password = "password"
        strong_password = "Str0ngP@ssw0rd"
        self.assertEqual(score_password_strength(weak_password), 1)
        self.assertEqual(score_password_strength(strong_password), 5)

    def test_generate_pattern_based_password(self):
        character_sets = {
            'C': string.ascii_letters,
            'D': string.digits,
            'S': string.punctuation
        }
        password = generate_pattern_based_password("CCDCSSDCC", character_sets, length=9)
        self.assertEqual(len(password), 9)
        self.assertTrue(any(char.isalpha() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_generate_multi_word_password(self):
        password = generate_multi_word_password(length=15, num_words=3, delimiter='-', include_digits=True, include_special_chars=True)
        self.assertEqual(len(password), 15)
        self.assertTrue('-' in password)
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

    def test_export_password(self):
        password = "MyPassword123!"
        plain_export = export_password(password, 'plain')
        base64_export = export_password(password, 'base64')
        hex_export = export_password(password, 'hex')
        self.assertEqual(plain_export, password)
        self.assertEqual(base64_export, 'TXlQYXNzd29yZDEyMyE=')
        self.assertEqual(hex_export, '4d79506173737764313233')
        with self.assertRaises(ValueError):
            export_password(password, 'invalid_format')

    def test_calculate_entropy(self):
        weak_password = "password"
        strong_password = "Str0ngP@ssw0rd"
        self.assertAlmostEqual(calculate_entropy(weak_password), 37.61, delta=0.01)
        self.assertAlmostEqual(calculate_entropy(strong_password), 96.36, delta=0.01)

    def test_generate_cryptographically_secure_password(self):
        password = generate_cryptographically_secure_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True)
        self.assertEqual(len(password), 12)
        self.assertTrue(any(char.isupper() for char in password))
        self.assertTrue(any(char.islower() for char in password))
        self.assertTrue(any(char.isdigit() for char in password))
        self.assertTrue(any(char in string.punctuation for char in password))

if __name__ == '__main__':
    unittest.main()