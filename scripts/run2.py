#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import os
import uuid

import random
from jinja2 import Environment, FileSystemLoader
from random_generator_libs import random_generator
import shutil

base_directory_path = os.path.dirname(os.path.abspath(__file__))
template_directory_path = "{}/random_generator_libs/template".format(base_directory_path)

work_dir_path = '{}/{}'.format(base_directory_path, 'all');

env = Environment(loader=FileSystemLoader(template_directory_path, encoding='utf8'))

templates = ['call_to_action',
'contacts',
'contents',
'features',
'footers',
'forms',
'headers',
'pricings',
'teams',
'testimonials']

for template in templates:
	copy_src_path = '{}/htmls'.format(base_directory_path)
	output_dir_path = "{}/{}".format(work_dir_path, template)
	if not os.path.exists(output_dir_path):
		shutil.copytree(copy_src_path, output_dir_path)

	tpl = env.get_template('outline.tpl.html')
	text = random_generator.load_html(template, tpl, output_dir_path)