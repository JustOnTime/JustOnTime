# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.trigger.before :destroy do |trigger|
    trigger.warn = "Dumping database"
    trigger.run_remote = {path: "scripts/dumpdb.sh"}
  end

  config.vm.define "dev" do |dev|

    dev.vm.provider :virtualbox do |virtualbox,override|

      dev.vm.provision "dev_provisioner", type: "shell", path: "bootstrap.sh"

      dev.vm.box = "ubuntu/bionic64"
      dev.vm.network "forwarded_port", guest: 80, host: 5000
      dev.vm.synced_folder "~/.aws", "/root/.aws"
      dev.vm.network "private_network", type: "dhcp"

    end
  end

  config.vm.define "prod" do |prod|

    prod.vm.provider :aws do |aws,override|

      prod.vm.provision "file", source: "application.py", destination: "$HOME/application.py"
      prod.vm.provision "file", source: "requirements.txt", destination: "$HOME/requirements.txt"
      prod.vm.provision "file", source: "static", destination: "$HOME/static"
      prod.vm.provision "file", source: "templates", destination: "$HOME/templates"
      prod.vm.provision "file", source: "scripts", destination: "$HOME/scripts"
      prod.vm.provision "prod_provisioner", type: "shell", path: "bootstrap.sh"

      prod.vm.synced_folder ".", "/vagrant", disabled: true

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
