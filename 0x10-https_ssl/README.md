# 0x10. HTTPS SSL

# Tasks
## 0. HTTPS ABC
What is HTTPS?

* A secure version of HTTP
* A faster version of HTTP
* A superior version of HTTP
Why do you need HTTPS?

* To encrypt credit card and social security number information going between the client and the website servers
* To encrypt all communication between the client and the website servers
* To accelerate the communication between the client and the website servers
You want to setup HTTPS on your website, where shall you place the certificate?

* In a secure location where nobody can access it
* You can host it anywhere but you have to share the link to it on your website
* On your website web server(s)

# 1. World wide web
 write a Bash script that will display information about subdomains.

Requirements:

Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
Add the subdomain lb-01 to your domain, point it to your lb-01 IP
Add the subdomain web-01 to your domain, point it to your web-01 IP
Add the subdomain web-02 to your domain, point it to your web-02 IP
Your Bash script must accept 2 arguments:
domain:
type: string
what: domain name to audit
mandatory: yes
subdomain:
type: string
what: specific subdomain to audit
mandatory: no
Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
When passing domain and subdomain parameters, display information for the specified subdomain
Ignore shellcheck case SC2086
Must use:
awk
at least one Bash function
You do not need to handle edge cases such as:
Empty parameters
Nonexistent domain names
Nonexistent subdomains
Example:

    sylvain@ubuntu$ dig www.holberton.online | grep -A1 'ANSWER SECTION:'
    ;; ANSWER SECTION:
    www.holberton.online.   87  IN  A   54.210.47.110
    sylvain@ubuntu$ dig lb-01.holberton.online | grep -A1 'ANSWER SECTION:'
    ;; ANSWER SECTION:
    lb-01.holberton.online. 101 IN  A   54.210.47.110
    sylvain@ubuntu$ dig web-01.holberton.online | grep -A1 'ANSWER SECTION:'
    ;; ANSWER SECTION:
    web-01.holberton.online. 212    IN  A   34.198.248.145
    sylvain@ubuntu$ dig web-02.holberton.online | grep -A1 'ANSWER SECTION:'
    ;; ANSWER SECTION:
    web-02.holberton.online. 298    IN  A   54.89.38.100
    sylvain@ubuntu$
    sylvain@ubuntu$
    sylvain@ubuntu$ ./1-world_wide_web holberton.online
    The subdomain www is a A record and points to 54.210.47.110
    The subdomain lb-01 is a A record and points to 54.210.47.110
    The subdomain web-01 is a A record and points to 34.198.248.145
    The subdomain web-02 is a A record and points to 54.89.38.100
    sylvain@ubuntu$
    sylvain@ubuntu$ ./1-world_wide_web holberton.online web-02
    The subdomain web-02 is a A record and points to 54.89.38.100
    sylvain@ubuntu$