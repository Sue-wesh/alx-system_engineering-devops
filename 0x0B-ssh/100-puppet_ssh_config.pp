#set up client SSH configuration file to connect to a server without a passwd.
class { 'ssh':
  IdentityFile           => '~/.ssh/school'
  PasswordAuthentication => 'no'
}
