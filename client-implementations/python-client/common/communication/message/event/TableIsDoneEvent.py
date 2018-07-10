#!/usr/bin/env python

from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class TableIsDoneEvent(TexasEvent):
    """ generated source for class TableIsDoneEvent """
    players = None        # type: list[GamePlayer]

    def __init__(self, players):
        """ generated source for method __init__ """
        super(TableIsDoneEvent, self).__init__()
        self.players = players

    def getPlayers(self):
        """ generated source for method getPlayers """
        return self.players

    def __str__(self):
        """ generated source for method toString """
        return "TableIsDoneEvent [players=" + self.players + "]"

