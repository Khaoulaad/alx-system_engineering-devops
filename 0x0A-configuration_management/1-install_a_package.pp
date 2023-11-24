#!/usr/bin/puppet

# Install the latest version of Flask and Werkzeug using pip3
package { 'flask':
  ensure   => 'latest',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
}

