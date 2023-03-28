0x0C. Web server

Tasks
0. Transfer a file to your server
Write a Bash script that transfers a file from our client to a server:

Requirements:

Accepts 4 parameters
The path to the file to be transferred
The IP of the server we want to transfer the file to
The username scp connects with
The path to the SSH private key that scp uses
Display Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY if less than 3 parameters passed
scp must transfer the file to the user home directory ~/
Strict host key checking must be disabled when using scp


In this example, I:

remotely execute the ls ~/ command via ssh to see what ~/ contains
create a file named some_page.html
execute my 0-transfer_file script
remotely execute the ls ~/ command via ssh to see that the file some_page.html has been successfully transferred
That is one way of publishing your website pages to your server.
