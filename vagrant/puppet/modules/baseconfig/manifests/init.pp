# == Class: baseconfig
#
# Performs initial configuration tasks for all Vagrant boxes.
#

class baseconfig {

  package { ['htop', 'tree', 'unzip', 'wget']:
    ensure => present;
  }
}
