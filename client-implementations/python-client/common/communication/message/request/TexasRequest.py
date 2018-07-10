#!/usr/bin/env python

from common.communication.message.TexasMessage import TexasMessage
import uuid


class TexasRequest(TexasMessage):
    """ generated source for class TexasRequest """
    sessionId = ""
    requestId = ""

    def __init__(self):
        self.sessionId = ""
        self.requestId = str(uuid.uuid4())

    def getSessionId(self):
        """ generated source for method getSessionId """
        return self.sessionId

    def setSessionId(self, sessionId):
        """ generated source for method setSessionId """
        self.sessionId = sessionId

    def getRequestId(self):
        """ generated source for method getRequestId """
        return self.requestId

    def setRequestId(self, requestId):
        """ generated source for method setRequestId """
        self.requestId = requestId

