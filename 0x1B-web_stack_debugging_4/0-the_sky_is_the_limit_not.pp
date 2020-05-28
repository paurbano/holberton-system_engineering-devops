# Change files of nginxs to solve error failed (24: Too many open files)
# take from https://www.claudiokuenzler.com/blog/850/nginx-socket-failed-24-too-many-open-files

# change limit file /etc/default/nginx
file_line { 'IncreaseLimit':
line => 'ULIMIT="-n 4096"',
path => '/etc/default/nginx'
}

# change /etc/security/limits.conf

file_line {'limits':
  line => 'nginx  soft nofile 30000',
  path => '/etc/security/limits.conf'
}

file_line {'limits':
  line => 'nginx  hard nofile 50000',
  path => '/etc/security/limits.conf'
}

# how many files can be opened
file_line {'HowManyFiles':
line => 'worker_rlimit_nofile 30000;',
path => '/etc/nginx/nginx.conf'
}

exec {'restart':
path    => '/usr/bin/:/usr/sbin:/bin',
command => 'sudo service nginx restart'
}
