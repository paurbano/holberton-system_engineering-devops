# 0x13. Firewall
More Info
As explained in the web stack debugging guide, telnet is a very good tool to check if sockets are open with telnet IP PORT. For example, if you want to check if port 22 is open on web-02:

    sylvain@ubuntu$ telnet web-02.holberton.online 22
    Trying 54.89.38.100...
    Connected to web-02.holberton.online.
    Escape character is '^]'.
    SSH-2.0-OpenSSH_6.6.1p1 Ubuntu-2ubuntu2.8

    Protocol mismatch.
    Connection closed by foreign host.
    sylvain@ubuntu$
We can see for this example that the connection is successful: Connected to web-02.holberton.online.

Now let’s try connecting to port 2222:

    sylvain@ubuntu$ telnet web-02.holberton.online 2222
    Trying 54.89.38.100...
    ^C
    sylvain@ubuntu$
We can see that the connection never succeeds, so after some time I just use ctrl+c to kill the process.

This can be used not just for this exercise, but for any debugging situation where two pieces of software need to communicate over sockets.

Note that the school network is filtering outgoing connections (via a network-based firewall), so you might not be able to interact with certain ports on servers outside of the school network. To test your work on web-01, please perform the test from outside of the school network, like from your web-02 server. If you SSH into your web-02 server, the traffic will be originating from web-02 and not from the school’s network, bypassing the firewall.

# Warning!
Containers on demand cannot be used for this project (Docker container limitation)

Be very careful with firewall rules! For instance, if you ever deny port 22/TCP and log out of your server, you will not be able to reconnect to your server via SSH, and we will not be able to recover it. When you install UFW, port 22 is blocked by default, so you should unblock it immediately before logging out of your server.

## 0. Firewall ABC mandatory
Pick one answer for every question.

What is a firewall?

* A hardware security system
* A hardware or software security system
* A software security system
What are the 2 types of firewall:

* Soft and hard firewall
* Incoming and outgoing firewall
* Network and host-based firewall
What is the main function of a firewall?

* To filter incoming and outgoing network traffic
* To filter incoming and outgoing TCP traffic
* To filter outgoing traffic

File: [`0-firewall_ABC`](https://github.com/paurbano/holberton-system_engineering-devops/blob/master/0x13-firewall/0-firewall_ABC)

## 1. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

* The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
* Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
    * 22 (SSH)
    * 443 (HTTPS SSL)
    * 80 (HTTP)
Share the ufw commands that you used in your answer file

File: [`1-block_all_incoming_traffic_but`](https://github.com/paurbano/holberton-system_engineering-devops/blob/master/0x13-firewall/1-block_all_incoming_traffic_but)