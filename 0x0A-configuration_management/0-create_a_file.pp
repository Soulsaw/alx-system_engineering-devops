# This puppet script permit to create a file in the tmp folder
file{'/tmp/school':
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => 'I love Puppet',
}
