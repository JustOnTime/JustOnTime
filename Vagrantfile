# -*- mode: ruby -*-
# vi: set ft=ruby :

$script = <<-SCRIPT
sudo apt-get update && sudo apt-get install -y mysql-server python3
sudo systemctl restart mysql
sudo /usr/bin/mysqladmin -u root password '12345'
sudo mysql -u root -p12345 -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '12345' WITH GRANT OPTION;"
sudo mysql -u root -p12345 -e "FLUSH PRIVILEGES;"
sudo systemctl restart mysql
sudo mysql -u root -p12345 -e "CREATE DATABASE justontime;"
sudo mysql -u root -p12345 -e "CREATE TABLE justontime.list (email VARCHAR(320));"

git clone https://github.com/JustOnTime/justontime.git && cd justontime

sudo apt-get install -y python3-setuptools python3-pip
sudo -H pip3 install --upgrade pip
sudo pip install --upgrade virtualenv
virtualenv -p python3 venv
source venv/bin/activate
pip install flask
python3 application.py &

SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  config.vm.network "forwarded_port", guest: 5000, host: 5000
  config.vm.provision "shell", inline: $script
end
