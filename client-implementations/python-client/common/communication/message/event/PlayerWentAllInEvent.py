#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerWentAllInEvent(TexasEvent):
    """ generated source for class PlayerWentAllInEvent """
    player = None       # type: GamePlayer
    allInAmount = long()

    def __init__(self, player, allInAmount):
        """ generated source for method __init__ """
        super(PlayerWentAllInEvent, self).__init__()
        self.player = player
        self.allInAmount = allInAmount

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getAllInAmount(self):
        """ generated source for method getAllInAmount """
        return self.allInAmount

    def __str__(self):
        """ generated source for method toString """
        return "PlayerWentAllInEvent [player=" + self.player + ", allInAmount=" + self.allInAmount + "]"

