# puppet script that sets up your web servers for deploymenta

exec { 'install nginx':
  command  => 'apt update && apt -y install nginx',
  provider => shell,
}

exec { 'make directories':
  command  => 'mkdir -p /data/web_static/releases/test/; mkdir -p /data/web_static/shared/',
  provider => shell,
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Holberton school',
  require => Exec['install nginx'],
}

exec { 'link':
  command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
  require  => Exec['make directories'],
  provider => shell,
}

exec { 'owner':
  command  => 'chown -R ubuntu:ubuntu /data/',
  require  => Exec['make directories'],
  provider => shell,
}


file {'/etc/nginx/sites-available/default':
  ensure   => file,
  content  => "
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html index.htm;
      location /hbnb_static {
      alias /data/web_static/current;
 	index index.html index.htm;
      }
      rewrite ^/redirect_me https://google.com;
      error_page 404 /404.html;
      location /404 {
  	root /var/www/html;
	internal;
      }
  }",
  require  => Exec['install nginx'],
}

exec { 'run':
  command  => 'service nginx restart',
  provider => shell,
}
