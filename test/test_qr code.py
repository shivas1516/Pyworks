import unittest
import os
from PIL import Image
from Pyworks.qr_code import *

class TestQRFunctions(unittest.TestCase):
    def test_generate_qr(self):
        # Test data
        data = "https://www.example.com"
        qr_image_path = "test_qr_code.png"

        # Generate QR code
        qr_image = generate_qr(data)
        qr_image.save(qr_image_path)

        # Decode QR code
        decoded_data = decode_qr(qr_image_path)

        # Clean up the temporary QR code image
        os.remove(qr_image_path)

        # Assertions
        self.assertEqual(decoded_data, data)

    def test_decode_qr(self):
        # Test data
        data = "https://www.example.com"
        qr_image_path = "test_qr_code.png"

        # Generate QR code
        qr_image = generate_qr(data)
        qr_image.save(qr_image_path)

        # Decode QR code from the saved image
        decoded_data = decode_qr(qr_image_path)

        # Clean up the temporary QR code image
        os.remove(qr_image_path)

        # Assertions
        self.assertEqual(decoded_data, data)

if __name__ == '__main__':
    unittest.main()
