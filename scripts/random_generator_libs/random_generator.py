#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import random

base_directory_path = os.path.dirname(os.path.abspath(__file__))
template_directory_path = "{}/template".format(base_directory_path)

def generate_html(dir_name, size = 1):
	paths = glob.glob('{}/output/{}/*'.format(template_directory_path, dir_name))
	flies =  random.sample(paths, size)

	text = ""
	for file in flies:
		with open(file, "r") as f:  #　txt形式の読み込み
			text += f.read()
		
		text += "\n"

	return text

def load_html(dir_name, tpl, output_dir_path):
	paths = sorted(glob.glob('{}/output/{}/*'.format(template_directory_path, dir_name)))

	text = ""
	for (index, file) in enumerate(paths):
		with open(file, "r") as f:  #　txt形式の読み込み
			text = f.read()

		html = tpl.render({'text': text})
		with open('{}/{:03d}.html'.format(output_dir_path, index), mode='w', encoding='utf-8') as f:
			f.write(html)

		text = "\n"

	return text
