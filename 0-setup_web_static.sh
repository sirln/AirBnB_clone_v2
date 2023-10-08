#!/usr/bin/env bash
# ---- Updating package list ----
sudo apt-get update
# ---- Installing ngix web server ----
sudo apt-get -y install nginx

# ---- Creating folders /data/web_static/releases/test/
# and /data/web_static/shared/ if they don’t already exist ----
sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# ---- Creating a fake HTML file ----
echo -e "<html>
  <head>
  </head>
  <body>
    You can also find me <a href='https://www.sirlawren.com'>here</a>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# ---- Creating a symbolic link ----
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# ---- Assigning /data directory ownership to ubuntu user & group ----
sudo chown -R ubuntu:ubuntu /data/

# ---- Updating the Nginx Configuration ----
FILE="/etc/nginx/sites-available/default"
ALIAS="/data/web_static/current/;"
STATIC="location /hbnb_static {\n\t\t\talias $ALIAS \n\t}"
if ! sudo grep "hbnb_static" "$FILE"; then
    sudo sed -i "/^\s*server_name.*;/a \\\n\t$STATIC" "$FILE"
fi

# Restart Nginx
sudo service nginx restart

# ---- Message if Nginx configuration update complete ----
echo "--------------------------------------"
echo "| Nginx configuration update complete |"
echo "--------------------------------------"
