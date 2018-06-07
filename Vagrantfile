# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-SCRIPT

debconf-set-selections <<< 'mysql-server mysql-server/root_password password 12345'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 12345'

sudo apt-get update && sudo apt-get install -y mysql-server python3 libmysqlclient-dev
sudo systemctl restart mysql
sudo mysql -u root -p12345 -e "CREATE DATABASE justontime;"
sudo mysql -u root -p12345 -e "CREATE TABLE justontime.list (email VARCHAR(320));"

sudo apt-get install -y python3-setuptools python3-pip
sudo -H pip3 install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install flask mysqlclient
cd /vagrant &&  nohup python3 application.py > /dev/null 2>&1 &
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", inline: $script
end
