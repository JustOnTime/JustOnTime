#!/usr/bin/env bash

if [ -d "/vagrant" ]; then
  home="/vagrant"
else
  home="/home/ubuntu"
fi

debconf-set-selections <<< 'mysql-server mysql-server/root_password password 12345'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 12345'

apt-get update && sudo apt-get install -y mysql-server python3 libmysqlclient-dev
systemctl restart mysql
mysql -u root -p12345 -e "CREATE DATABASE justontime;"
mysql -u root -p12345 -e "CREATE TABLE justontime.list (email VARCHAR(320));"

apt-get install -y python3-setuptools python3-pip
pip3 install --upgrade pip
pip install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install -r $home/requirements.txt

echo "bootstrap - Loading db - start"
chmod +x $home/scripts/loaddb.sh
$home/scripts/loaddb.sh
echo "bootstrap - Loading db - end"

nohup python3 $home/application.py > /dev/null 2>&1 &

chmod +x $home/scripts/dumpdb.sh
crontab -l > mycron 2>/dev/null
echo "0 22 * * * $home/scripts/dumpdb.sh" >> mycron
crontab mycron
rm mycron
