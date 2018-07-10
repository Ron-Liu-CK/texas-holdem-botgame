#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerFoldedEvent(TexasEvent):
    """ generated source for class PlayerFoldedEvent """
    player = None       # type: GamePlayer
    investmentInPot = long()

    def __init__(self, player, investmentInPot):
        """ generated source for method __init__ """
        super(PlayerFoldedEvent, self).__init__()
        self.player = player
        self.investmentInPot = investmentInPot

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getInvestmentInPot(self):
        """ generated source for method getInvestmentInPot """
        return self.investmentInPot

    def __str__(self):
        """ generated source for method toString """
        return "PlayerFoldedEvent [player=" + self.player + ", investmentInPot=" + self.investmentInPot + "]"

