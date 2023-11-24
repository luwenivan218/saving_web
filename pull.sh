#!/bin/sh

. /etc/profile
. ~/.bash_profile
cd /home/docker-compose/nginx/html/static/saving_web;
git fetch --all &&  git reset --hard origin/master && git pull && python changeToHtml.py;
#git reset --hard HEAD
#git pull;
# python changeToHtml.py;
