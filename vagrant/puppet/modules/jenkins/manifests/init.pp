# == Class: jenkins config
#
# Performs jenkins configuration tasks for all Vagrant boxes.
#

class jenkins {

  exec { 'install default jre':
    path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'sudo apt install default-jre -y',
    user    => 'root',
    notify  => Exec['add jenkins GPG key']
  }

  exec { 'add jenkins GPG key':
    path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -',
    user    => 'root',
    refreshonly => true,
    notify  => Exec['add jenkins Aot source to /etc/apt/sources.list.d/']
  }

  exec { 'add jenkins Aot source to /etc/apt/sources.list.d/':
    path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list',
    user    => 'root',
    refreshonly => true,
    notify  => Exec['apt-get update']
  }

  exec { 'apt-get update':
    path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'sudo apt-get update',
    user    => 'root',
    refreshonly => true,
    notify  => Exec['apt-get install jenkins']
  }

  exec { 'apt-get install jenkins':
    path => '/usr/bin:/usr/sbin:/bin:/usr/local/bin',
    command => 'sudo apt-get install jenkins -y',
    user    => 'root',
  }
}
