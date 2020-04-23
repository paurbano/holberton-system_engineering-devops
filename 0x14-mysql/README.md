# 0x14. Mysql

# General
* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

## 0. Install MySQL
MySQL installed on both your web-01 and web-02 servers.

## 1. Let us in!
* Create a MySQL user named holberton_user on both web-01 and web-02 with the host name set to localhost and the password projectcorrection280hbtn. This will allow us to access the replication status on both servers.
* Make sure that holberton_user has permission to check the primary/replica status of your databases.

Example:

    ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "SHOW GRANTS FOR 'holberton_user'@'localhost'"
    Enter password:
    +-----------------------------------------------------------------+
    | Grants for holberton_user@localhost                             |
    +-----------------------------------------------------------------+
    | GRANT REPLICATION CLIENT ON *.* TO 'holberton_user'@'localhost' |
    +-----------------------------------------------------------------+
    ubuntu@229-web-01:~$

## 2. If only you could see what I've seen with your eyes
In order for you to set up replication, you’ll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.

    ubuntu@229-web-01:~$ mysql -uholberton_user -p -e "use tyrell_corp; select * from nexus6"
    Enter password:
    +----+-------+
    | id | name  |
    +----+-------+
    |  1 | Leon  |
    +----+-------+
    ubuntu@229-web-01:~$

## 3. Quite an experience to live in fear, isn't it?
On your primary MySQL server (web-01), create a new user for the replica server.

The name of the new user should be replica_user, with the host name set to %, and can have whatever password you’d like.
replica_user must have the appropriate permissions to replicate your primary MySQL server.
holberton_user will need SELECT privileges on the mysql.user table in order to check that replica_user was created with the correct permissions.

Example

    ubuntu@229-web-01:~$ mysql -uholberton_user -p -e 'SELECT user, Repl_slave_priv FROM mysql.user'
    +------------------+-----------------+
    | user             | Repl_slave_priv |
    +------------------+-----------------+
    | root             | Y               |
    | mysql.session    | N               |
    | mysql.sys        | N               |
    | debian-sys-maint | Y               |
    | holberton_user   | N               |
    | replica_user     | Y               |
    +------------------+-----------------+
    ubuntu@229-web-01:~$

## 4. Setup a Primary-Replica infrastructure using MySQL
Having a replica member on for your MySQL database has 2 advantages:

* Redundancy: If you lose one of the database servers, you will still have another working one and a copy of your data
* Load distribution: You can split the read operations between the 2 servers, reducing the load on the primary member and improving query response speed

## 5. MySQL backup
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.

Requirements:

* The MySQL dump must contain all your MySQL databases
* The MySQL dump must be named backup.sql
* The MySQL dump file has to be compressed to a tar.gz archive
* This archive must have the following name format: day-month-year.tar.gz
* The user to connect to the MySQL database must be root
* The Bash script accepts one argument that is the password used to connect to the MySQL database

File: [`5-mysql_backup`]