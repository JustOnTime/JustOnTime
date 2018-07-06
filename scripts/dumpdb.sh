#!/usr/bin/env bash

source venv/bin/activate

mysqldump -u root -p12345 --opt justontime > justontime.sql
aws s3 cp justontime.sql s3://justontime-backup/justontime.sql
