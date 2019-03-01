from PIL import Image
from io import BytesIO
import os
import glob
import shutil

def get_concat_v(im1, im2):
    dst = Image.new('RGB', (im1.width, im1.height + im2.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (0, im1.height))
    return dst

def get_concat(directory, dst_path):
	pngs = sorted(glob.glob('./{}/*'.format(directory)))
	first_file = pngs[0]

	shutil.copyfile(first_file, dst_path)

	for png in pngs[1:]:
		im1 = Image.open(dst_path)
		im2 = Image.open(png)
		get_concat_v(im1, im2).save(dst_path)

def delete_temporary_directory(directory):
	shutil.rmtree(directory)
