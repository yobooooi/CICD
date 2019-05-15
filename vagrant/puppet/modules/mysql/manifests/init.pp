# == Class: jenkins config
#
# Performs jenkins configuration tasks for all Vagrant boxes.
#

class mysql(
  $USERNAME='admin',
  $PASSWORD='password',
  ){

  exec {'setting user name and password in deb-conf':
    path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    environment => [ "DEBIAN_FRONTEND=noninteractive" ],
    command => "sudo -E apt-get -q -y install mysql-server",
    user    => 'root',
    notify  => Exec['install mysql']
  }

  exec { 'install mysql':
    path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'sudo apt install mysql-server -y',
    user    => 'root',
    notify  => Exec['configure mysql']
  }

  exec { 'configure mysql':
    path    => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'mysql_secure_installation',
    user    => 'root'
  }

}
