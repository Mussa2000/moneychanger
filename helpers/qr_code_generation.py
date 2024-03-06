import os
from base64 import b64encode
from django.conf import settings
import random
import qrcode


def encode_data(data) -> str:
    stringified_data = str(data)
    stringified_data_bytes = stringified_data.encode("ascii")
    encoded_data = b64encode(stringified_data_bytes)
    return encoded_data


def generate_qr_code(
    data: dict,
    version=3,
    box_size=20,
    border=1,
    fill_color="white",
    back_color="black",
    output_qr_image_path=None,
):
    if output_qr_image_path is None:
        output_qr_image_path = settings.MEDIA_ROOT
        
    def get_random_int():
        return random.randint(0,5000)
        
    qr = qrcode.QRCode(version=version, box_size=box_size, border=border)
    encoded_data = encode_data(data)
    qr.add_data(encoded_data)

    qr_image = qr.make_image(fill_color=fill_color, back_color=back_color)
    
    
    # output_qr_image_path = os.path.join(output_qr_image_path, qr_image_file_name)
    
    output_qr_image_path = output_qr_image_path # + f'/qr-{get_random_int()}-{get_random_int()}.png'
    
    qr_image.save(output_qr_image_path)
    
    return output_qr_image_path
