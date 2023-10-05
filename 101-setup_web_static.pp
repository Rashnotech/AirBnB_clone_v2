# puppet script that sets up your web servers for deployment
include stdlib

package { 'nginx':
  ensure => installed,
}

exec { 'install nginx'
  command  => 'sudo apt update && sudo apt install -y nginx',
  provider => shell,
  require  => Package['nginx']
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    server_name _;
    root /var/www/html/;
    location /hbnb_static {
      alias /data/web_static/current;
    }
  }",
  require => Exec['install nginx'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Holberton School',
}

file { '/data/web_static':
  ensure  => directory,
  recurse => true,
  require => File['/data/web_static/releases/test/index.html'],
}

file { '/data/web_static/current':
  ensure  => link,
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => File['/data/web_static'],
}

service { 'nginx':
  ensure    => 'running'
  enable    => true,
  require   => [Package['nginx'], File['/etc/nginx/sites-available/default']],
  subscribe => File['/etc/nginx/sites-available/default'],
}
