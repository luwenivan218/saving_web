#!/bin/sh

. /etc/profile
. ~/.bash_profile
cd /home/docker-compose/nginx/html/static/saving_web;
git pull;
python changeToHtml.py;
