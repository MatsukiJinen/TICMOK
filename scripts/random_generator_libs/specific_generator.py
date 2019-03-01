#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob
import random

base_directory_path = os.path.dirname(os.path.abspath(__file__))
template_directory_path = "{}/template".format(base_directory_path)

def generate_html(template):
	dir_name = template['key']
	number = template['value']

	path = '{}/output/{}/{:03d}.html'.format(template_directory_path, dir_name, number)
	with open(path, "r") as f:  #　txt形式の読み込み
		text = f.read()
		text += "\n"

	return text
