# puppet script that sets up your web servers for deploymenta

class web_static_setup {
  # Ensure Nginx is installed
  package { 'nginx':
    ensure => installed,
  }

  # Create necessary directories
  file { '/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }
  
  file { '/data/web_static/releases':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755'
  }

  file { '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }
  
  # Create a HTML file
  file { '/data/web_static/releases/test/index.html':
    ensure  => file,
    content => '<html><body>Holberton School.</body></html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  # Create or recreate symbolic link
  file { '/data/web_static/current':
    ensure =>link,
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  # Update Nginx configuration to serve content
  file { '/etc/nginx/sites-available/default':
    ensure  => file,
    content => "
      server {
        listen 80 default_server;
        server_name _;
        location /hbnb_static {
          alias /data/web_static/current;
        }
        location / {
          try_files \$uri \uri/ =404;
        }
      }
    ",
    notify  => Service['nginx'],
  }

  # Ensure Nginx service is running and restart on config change
  service { 'nginx':
    ensure => running,
    enable => true,
    hasrestart => true,
    require    => File['/etc/nginx/sites-available/default'],
  }
}

include web_static_setup
