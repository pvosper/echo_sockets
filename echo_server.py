#!/usr/bin/env python3

"""
Internet Programming in Python: Session 01

Homework

Your homework assignment for this week is to take what you've learned here and
build a simple "echo" server.

The server should automatically return to any client that connects exactly what
it receives (it should echo all messages).

You will also write a python script that, when run, will send a message to the
server and receive the reply, printing it to stdout.

Finally, you'll do all of this so that it can be tested.

Notes:

    - Server will echo but not accumulate messages
    - KeyboardInterrupt works with control-c
    - More comments than code :-P

"""

import socket

import sys


def server(log_buffer=sys.stderr):
    # set an address for our server
    address = ('127.0.0.1', 10000)
    # xTODO: Replace the following line with your code which will instantiate
    #       a TCP socket with IPv4 Addressing, call the socket you make 'sock'
    # sock = None

    # socket family for IPV4 is "AF_INET"
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_IP)

    # xTODO: You may find that if you repeatedly run the server script it
    #   fails,
    #       claiming that the port is already used.  You can set an option on
    #       your socket that will fix this problem. We DID NOT talk about this
    #       in class. Find the correct option by reading the very end of the
    #       socket library documentation:
    #       http://docs.python.org/3/library/socket.html#example

    # "This is because the previous execution has left the socket in a
    #   TIME_WAIT state, and can’t be immediately reused.
    # There is a socket flag to set, in order to prevent this,
    #   socket.SO_REUSEADDR:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # s.bind((HOST, PORT))"

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # log that we are building a server
    print("making a server on {0}:{1}".format(*address), file=log_buffer)

    # xTODO: bind your new sock 'sock' to the address above and begin to listen
    #       for incoming connections

    sock.bind(address)

    sock.listen(1)

    try:
        # the outer loop controls the creation of new connection sockets. The
        # server will handle each incoming connection one at a time.
        while True:
            print('waiting for a connection', file=log_buffer)

            # xTODO: make a new socket when a client connects, call it 'conn',
            #       at the same time you should be able to get the address of
            #       the client so we can report it below.  Replace the
            #       following line with your code. It is only here to prevent
            #       syntax errors
            # addr = ('bar', 'baz')

            conn, addr = sock.accept()

            try:
                print('connection - {0}:{1}'.format(*addr), file=log_buffer)

                # the inner loop will receive messages sent by the client in
                # buffers.  When a complete message has been received, the
                # loop will exit
                while True:
                    # xTODO: receive 16 bytes of data from the client. Store
                    #       the data you receive as 'data'.  Replace the
                    #       following line with your code.  It's only here as
                    #       a placeholder to prevent an error in string
                    #       formatting
                    # data = b''

                    data = conn.recv(16)

                    print('received "{0}"'.format(data.decode('utf8')))

                    # xTODO: Send the data you received back to the client, log
                    # the fact using the print statement here.  It will help in
                    # debugging problems.

                    conn.sendall(data)

                    print('sent "{0}"'.format(data.decode('utf8')))

                    # xTODO: Check here to see if the message you've received
                    #   is
                    # complete.  If it is, break out of this inner loop.

                    if len(data) < 16:
                        break

            finally:
                # xTODO: When the inner loop exits, this 'finally' clause will
                #       be hit. Use that opportunity to close the socket you
                #       created above when a client connected.

                # sock.close()
                # If I close this here, it never gets re-established

                # @christy
                # Line 123 of echo_server - Looks like you were trying to
                #   close the socket here, but you should close the connection
                #   here (the conn variable).

                # This doesn't stop the tests from passing, but the server
                #   connection never closes.

                # Otherwise, looks good!

                conn.close()

                print(
                    'echo complete, client connection closed', file=log_buffer
                )

    except KeyboardInterrupt:
        # xTODO: Use the python KeyboardInterrupt exception as a signal to
        #       close the server socket and exit from the server function.
        #       Replace the call to `pass` below, which is only there to
        #       prevent syntax problems
        # pass

        sock.close()

        print('quitting echo server', file=log_buffer)


if __name__ == '__main__':
    server()
    sys.exit(0)
