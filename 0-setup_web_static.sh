#!/usr/bin/env bash
# Script that sets up the web servers for deployment

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create the folder /data/ if it doesn’t already exist
# Create the folder /data/web_static/ if it doesn’t already exist
# Create the folder /data/web_static/releases/ if it doesn’t already exist
# Create the folder /data/web_static/releases/test/ if it doesn’t already exist
# Create the folder /data/web_static/shared/ if it doesn’t already exist
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# Create a fake HTML file /data/web_static/releases/test/index.html
echo '<html>
  <head>
  </head>
  <body>
    Alx Software Engineering 2023
  </body>
</html>' > /data/web_static/releases/test/index.html

# Creating a symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Giving ownership of the /data/ folder to ubuntu user AND Group
sudo chown -hR ubuntu:ubuntu /data/

# Updating the Nginx Configuration
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart
