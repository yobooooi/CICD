# == Class: webserver config
#
# Performs webserver configuration tasks for all Vagrant boxes.
#
class webserver (
  $PATH='/usr/bin:/usr/sbin:/bin:/usr/local/bin',
  $HOME='/home/vagrant',
  $APP_DIR='/data/app'
  ){

  exec { 'install development pacakges':
    path    => "${PATH}",
    command => "sudo apt-get install -y make build-essential python3.5-dev",
    user    => 'vagrant',
    notify  => Exec['install virtualenv'],
    timeout => 720
  }

  exec {'install virtualenv':
    path    => "${PATH}",
    command => "sudo apt-get install virtualenv -y",
    user    => 'vagrant',
    timeout => 720,
    notify  => Exec['create virtual environment'],
  }

  exec {'create virtual environment':
    path    => "${PATH}",
    command => "virtualenv -p /usr/bin/python3 restapi",
    user    => 'vagrant',
    notify  => Exec['install python requirements']
  }

  exec {'install python requirements':
    path    => "${PATH}",
    command => "source restapi/bin/activate;
                pip install -r ${APP_DIR}/requirements.txt;
                deactivate",
    user    => 'vagrant'
    notify  => Exec['start app']
  }

  exec {'start app':
    path    => "${PATH}",
    command => "restapi/bin/python3 /data/app/run.py"
    user    => 'vagrant'
  }
}
