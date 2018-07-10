#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerCheckedEvent(TexasEvent):
    player = None       # type: GamePlayer

    def __init__(self, player):
        """ generated source for method __init__ """
        super(PlayerCheckedEvent, self).__init__()
        self.player = player

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def __str__(self):
        """ generated source for method toString """
        return "PlayerCheckedEvent [player=" + self.player + "]"

