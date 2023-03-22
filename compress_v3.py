import os
import argparse
from PIL import Image

def compress_image(infile, outfile, level):
    img = Image.open(infile)
    img.save(outfile, optimize=True, quality=level)

    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress images in the current directory')
    parser.add_argument('-l', '--level', default=50, help='Compression level (0-100), default: 50')
    parser.add_argument('-f', '--file', help='File to compress')
    args = parser.parse_args()
    
    
    if args.file:
        # compress a single file
        if os.path.isfile(args.file) and args.file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            outfile = os.path.splitext(args.file)[0] + '_compressed' + os.path.splitext(args.file)[1]
            compress_image(args.file, outfile, args.level)
            print(f'{args.file} compressed as {outfile}')
        else: 
            print(f'{args.file} is not a valid image file')

    else:
        # compress all images in the current directory
        files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith(('.png', '.jpg','.jpeg','.gif'))]
        for f in files:
            outfile = os.path.splitext(f)[0] + '_compressed' + os.path.splitext(f)[1]
            compress_image(f, outfile, args.level)
        print('All images compressed')