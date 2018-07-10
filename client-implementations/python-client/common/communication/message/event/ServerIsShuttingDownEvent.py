#!/usr/bin/env python

from TexasEvent import TexasEvent


class ServerIsShuttingDownEvent(TexasEvent):
    """ generated source for class ServerIsShuttingDownEvent """
    message = str()

    def __init__(self, message):
        """ generated source for method __init__ """
        super(ServerIsShuttingDownEvent, self).__init__()
        self.message = message

    def getMessage(self):
        """ generated source for method getMessage """
        return self.message

    def __str__(self):
        """ generated source for method toString """
        return "ServerIsShuttingDownEvent [message=" + self.message + "]"

