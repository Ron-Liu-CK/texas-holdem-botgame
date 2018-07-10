#!/usr/bin/env python

from functools import wraps
from threading import RLock
from common.communication.lock.ResponseLock import ResponseLock


def lock_for_object(obj, locks={}):
    return locks.setdefault(id(obj), RLock())


def synchronized(call):
    assert call.__code__.co_varnames[0] in ['self', 'cls']
    @wraps(call)
    def inner(*args, **kwds):
        with lock_for_object(args[0]):
            return call(*args, **kwds)
    return inner


class SyncMessageResponseManager(object):
    """ generated source for class SyncMessageResponseManager """
    mapLock = {}
    responseLocks = {}

    def push(self, requestId):
        """ generated source for method push """
        lock = ResponseLock(requestId)
        if self.responseLocks[requestId]:
            raise Exception("Request ID is already in use")
        with lock_for_object(self.mapLock):
            self.responseLocks[requestId] = lock

        return lock

    def pop(self, requestId):
        """ generated source for method pop """
        if not self.responseLocks[requestId]:
            raise Exception("Unknown Request ID")

        lock = None
        with lock_for_object(self.mapLock):
            lock = self.responseLocks[requestId]
            del self.responseLocks[requestId]

        return lock

