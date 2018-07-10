#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerCalledEvent(TexasEvent):
    """ generated source for class PlayerCalledEvent """
    player = None       # type: GamePlayer
    callBet = long()

    def __init__(self, player, callBet):
        """ generated source for method __init__ """
        super(PlayerCalledEvent, self).__init__()
        self.player = player
        self.callBet = callBet

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getCallBet(self):
        """ generated source for method getCallBet """
        return self.callBet

    def __str__(self):
        """ generated source for method toString """
        return "PlayerCalledEvent [player=" + self.player + ", callBet=" + self.callBet + "]"

