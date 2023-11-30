# This puppet
package {'nginx':
ensure   => installed,
name     => 'nginx',
provider => 'apt',
}

file {'/etc/nginx/sites-available/default':
    ensure  => file,
    mode    => '0644',
    content => "server {
            listen 80 default server;
            listen [::]:80;

            location / {
                return 200 'Hello word!';
            }
            location /redirect_me {
                return 301 /redirect_me;
            }
    }",
    notify  => Service['nginx'],
}

file {'/etc/nginx/sites-available/default':
    ensure => link,
    target => '/etc/nginx/sites-available/default',
    notify => Service['nginx'],
}

file {'/etc/nginx/sites-available/default':
    ensure => absent,
}

service {'nginx':
ensure  => running,
enable  => true,
require => Package['nginx']
}