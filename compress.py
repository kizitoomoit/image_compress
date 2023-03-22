import os
from PIL import Image
from os import listdir


for images in os.listdir():

    # check if the image ends with png or jpg or jpeg
    if (images.endswith(".png") or images.endswith(".jpg") \
            or images.endswith(".jpeg")):
        print(images)

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format


    e.g:

       1253656 => '1.20MB'
       1253656678 => '1.17GB'

    """

    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor

    return f"{b:.2f}Y{suffix}"

def compress_img(image_name, new_size_ratio=0.9, quality=90, width=None, height=None, to_jpg=True):
    #load the image to memory
    img = Image.open(image_name)

    #print the original image shape
    print("[*] Image shape:", img.size)

    # get the original image size in bytes
    image_size = os.path.getsize(image_name)

    # print the size before compression/resizing
    print("[*] Size before compression:", get_size_format(image_size))
    if new_size_ratio < 1.0:
        # if resizing ration is below 1.0, then multiply with & height with this ratio to reduce image size
        img = img.resize((int(img.size[0] * new_size_ratio), int(img.size[1] * new_size_ratio)), Image.ANTIALIAS)

        # print new image shape

        print("[+] New Image shape:", img.size)
    elif width and height:
        # if width and height are set, resize with them instead

        img = img.resize((width, height), Image.ANTIALIAS)

        # print new image shape
        print("[+] new Image shape:", img.size)

    elif all:
        for file_name in os.listdir():
            if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
                with Image.open(file_name) as img:
                    img.save(file_name[:-4] + '_compressed{ext}', optimize=True, quality=50)

    #split the filename and extension
    filename, ext = os.path.splitext(image_name)

    # make new filename appending _compressed to the original file name

    if to_jpg:

        # change the extension to JPEG
        new_filename = f"{filename}_compressed.jpg"

    else:

        # retain the same extension of the original image
        new_filename = f"{filename}_compressed{ext}"

    try:

        # save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=quality, optimize=True)
    except OSError:

        # convert the image to RGB mode first

        img = img.convert("RGB")

        # save the image with the corresponding quality and optimize set to True
        img.save(new_filename, quality=quality, optimize=True)

    print("[+] New file saved:", new_filename)

    # get the new image size in bytes
    new_image_size = os.path.getsize(new_filename)
    # print the new size in a good format
    print("[+] Size after compression:", get_size_format(new_image_size))

    # calculate the saving bytes
    saving_diff = new_image_size - image_size

    #print the saving percentage
    print(f"[+] Image size change: {saving_diff/image_size*100:.2f}% of the original image size.")


if __name__=="__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Simple Python script for compressing and resizing images")
    parser.add_argument("--image", default=50, help="Target image to compress and/or resize")
    parser.add_argument("-j", "--to-jpg", action="store_true", help="whether to convert the image to the JPEG format")
    parser.add_argument("-q", "--quality", type=int, help="Quality ranging from a minimum of 0 (worst) to a maximum of 95 (best). Default is 90", default=90)
    parser.add_argument("-r", "--resize-ratio", type=float, help="Resizing ratio from 0 to 1, setting to 0.5 will multiply width & heigh of the image by 0.5. default is 1.0", default=1.0)
    parser.add_argument("-w", "--width", type=int, help="The new width image, make sure to set it with the 'height' parameter")
    parser.add_argument("-hh", "--height", type=int, help="The new height for the image, make sure to set it with the 'width' paramenter")
    args = parser.parse_args()

    # print the passed arguments
    print("="*50)
    print("[*] Image:", args.image)
    print("[*] To JPEG:", args.to_jpg)
    print("[*] Quality:", args.quality)
    print("[*] Resizing ratio:", args.resize_ratio)

    if args.width and args.height:
        print("[*] Width:", args.width)
        print("[*] height:", args.height)
        print("="*50)


    # compress the image

    compress_img(args.image, args.resize_ratio, args.quality, args.width, args.height, args.to_jpg)


