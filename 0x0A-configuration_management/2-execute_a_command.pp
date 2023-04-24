# create using puppet manifest that kills process killmenow

exec { 'pkill -x killmenow':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
