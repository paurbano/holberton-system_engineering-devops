# Change files of nginxs to solve error failed (24: Too many open files)
# take it from https://www.claudiokuenzler.com/blog/850/nginx-socket-failed-24-too-many-open-files

# change limit file /etc/default/nginx
file_line { 'IncreaseLimit':
line => 'ULIMIT="-n 4096"',
path => '/etc/default/nginx'
}

exec { 'restart':
command => 'sudo service nginx restart',
path    => ['/usr/bin/','/usr/sbin','/bin']
}
