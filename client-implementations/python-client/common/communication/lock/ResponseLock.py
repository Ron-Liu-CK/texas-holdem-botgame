#!/usr/bin/env python

from common.communication.message.response.TexasResponse import TexasResponse


class ResponseLock(object):
    """ generated source for class ResponseLock """
    requestId = str()
    response = TexasResponse()

    def __init__(self, requestId):
        """ generated source for method __init__ """
        self.requestId = requestId

    def getResponse(self):
        """ generated source for method getResponse """
        return self.response

    def setResponse(self, response):
        """ generated source for method setResponse """
        if response is None:
            raise Exception("Response is null")
        if not self.requestId == response.getRequestId():
            raise Exception("Response has wrong request ID")
        self.response = response

    def hashCode(self):
        """ generated source for method hashCode """
        prime = 31
        result = 1
        result = prime * result + (0 if (self.requestId is None) else self.requestId.hashCode())
        return result

    def equals(self, obj):
        """ generated source for method equals """
        if self == obj:
            return True
        if obj is None:
            return False
        if self.__class__ != obj.__class__:
            return False
        other = obj
        if self.requestId is None:
            if other.requestId is not None:
                return False
        elif not self.requestId == other.requestId:
            return False
        return True

    def __eq__(self, other):
        return self.equals(other)

    def __hash__(self):
        return self.hashCode()