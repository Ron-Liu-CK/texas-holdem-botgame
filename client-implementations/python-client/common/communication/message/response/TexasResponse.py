#!/usr/bin/env python

from common.communication.message.TexasMessage import TexasMessage


class TexasResponse(TexasMessage):
    """ generated source for class TexasResponse """
    requestId = str()

    def getRequestId(self):
        """ generated source for method getRequestId """
        return self.requestId

    def setRequestId(self, requestId):
        """ generated source for method setRequestId """
        self.requestId = requestId

