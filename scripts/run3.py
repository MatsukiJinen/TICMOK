#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import os
import uuid

import random
from jinja2 import Environment, FileSystemLoader
from random_generator_libs import specific_generator
import shutil
import uuid

x=sys.argv[1]
data=json.loads(x)

if not "filename" in data:
	exit()

if not "templates" in data:
	exit()

if data['templates'] == None:
	exit()

base_directory_path = os.path.dirname(os.path.abspath(__file__))
template_directory_path = "{}/random_generator_libs/template".format(base_directory_path)
zip_directory_path = base_directory_path.replace('scripts', 'storage')

env = Environment(loader=FileSystemLoader(template_directory_path, encoding='utf8'))
tpl = env.get_template('outline.tpl.html')

u4 = data['filename'] #str(uuid.uuid4()) 
work_dir_path = '{}/{}'.format(base_directory_path, u4);
if os.path.exists(work_dir_path):
	shutil.rmtree(work_dir_path)

shutil.copytree('{}/htmls'.format(base_directory_path), work_dir_path)

text = ""
for template in data['templates']:
	text += specific_generator.generate_html(template)

html = tpl.render({'text': text})

with open('{}/index.html'.format(work_dir_path), mode='w', encoding='utf-8') as f:
	f.write(html)

shutil.make_archive('{}/app/public/{}'.format(zip_directory_path, u4), 'zip', root_dir=work_dir_path)
shutil.rmtree(work_dir_path)
print(u4)
