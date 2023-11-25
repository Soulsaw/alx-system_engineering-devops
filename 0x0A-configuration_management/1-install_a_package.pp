# This puppet script permit to install flask
package{'Flask':
ensure   => installed,
name     => 'flask==2.1.0',
provider => 'pip3',
}
