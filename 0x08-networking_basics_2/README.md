# 0x08. Networking basics #1

# General
* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

# 0. Localhost mandatory
What is localhost?

1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

# 1. All IPs mandatory
What is 0.0.0.0?

1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

# 2. Change your home IP mandatory
Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

* localhost resolves to 127.0.0.2
* facebook.com resolves to 8.8.8.8.
* The checker is running on Docker, so make sure to read this

# 3. Show attached IPs mandatory
Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Example:

    sylvain@ubuntu$ ./3-show_attached_IPs | cat -e
    10.0.2.15$
    127.0.0.1$
    sylvain@ubuntu$

# 4. Port listening on localhost
Write a Bash script that listens on port 98 on localhost.
