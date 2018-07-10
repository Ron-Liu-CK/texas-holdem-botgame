#!/usr/bin/env python

import ActionType


class Action(object):
    def __init__(self, actionType, amount):
        """
        :type actionType: ActionType
        :type amount: long
        """
        self.actionType = actionType
        self.amount = amount

    def getActionType(self):
        """ generated source for method getActionType """
        return self.actionType

    def getAmount(self):
        """ generated source for method getAmount """
        return self.amount

    def __str__(self):
        """ generated source for method toString """
        return "Action [actionType=" + self.actionType + ", amount=" + self.amount + "]"

