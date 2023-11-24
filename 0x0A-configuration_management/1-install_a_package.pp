#!/usr/bin/puppet

# Install Flask version 2.1.0 using pip3
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure that Werkzeug is installed with version 2.0.2
package { 'werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
}

