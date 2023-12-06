# This puppet
package {'nginx':
ensure   => installed,
name     => 'nginx',
provider => 'apt',
}

file {'/etc/nginx/sites-available/default':
    ensure  => present,
    mode    => '0644',
    content => "server {
            listen 80 default_server;
            listen [::]:80 default_server;

            server_name _;

            add_header X-Served-By \$hostname;
            location / {
                return 200 'Hello World!';
            }
            location /redirect_me {
                return 301 /redirect_me;
            }
}",
    notify  => Service['nginx'],
}

service {'nginx':
ensure  => running,
enable  => true,
require => Package['nginx']
}