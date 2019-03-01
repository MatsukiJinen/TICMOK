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
