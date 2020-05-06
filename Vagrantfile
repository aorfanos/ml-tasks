Vagrant.configure("2") do |config|
  config.vm.box = "generic/centos7"
  config.ssh.insert_key = false
  config.vm.define "pam_limits" do |pam_limits|
     pam_limits.vm.hostname = "ulimit.test"
     pam_limits.vm.network :private_network, ip: "192.168.3.146"
     config.vm.provision :ansible do |ansible|
        ansible.compatibility_mode = "2.0"
        ansible.playbook = "/etc/ansible/ulimit_change.yml"
        ansible.inventory_path = "/etc/ansible/hosts"
        ansible.become = true
        ansible.extra_vars = { "hosts": "pam_limits" }
    end
  end 
end
