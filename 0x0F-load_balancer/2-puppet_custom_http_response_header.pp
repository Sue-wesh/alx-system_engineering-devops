# automate the task of creating a custom HTTP header response with Puppet
# name of the custom HTTP header must be X-Served-By
# value of custom HTTP header is the hostname of server Nginx runs on
exec { 'nginx':
  command  => "sudo apt-get update;
  sudo apt-get -y install nginx;
  sudo sed -i '/listen 80 default-server;/a add_header X-Served-By $HOSTNAME;' /etc/nginx/sites-available/default;
  sudo service nginx restart",
  provider => shell,
}
