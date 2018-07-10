#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerBetBigBlindEvent(TexasEvent):
    """ generated source for class PlayerBetBigBlindEvent """
    player = None       # type: GamePlayer
    bigBlind = long()

    def __init__(self, player, bigBlind):
        """ generated source for method __init__ """
        super(PlayerBetBigBlindEvent, self).__init__()
        self.player = player
        self.bigBlind = bigBlind

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getBigBlind(self):
        """ generated source for method getBigBlind """
        return self.bigBlind

    def __str__(self):
        """ generated source for method toString """
        return "PlayerCalledEvent [player=" + self.player + ", bigBlind=" + self.bigBlind + "]"

