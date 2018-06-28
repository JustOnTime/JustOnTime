#!/usr/bin/env bash

if [ -d "/home/vagrant" ]; then
  home="/home/vagrant"
else
  home="/home/ubuntu"
fi

source $home/venv/bin/activate

mysqldump -u root -p12345 --opt justontime > justontime.sql
aws s3 cp justontime.sql s3://justontime-backup/justontime.sql
