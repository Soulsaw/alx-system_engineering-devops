# kill the process name killmenow
exec {'killmenow':
path    => ['/usr/bin', '/usr/sbin'],
command => 'pkill killmenow',
}
