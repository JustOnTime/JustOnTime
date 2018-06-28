#!/usr/bin/env bash

if [ -d "/home/vagrant" ]; then
  home="/home/vagrant"
else
  home="/home/ubuntu"
fi

source $home/venv/bin/activate

aws s3 cp s3://justontime-backup/justontime.sql justontime.sql
mysql -u root -p12345 justontime < justontime.sql
