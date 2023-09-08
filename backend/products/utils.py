import sys
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


def pil_image_to_django_file(picture_name):
    path = f'../frontend/temp/{picture_name}'
    picture = Image.open(path)
    pic_io = BytesIO()
    picture.save(pic_io, format='JPEG')
    pic_io.seek(0)  # it will get back the bytes value from buffer - needed
    new_pic = InMemoryUploadedFile(pic_io, 'picture', picture_name, 'image/jpeg',
                                   sys.getsizeof(pic_io), None)
    return new_pic
