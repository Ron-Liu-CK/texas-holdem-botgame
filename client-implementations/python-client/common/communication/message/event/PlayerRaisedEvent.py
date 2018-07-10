#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerRaisedEvent(TexasEvent):
    """ generated source for class PlayerRaisedEvent """
    player = None       # type: GamePlayer
    raiseBet = long()

    def __init__(self, player, raiseBet):
        """ generated source for method __init__ """
        super(PlayerRaisedEvent, self).__init__()
        self.player = player
        self.raiseBet = raiseBet

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getRaiseBet(self):
        """ generated source for method getRaiseBet """
        return self.raiseBet

    def __str__(self):
        """ generated source for method toString """
        return "PlayerRaisedEvent [player=" + self.player + ", raiseBet=" + self.raiseBet + "]"

