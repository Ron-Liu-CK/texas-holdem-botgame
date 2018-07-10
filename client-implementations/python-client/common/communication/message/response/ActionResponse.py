#!/usr/bin/env python

from common.game.Action import Action
from common.communication.message.response.TexasResponse import TexasResponse


class ActionResponse(TexasResponse):
    """ generated source for class ActionResponse """
    action = None       # type: Action

    def getAction(self):
        """ generated source for method getAction """
        return self.action

    def setAction(self, action):
        """ generated source for method setAction """
        self.action = action

