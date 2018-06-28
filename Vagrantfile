# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.provision "file", source: "application.py", destination: "$HOME/application.py"
  config.vm.provision "file", source: "requirements.txt", destination: "$HOME/requirements.txt"
  config.vm.provision "file", source: "static", destination: "$HOME/static"
  config.vm.provision "file", source: "templates", destination: "$HOME/templates"
  config.vm.provision "file", source: "scripts", destination: "$HOME/scripts"
  config.vm.provision "shell", path: "bootstrap.sh"

  config.vm.synced_folder ".", "/vagrant", disabled: true

  config.vm.define "dev" do |dev|

    dev.vm.provider :virtualbox do |virtualbox,override|

      dev.vm.box = "ubuntu/bionic64"
      dev.vm.network "forwarded_port", guest: 80, host: 5000
      dev.vm.synced_folder "~/.aws", "/root/.aws"

    end
  end

  config.vm.define "prod" do |prod|

    prod.vm.provider :aws do |aws,override|

      prod.vm.box = "dummy"

      aws.keypair_name = "id_rsa"
      aws.ami = "ami-46dee13f"
      aws.instance_type = "t2.micro"
      aws.elastic_ip = "34.247.95.242"
      aws.region = "eu-west-1"
      aws.subnet_id = "subnet-709f1838"
      aws.security_groups = ["sg-018775fbd35fb87ed"]
      aws.associate_public_ip = true
      aws.iam_instance_profile_name = "AmazonS3FullAccess"

      override.ssh.username = "ubuntu"
      override.ssh.private_key_path = "~/.ssh/id_rsa"

   end
 end

end
