#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import random

path = "/home/docker-compose/nginx/html/static/saving_web"

tmp = '<html><head><meta charset="utf-8"><link rel="stylesheet" href="./common.css" /></head><body><div>';
for root, dirs, files in os.walk(path):
	for file in files:
		if(file.endswith('.html')):
			tmp += '<p><a target="_blank" href="./'+file+'">'+file+'</a></p>'


tmp += '</div></body></html>'
print(tmp)
f = open(path + '/index.htm','w')
f.write(tmp)

