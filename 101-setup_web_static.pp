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
  command  => 'sudo apt update && sudo apt -y install nginx',
  provider => shell,
  require  => Package['nginx'],
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
}

file { $web_static_dir:
  ensure  => directory,
  recurse => true,
  require => File['/data/web_static/releases/test/index.html'],
}

file { $current_dir:
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
