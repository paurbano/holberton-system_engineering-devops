# Change files of nginxs to solve error failed (24: Too many open files)
# take it from https://www.claudiokuenzler.com/blog/850/nginx-socket-failed-24-too-many-open-files

# change limit file /etc/default/nginx
exec { 'restart':
command => "sed -i 's/15/4096/g' /etc/default/nginx; sudo service nginx restart",
path    => ['/usr/bin/', '/usr/sbin', '/bin']
}
