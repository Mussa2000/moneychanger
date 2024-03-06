import base64

def image_to_base64(image_path):
    """
    Convert an image file to a base64-encoded string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string.
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        return encoded_string

# # Example usage:
# image_path = 'path/to/your/image.jpg'
# base64_string = image_to_base64(image_path)
# print(base64_string)
