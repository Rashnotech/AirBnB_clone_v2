# puppet script that sets up your web servers for deploymenta

exec { 'install nginx':
command => '/usr/bin/apt -y update; /usr/bin/apt -y install nginx',
}

exec { 'create directories':
command  => 'mkdir -p /data/web_static/releases/test/; mkdir -p /data/web_static/shared/',
provider => shell,
}

exec { 'write':
command  => 'echo "hello world!" | sudo tee /data/web_static/releases/test/index.html',
require  => Exec['install nginx'],
provider => shell,
}

exec { 'link':
command  => 'ln -sf /data/web_static/releases/test/ /data/web_static/current',
require  => Exec['create directories'],
provider => shell,
}

exec { 'change owner':
command  => 'chown -R ubuntu:ubuntu /data/',
require  => Exec['create directories'],
provider => shell,
}


exec {'configure server':
command  => 'printf %s "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	add_header X-Served-By $HOSTNAME;
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
}" > /etc/nginx/sites-available/default',
require  => Exec['install nginx'],
provider => shell,
}

exec { 'run':
command  => 'service nginx restart',
provider => shell,
}
