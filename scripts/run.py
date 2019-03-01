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

x=sys.argv[1]
data=json.loads(x)

if not "filename" in data:
	exit()

base_directory_path = os.path.dirname(os.path.abspath(__file__))
template_directory_path = "{}/random_generator_libs/template".format(base_directory_path)
zip_directory_path = base_directory_path.replace('scripts', 'storage')

env = Environment(loader=FileSystemLoader(template_directory_path, encoding='utf8'))
tpl = env.get_template('outline.tpl.html')

numbers = 10
if 'numbers' in data.keys():
	if isinstance(data['numbers'], int):
		numbers = data['numbers']

u4 = data['filename'] #str(uuid.uuid4()) 
work_dir_path = '{}/{}'.format(base_directory_path, u4);
# shutil.rmtree(work_dir_path)

shutil.copytree('{}/htmls'.format(base_directory_path), work_dir_path)

for index in range(1, numbers + 1):
	# header = random_generator.generate_html('headers')
	# footer = random_generator.generate_html('footers')

	text = ""
	for template in data['templates']:
		text += random_generator.generate_html(template, 1)
		# text += random_generator.generate_html('features')
		# text += random_generator.generate_html('contents', 2)
		# text += random_generator.generate_html('testimonials')
		# text += random_generator.generate_html('pricings')
		# text += random_generator.generate_html('teams')

		# directory_name = random.choice(['contacts', 'call_to_action', 'forms'])
		# text += random_generator.generate_html(directory_name)

	html = tpl.render({'text': text})

	with open('{}/sample{:02d}.html'.format(work_dir_path, index), mode='w', encoding='utf-8') as f:
		f.write(html)

shutil.make_archive('{}/app/public/{}'.format(zip_directory_path, u4), 'zip', root_dir=work_dir_path)
shutil.rmtree(work_dir_path)
print(u4)
