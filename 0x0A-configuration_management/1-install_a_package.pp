# Install specific version of Werkzeug
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

# Install Flask with version 2.1.0
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
