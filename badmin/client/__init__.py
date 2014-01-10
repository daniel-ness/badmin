#!/usr/bin/env python

from twisted.internet.protocol import ClientFactory as BaseClientFactory
from twisted.internet.protocol import Protocol
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor


class Client(LineReceiver):
    """

    """
    def connectionMade(self):
        print "connection made"
        self.sendLine("HALLO")

    def lineReceived(self, line):
        print "receive: ", line
        self.transport.loseConnection()


class ClientFactory(BaseClientFactory):
    """

    """
    protocol = Client

    def clientConnectionFailed(self, connector, reason):
        print "connection failed: ", reason.getErrorMessage()
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print "connection lost: ", reason.getErrorMessage()
        reactor.stop()
