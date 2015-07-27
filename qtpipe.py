#! /usr/bin/env python3

"""Utility used for piping data over a network connection.

This program is designed to create a connection with another running instance
and pipe data from standard in to standard out. Run this program with either
-h or --help as a command line argument for further instructional material."""

__version__ = 1, 0, 1
__date__ = '27 July 2015'
__author__ = 'Stephen Paul Chappell'
__credits__ = '''Jacob Bridges, for inspiring this program via cutiepipe.
Please see https://github.com/jacobbridges/cutiepipe for more information.'''

import argparse
import os
import socket

BUFFER_SIZE = 1 << 12
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 10000
STANDARD_IN, STANDARD_OUT, STANDARD_ERROR = range(3)


def main():
    """Connect with another process and simulate a pipe over a network."""
    link = make_link()
    try:
        if os.isatty(STANDARD_IN):
            pipe_from_link_to_standard_out(link)
        else:
            pipe_from_standard_in_to_link(link)
    finally:
        link.shutdown(socket.SHUT_RDWR)
        link.close()


def make_link():
    """Create a client-server relationship to enable transfer of data."""
    address = parse_arguments()
    try:
        return socket.create_connection(address, 1)
    except (socket.gaierror, OverflowError) as error:
        raise_error(str(error))
    except (socket.timeout, ConnectionRefusedError):
        host, port = address
        if host != DEFAULT_HOST:
            raise_error('could not connect to "{}" computer'.format(host))
        else:
            server = create_server(port)
            server.settimeout(60)
            try:
                link, address = server.accept()
            except socket.timeout:
                raise_error('could not connect and did not receive any data')
            else:
                return link
            finally:
                server.close()


def parse_arguments():
    """Check the command line for arguments effecting program parameters."""
    parser = argparse.ArgumentParser(description='Pipe data over a network.')
    parser.add_argument('host', nargs='?', default=DEFAULT_HOST, type=str,
                        help='name of computer to link with')
    parser.add_argument('port', nargs='?', default=DEFAULT_PORT, type=int,
                        help='port used for the connection')
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {}.{}.{}'.format(*__version__))
    arguments = parser.parse_args()
    return arguments.host, arguments.port


def raise_error(message):
    """Convey error state in program to user and terminate execution."""
    os.write(STANDARD_ERROR, '\n{}\n'.format(message).encode('ascii'))
    raise SystemExit(1)


def create_server(port):
    """Construct a server waiting for a single incoming connection."""
    for family, kind, proto, _, address in socket.getaddrinfo(
            None, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0,
            socket.AI_PASSIVE):
        try:
            server = socket.socket(family, kind, proto)
        except OSError:
            pass
        else:
            try:
                server.bind(address)
                server.listen(1)
            except OSError:
                server.close()
            else:
                return server
    raise_error('could not create server socket')


def pipe_from_link_to_standard_out(link):
    """Collect all data from the socket and display it using standard out."""
    while True:
        buffer = link.recv(BUFFER_SIZE)
        if not buffer:
            break
        os.write(STANDARD_OUT, buffer)


def pipe_from_standard_in_to_link(link):
    """Communicate all data from standard in through the connected socket."""
    while True:
        buffer = os.read(STANDARD_IN, BUFFER_SIZE)
        if not buffer:
            break
        link.sendall(buffer)

if __name__ == '__main__':
    main()
