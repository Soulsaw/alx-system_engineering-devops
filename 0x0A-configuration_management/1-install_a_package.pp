# This puppet script permit to install flask
package{'Flask':
ensure   => '2.1.0',
name     => 'flask',
provider => 'pip3',
}
