# Increase the hard and soft holberton user
exec { 'increase-hard-file-limits-for-holberton-user':
  command => "sed -i '/^holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}

exec { 'increase-soft-file-limits-for-holberton-user':
  command => "sed -i '/^holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/',
}