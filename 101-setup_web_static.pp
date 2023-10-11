# Setting up the web servers for deployment of `web_static` application

# Ensure the package list is updated and Nginx is installed
exec { 'apt-update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => present,
  require => Exec['apt-update'],
}

# Ensure the required directories exist
file { ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0755',
}

# Create a fake HTML file for testing Nginx configuration
file { '/data/web_static/releases/test/index.html':
  ensure  => present,
  content => '<html><head><title>Test</title></head><body>You can also find me <a href='https://www.sirlawren.com'>here</a></body></html>',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0644',
}

# Ensure the symbolic link exists, pointing to the test release directory
file { '/data/web_static/current':
  ensure => link,
  target => '/data/web_static/releases/test/',
  force  => true, # This ensures the link is recreated if it exists
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Update Nginx configuration to serve the content
file_line { 'update_nginx_config':
  path  => '/etc/nginx/sites-available/default',
  line  => "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n",
  after => 'server_name _;',
  match => 'location /hbnb_static', # Ensures the line doesn't get added multiple times
  replace => "\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n",
}

# Ensure Nginx is running and enabled on boot
service { 'nginx':
  ensure => running,
  enable => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Restart Nginx if the config file changes
}
