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

# 2. Show your Bash PID
Using previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.

Requirements:

* You cannot use pgrep
* The third line of your script must be # shellcheck disable=SC2009

    sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
    sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
    sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
    sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
    sylvain@ubuntu$

# 3. Show your Bash PID made easy
Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.

Requirements:

* You cannot use `ps`

# 4. To infinity and beyond
Write a Bash script that displays To infinity and beyond indefinitely.

Requirements:

* In between each iteration of the loop, add a `sleep 2`

# 5. Kill me now
We killed our 4-to_infinity_and_beyond process using ctrl+c in the previous task, there is actually another way to do this.

Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

* You must use `kill`

# 6. Kill me now made easy
Write a Bash script that kills 4-to_infinity_and_beyond process.

Requirements:

* You cannot use kill or killall

# 7. Highlander
Write a Bash script that displays:

* To infinity and beyond indefinitely
* With a sleep 2 in between each iteration
* I am invincible!!! when receiving a SIGTERM signal

Make a copy of your `6-kill_me_now_made_easy script`, name it `67-kill_me_now_made_easy`, that kills the `7-highlander` process instead of the `4-to_infinity_and_beyond` one.

# 8. Beheaded process
Write a Bash script that kills the process `7-highlander`.

Repo:

* GitHub repository: holberton-system_engineering-devops
* Directory: 0x05-processes_and_signals
* File: 8-beheaded_process

# 9. Process and PID file
Write a Bash script that:

* Creates the file `/var/run/holbertonscript.pid` containing its PID
* Displays `To infinity and beyond` indefinitely
* Displays `I hate the kill command` when receiving a SIGTERM signal
* Displays `Y U no love me?!` when receiving a SIGINT signal
* Deletes the file `/var/run/holbertonscript.pid` and terminates itself when receiving a SIGQUIT or SIGTERM signal


## Author - [Pablo Andres Urbano De la Cruz](paurbano@gmail.com)