#set up client SSH configuration file to connect to a server without a passwd.
class { 'ssh':
  PrivateKey             => '~/.ssh/school'
  PasswordAuthentication => 'No'
}
