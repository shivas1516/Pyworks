import qrcode

from pyzbar.pyzbar import decode
import PIL.Image
import PIL.ImageDraw

def generate_qr(data, version=None, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4,
                fill_color="black", back_color="white", logo=None, logo_size=None, fit=True, embeded_image_path=None):
    """
    Generate a QR code with customizable options.

    Args:
        data (str): The data to be encoded in the QR code.
        version (int, optional): Version of the QR code (1-40). If None, the version is determined automatically.
        error_correction (int): Error correction level (L, M, Q, H).
        box_size (int): Size of the QR code boxes (pixels).
        border (int): Width of the QR code border.
        fill_color (str): Color of the QR code boxes.
        back_color (str): Color of the QR code background.
        logo (str, optional): Path to the logo image to be embedded in the QR code.
        logo_size (int, optional): Size of the embedded logo (pixels).
        fit (bool): Whether to fit the logo image to the available space in the QR code.
        embeded_image_path (str, optional): Path to the image to be embedded in the QR code.

    Returns:
        PIL.Image.Image: The generated QR code image.
    """
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=version,
        error_correction=error_correction,
        box_size=box_size,
        border=border
    )

    # Add the data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # Embed a logo in the QR code
    if logo:
        logo_img = PIL.Image.open(logo)
        if logo_size:
            logo_img = logo_img.resize((logo_size, logo_size))
        qr_w, qr_h = img.size
        logo_w, logo_h = logo_img.size
        logo_x = (qr_w - logo_w) // 2
        logo_y = (qr_h - logo_h) // 2
        img.paste(logo_img, (logo_x, logo_y), mask=logo_img)

    # Embed an image in the QR code
    if embeded_image_path:
        embeded_img = PIL.Image.open(embeded_image_path)
        draw = PIL.ImageDraw.Draw(img)
        img_w, img_h = embeded_img.size
        qr_w, qr_h = img.size
        embeded_img = embeded_img.resize((qr_w // 2, qr_h // 2))
        img.paste(embeded_img, (qr_w // 4, qr_h // 4))

    return img

def decode_qr(image_path):
    """
    Decode a QR code from an image.

    Args:
        image_path (str): Path to the image containing the QR code.

    Returns:
        str: The decoded data from the QR code, or None if no QR code is found.
    """
    # Open the image
    img = PIL.Image.open(image_path)

    # Decode the QR code
    result = decode(img)

    # Return the decoded data if a QR code is found
    if result:
        return result[0].data.decode("utf-8")
    else:
        return None