#set up client SSH configuration file to connect to a server without a passwd.
include stdlib

file_line { 'passwd auth':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace => true,
}

file_line { 'config private key':
  ensure  => present,
  path    => 'etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}
