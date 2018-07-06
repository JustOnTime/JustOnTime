#!/usr/bin/env bash

source venv/bin/activate

aws s3 cp s3://justontime-backup/justontime.sql justontime.sql
mysql -u root -p12345 justontime < justontime.sql
