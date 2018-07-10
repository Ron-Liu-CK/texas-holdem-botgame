#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.definitions.PlayState import PlayState
from TexasEvent import TexasEvent


class TableChangedStateEvent(TexasEvent):
    """ generated source for class TableChangedStateEvent """
    state = None       # type: PlayState

    def __init__(self, state):
        """ generated source for method __init__ """
        super(TableChangedStateEvent, self).__init__()
        self.state = state

    def getState(self):
        """ generated source for method getState """
        return self.state

    def __str__(self):
        """ generated source for method toString """
        return "TableChangedStateEvent [state=" + self.state + "]"

