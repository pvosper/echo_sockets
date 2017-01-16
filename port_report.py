#!/usr/bin/env python3

"""Optional Tasks:
---------------

Simple:

* Write a python function that lists the services provided by a given range of
  ports.

    * accept the lower and upper bounds as arguments
    * provide sensible defaults
    * Ensure that it only accepts valid port numbers (0-65535)

    21: File Transfer Protocol (FTP)
    22: Secure Shell (SSH)
    23: Telnet remote login service
    25: Simple Mail Transfer Protocol (SMTP)
    53: Domain Name System (DNS) service
    80: Hypertext Transfer Protocol (HTTP) used in the World Wide Web
    110: Post Office Protocol (POP3)
    119: Network News Transfer Protocol (NNTP)
    123: Network Time Protocol (NTP)
    143: Internet Message Access Protocol (IMAP)
    161: Simple Network Management Protocol (SNMP)
    194: Internet Relay Chat (IRC)
    443: HTTP Secure (HTTPS)

"""

def port_report(lower = 21, upper = 80):
    for port in range(lower, upper):
        # serv = 'open'
        try:
            serv = socket.getservbyport(port)
        except:
            continue
        print("Port: {}\t{}".format(port, serv))

if __name__ == '__main__':
    port_report()