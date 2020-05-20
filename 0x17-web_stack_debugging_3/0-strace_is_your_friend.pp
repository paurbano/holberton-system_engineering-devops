# fix wordpress

exec {'rename_file':
  path    => '/var/www/html/wp-includes/'
  command => 'mv class-wp-locale.phpp class-wp-locale.php'
}
