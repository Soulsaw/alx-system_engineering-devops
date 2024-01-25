# Increase the ULIMIT of the default fioe
exec { 'fix--for-nginx':
    # Modify the ULIMIT value
    command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
    # Sepecify the path for the sed command
    path    =>  '/usr/local/bin/:/bin/',
}

# Restart the nginx
exec { 'nginx-restart':
    # Restart the nginx service
    command =>  '/etc/init.d/nginx restart',
    # Specify the path for the init.d script
    path    =>  '/etc/init.d/',
}
