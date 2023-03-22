from PIL import Image
import os

for file_name in os.listdir():
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        with Image.open(file_name) as img:
            img.save(file_name[:-4] + '_converted.jpg', optimize=True, quality=50)
