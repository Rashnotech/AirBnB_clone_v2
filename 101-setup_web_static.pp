# puppet script that sets up your web servers for deployment
include stdlib

$web_static_dir = '/data/web_static'
$test_dir = "${web_static_dir}/releases/test"
$shared_dir = "${web_static_dir}/shared"
$current_dir = "${web_static_dir}/current"

package { 'nginx':
  ensure => installed,
}

exec { 'install nginx':
  command  => 'apt update && apt -y install nginx',
  provider => shell,
  require  => Package['nginx'],
}

exec { 'directory':
  command  => "mkdir -p $web_static_dir $current_dir $shared_dir $test_dir",
  provider => shell,
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "server {
    listen 80 default_server;
    server_name _;
    root /var/www/html;
    location /hbnb_static {
      alias /data/web_static/current;
    }
  }",
  require => Exec['install nginx'],
}

file { '/data/web_static/releases/test/index.html':
  ensure  => file,
  content => 'Holberton School',
  require => Exec['directory'],
}

exec { 'link':
  command    => "ln -sF $test_dir $current_dir",
  provider   => shell,
}

exec { 'change owner':
  command    => 'chown -R ubuntu:ubuntu /data/',
  require    => Exec['directory'],
  provider   => shell,
}

exec { 'run':
  command  => 'service nginx restart',
  provider => shell,
}
