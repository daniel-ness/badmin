#!/usr/bin/env python

import argparse

from twisted.internet.protocol import Factory
from twisted.internet import reactor

from badmin.client import ClientFactory
from badmin.server import Server


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="badmin -- public key manager for teams")
    parser.add_argument('mode', nargs='?', default='client', help="Either 'server' or 'client' (default: 'client')")

    args = parser.parse_args()

    if args.mode == 'client':
        reactor.connectTCP('localhost', 8000, ClientFactory())
        reactor.run()

    elif args.mode == 'server':
        factory = Factory()
        factory.protocol = Server

        reactor.listenTCP(8000, factory)
        reactor.run()

    else:
        raise argparse.ArgumentTypeError("'mode' should be 'client' or 'server'")
