#!/usr/bin/env bash

# install nginx if not installed
sudo apt-get -y update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file for testing
echo "Hello, this is a test index page." | sudo tee /data/web_static/releases/test/index.html

# Create symbolic link if it doesn't exist, delete and recreate otherwise
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
config="location /hbnb_static/ {alias /data/web_static/current/; }"
sudo sed -i "/^server_name _;/a $config" /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

