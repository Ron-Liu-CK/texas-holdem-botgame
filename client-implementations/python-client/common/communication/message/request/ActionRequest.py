#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.Action import Action
from common.communication.message.request.TexasRequest import TexasRequest


class ActionRequest(TexasRequest):
    """ generated source for class ActionRequest """
    possibleActions = []

    def __init__(self, possibleActions = []):
        """ generated source for method __init___0 """
        super(ActionRequest, self).__init__()
        self.possibleActions = possibleActions

    def getPossibleActions(self):
        """ generated source for method getPossibleActions """
        return self.possibleActions

    def setPossibleActions(self, possibleActions):
        """ generated source for method setPossibleActions """
        self.possibleActions = possibleActions

