#!/usr/bin/env python

import json


class TexasMessage(object):
    def __init__(self):
        self.version = ""

    def getType(self):
        """ generated source for method getType """
        return type(self).__name__

    def getModule(self):
        """ generated source for method getType """
        return type(self).__module__

    def getVersion(self):
        """ generated source for method getVersion """
        return self.version

    def setVersion(self, version):
        """ generated source for method setVersion """
        self.version = version

    def toJSON(self):
        self.type = self.getModule().replace("common.", "se.cygni.texasholdem.")
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

