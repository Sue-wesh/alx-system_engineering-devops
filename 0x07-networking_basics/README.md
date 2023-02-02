0x07. Networking basics #0

0. OSI model
What is the OSI model?
How is the OSI model organized?

1. Types of network
What type of network a computer in local is connected to?
What type of network could connect an office in one building to another office in a building a few streets away?
What network do you use when you browse www.google.com from your smartphone (not connected to the Wifi)?

2. MAC and IP address
What is a MAC address?
What is an IP address?

3. UDP and TCP
TCP
It is a protocol that is transferring data in a slow way but surely
UDP
It is a protocol that is transferring data in a fast way and might loss data along in the process
TCP checking
Have you received boxes x, y, z?

4. TCP and UDP ports
Bash script that displays listening ports:

That only shows listening sockets
That shows the PID and name of the program to which each socket belongs

5. Is the host on the network
Bash script that pings an IP address passed as an argument.

Requirements:

Accepts a string as an argument
Displays Usage: 5-is-the-host-on-the-network {IP-ADDRESS} if no argument passed
Ping the IP 5 times
