import string
import random
import sqlite3
import datetime

# Initialize the SQLite database
conn = sqlite3.connect('url_shortener.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS urls
             (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_url TEXT UNIQUE, created_at TIMESTAMP, expires_at TIMESTAMP, clicks INTEGER DEFAULT 0)''')
conn.commit()

def shorten_url(original_url, custom_short=None, expiration_days=None):
    """
    Shorten a URL and store it in the database.

    Args:
        original_url (str): The original URL to be shortened.
        custom_short (str, optional): A custom short URL. If provided, it will be used if available.
        expiration_days (int, optional): Number of days after which the short URL will expire.

    Returns:
        str: The shortened URL.
    """
    # Generate a short URL if no custom short URL is provided
    if not custom_short:
        short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    else:
        short_url = custom_short

    # Check if the short URL is already taken
    c.execute("SELECT * FROM urls WHERE short_url = ?", (short_url,))
    existing_url = c.fetchone()
    if existing_url:
        if custom_short:
            return None  # Custom short URL is taken
        else:
            short_url = ''.join(random.choices(string.ascii_letters + string.digits, k=6))

    # Calculate the expiration date if provided
    expires_at = None
    if expiration_days:
        expires_at = datetime.datetime.now() + datetime.timedelta(days=expiration_days)

    # Insert the new URL into the database
    c.execute("INSERT INTO urls (original_url, short_url, created_at, expires_at) VALUES (?, ?, ?, ?)",
              (original_url, short_url, datetime.datetime.now(), expires_at))
    conn.commit()

    return f"http://example.com/{short_url}"

def resolve_url(short_url):
    """
    Retrieve the original URL from the short URL.

    Args:
        short_url (str): The short URL to be resolved.

    Returns:
        str: The original URL, or None if the short URL is not found or expired.
    """
    # Query the database for the short URL
    c.execute("SELECT original_url, expires_at, clicks FROM urls WHERE short_url = ?", (short_url,))
    url_info = c.fetchone()

    if url_info:
        original_url, expires_at, clicks = url_info
        now = datetime.datetime.now()

        # Check if the URL has expired
        if expires_at and now > expires_at:
            return None  # URL has expired

        # Increment the click count
        clicks += 1
        c.execute("UPDATE urls SET clicks = ? WHERE short_url = ?", (clicks, short_url))
        conn.commit()

        return original_url
    else:
        return None

def get_url_analytics(short_url):
    """
    Retrieve analytics for a short URL.

    Args:
        short_url (str): The short URL to retrieve analytics for.

    Returns:
        dict: A dictionary containing the original URL, creation date, expiration date (if applicable), and click count.
    """
    c.execute("SELECT original_url, created_at, expires_at, clicks FROM urls WHERE short_url = ?", (short_url,))
    url_info = c.fetchone()

    if url_info:
        original_url, created_at, expires_at, clicks = url_info
        analytics = {
            "original_url": original_url,
            "created_at": created_at,
            "expires_at": expires_at,
            "clicks": clicks
        }
        return analytics
    else:
        return None
