import string
import secrets
import random
from itertools import chain
from math import log2

def generate_personalized_password(name, length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    """
    Generate a personalized password based on a given name.

    Args:
        name (str): The name to be used as the basis for the personalized password.
        length (int): The desired length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated personalized password.
    """
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    name_chars = ''.join(random.choices(name.lower(), k=length // 4))
    remaining_chars = ''.join(secrets.choice(characters) for _ in range(length - len(name_chars)))
    password = ''.join(random.sample(name_chars + remaining_chars, len(name_chars + remaining_chars)))

    return password

def generate_memorable_password(length=12, num_words=3, delimiter='-', include_digits=True, include_special_chars=True):
    """
    Generate a memorable password by combining common words with numbers and special characters.

    Args:
        length (int): The desired length of the password.
        num_words (int): The number of common words to include in the password.
        delimiter (str): The character to use as a delimiter between words and other characters.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated memorable password.
    """
    with open('/usr/share/dict/words', 'r') as f:
        words = [word.strip().lower() for word in f.read().split()]

    selected_words = secrets.sample(words, num_words)
    remaining_length = length - (num_words * len(delimiter))
    additional_chars = generate_random_characters(remaining_length, include_digits, include_special_chars)

    password = delimiter.join(selected_words) + additional_chars
    return ''.join(random.sample(password, len(password)))

def generate_pronounceable_password(length=12, include_digits=True, include_special_chars=True):
    """
    Generate a pronounceable password that resembles a word or phrase from a language.

    Args:
        length (int): The desired length of the password.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated pronounceable password.
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    password = ''.join(secrets.choice(consonants + vowels) for _ in range(length))

    # Ensure the password starts and ends with a consonant
    if password[0] in vowels:
        password = consonants[0] + password[1:]
    if password[-1] in vowels:
        password = password[:-1] + consonants[-1]

    additional_chars = generate_random_characters(length // 4, include_digits, include_special_chars)
    password = ''.join(random.sample(password + additional_chars, len(password + additional_chars)))

    return password

def score_password_strength(password):
    """
    Score the strength of a given password based on various criteria.

    Args:
        password (str): The password to be scored.

    Returns:
        int: A score representing the strength of the password, ranging from 0 (weak) to 5 (strong).
    """
    score = 0
    if len(password) >= 8:
        score += 1
    if any(char.isupper() for char in password):
        score += 1
    if any(char.islower() for char in password):
        score += 1
    if any(char.isdigit() for char in password):
        score += 1
    if any(char in string.punctuation for char in password):
        score += 1

    return score

def generate_pattern_based_password(pattern, character_sets, length=12):
    """
    Generate a password based on a specified pattern and custom character sets.

    Args:
        pattern (str): The pattern to follow for generating the password. Use 'C' for characters, 'D' for digits, and 'S' for special characters.
        character_sets (dict): A dictionary containing custom character sets for characters ('C'), digits ('D'), and special characters ('S').
        length (int): The desired length of the password.

    Returns:
        str: The generated pattern-based password.
    """
    characters = []
    for char in pattern[:length]:
        if char == 'C':
            characters.append(secrets.choice(character_sets['C']))
        elif char == 'D':
            characters.append(secrets.choice(character_sets['D']))
        elif char == 'S':
            characters.append(secrets.choice(character_sets['S']))

    return ''.join(characters)

def generate_multi_word_password(length=12, num_words=3, delimiter='-', include_digits=True, include_special_chars=True):
    """
    Generate a password composed of multiple words separated by a delimiter.

    Args:
        length (int): The desired length of the password.
        num_words (int): The number of words to include in the password.
        delimiter (str): The character to use as a delimiter between words.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated multi-word password.
    """
    with open('/usr/share/dict/words', 'r') as f:
        words = [word.strip().lower() for word in f.read().split()]

    selected_words = secrets.sample(words, num_words)
    remaining_length = length - (num_words * len(delimiter)) - (num_words - 1)
    additional_chars = generate_random_characters(remaining_length, include_digits, include_special_chars)

    password = delimiter.join(chain(selected_words, [additional_chars]))
    return ''.join(random.sample(password, len(password)))

def generate_random_characters(length, include_digits=True, include_special_chars=True):
    """
    Generate a string of random characters with optional inclusion of digits and special characters.

    Args:
        length (int): The desired length of the random character string.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated string of random characters.
    """
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    return ''.join(secrets.choice(characters) for _ in range(length))

def export_password(password, export_format):
    """
    Export a password in a specified format.

    Args:
        password (str): The password to be exported.
        export_format (str): The desired export format (e.g., 'plain', 'base64', 'hex').

    Returns:
        str: The exported password in the specified format.
    """
    if export_format == 'plain':
        return password
    elif export_format == 'base64':
        import base64
        return base64.b64encode(password.encode()).decode()
    elif export_format == 'hex':
        return password.encode().hex()
    else:
        raise ValueError(f"Invalid export format: {export_format}")

def calculate_entropy(password):
    """
    Calculate the entropy (randomness) of a given password.

    Args:
        password (str): The password for which to calculate entropy.

    Returns:
        float: The entropy of the password in bits.
    """
    charset = set(password)
    charset_len = len(charset)
    entropy = len(password) * log2(charset_len)
    return entropy

def generate_cryptographically_secure_password(length=12, include_uppercase=True, include_lowercase=True, include_digits=True, include_special_chars=True):
    """
    Generate a cryptographically secure password using the system's secure random number generator.

    Args:
        length (int): The desired length of the password.
        include_uppercase (bool): Whether to include uppercase letters.
        include_lowercase (bool): Whether to include lowercase letters.
        include_digits (bool): Whether to include digits.
        include_special_chars (bool): Whether to include special characters.

    Returns:
        str: The generated cryptographically secure password.
    """
    characters = ''
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_digits:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password