#!/bin/bash

echo "Running apt-get"
sudo apt-get update
sudo apt-get install nginx supervisor build-essential python-dev python-pip mongodb libpq-dev -y

echo "Installing python requirements with pip"
sudo pip install -r /vagrant/requirements.txt

echo "Setting up nginx configuration"
sudo cp /vagrant/vagrant/files/nginx /etc/nginx/sites-enabled/default

echo "Restarting nginx"
sudo service nginx restart

echo "Done provisioning!"
