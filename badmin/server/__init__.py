#!/usr/bin/env python

from twisted.internet.protocol import (
    Factory,
    Protocol,
    )
from twisted.internet import reactor


class Server(Protocol):

    def dataReceived(self, data):
        """
        """
        self.transport.write("hiya")
