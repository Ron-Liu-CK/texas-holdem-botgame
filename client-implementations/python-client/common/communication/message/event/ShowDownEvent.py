#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.PlayerShowDown import PlayerShowDown
from TexasEvent import TexasEvent


class ShowDownEvent(TexasEvent):
    """ generated source for class ShowDownEvent """
    playersShowDown = None    # type: list[PlayerShowDown]

    def __init__(self, playersShowDown):
        """ generated source for method __init__ """
        super(ShowDownEvent, self).__init__()
        self.playersShowDown = playersShowDown

    def getPlayersShowDown(self):
        """ generated source for method getPlayersShowDown """
        return self.playersShowDown

    def __str__(self):
        """ generated source for method toString """
        return "ShowDownEvent [playersShowDown=" + self.playersShowDown + "]"

