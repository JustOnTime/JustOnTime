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
pip install -r requirements.txt
nohup python3 application.py > /dev/null 2>&1 &
SCRIPT

Vagrant.configure("2") do |config|

  config.vm.provision "file", source: "application.py", destination: "$HOME/application.py"
  config.vm.provision "file", source: "requirements.txt", destination: "$HOME/requirements.txt"
  config.vm.provision "file", source: "static", destination: "$HOME/static"
  config.vm.provision "file", source: "templates", destination: "$HOME/templates"
  config.vm.provision "shell", inline: $script

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.provider :virtualbox do |virtualbox,override|

    override.vm.box = "ubuntu/bionic64"
    config.vm.network "forwarded_port", guest: 80, host: 5000

  end


  config.vm.provider :aws do |aws,override|

    override.vm.box = "dummy"

    aws.keypair_name = "id_rsa"
    aws.ami = "ami-46dee13f"
    aws.instance_type = "t2.micro"
    aws.elastic_ip = "34.247.95.242"
    aws.region = "eu-west-1"
    aws.subnet_id = "subnet-709f1838"
    aws.security_groups = ["sg-018775fbd35fb87ed"]
    aws.associate_public_ip = true

    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = "~/.ssh/id_rsa"
 end
end
