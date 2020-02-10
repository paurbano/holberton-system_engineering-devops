# 0x05. Processes and signals

### man or help:

* ps
* pgrep
* pkill
* kill
* exit
* trap

# Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
* What is a PID
* What is a process
* How to find a process’ PID
* How to kill a process
* What is a signal
* What are the 2 signals that cannot be ignored

# 0. What is my PID
Write a Bash script that displays its own PID.

    sylvain@ubuntu$ ./0-what-is-my-pid
    4120
    sylvain@ubuntu$

Repo:

* GitHub repository: holberton-system_engineering-devops
* Directory: 0x05-processes_and_signals
* File: 0-what-is-my-pid

# 1. List your processes mandatory
Write a Bash script that displays a list of currently running processes.

Requirements:

* Must show all processes, for all users, including those which might not have a TTY
* Display in a user-oriented format
* Show process hierarchy

### Repo:

* GitHub repository: holberton-system_engineering-devops
* Directory: 0x05-processes_and_signals
* File: 1-list_your_processes