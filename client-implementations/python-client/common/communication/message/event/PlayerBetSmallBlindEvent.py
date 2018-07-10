#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayerBetSmallBlindEvent(TexasEvent):
    """ generated source for class PlayerBetSmallBlindEvent """
    player = None       # type: GamePlayer
    smallBlind = 0      # type: int

    def __init__(self, player, smallBlind):
        """ generated source for method __init__ """
        super(PlayerBetSmallBlindEvent, self).__init__()
        self.player = player
        self.smallBlind = smallBlind

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getSmallBlind(self):
        """ generated source for method getSmallBlind """
        return self.smallBlind

    def __str__(self):
        """ generated source for method toString """
        return "PlayerCalledEvent [player=" + self.player.getName() + ", smallBlind=" + str(self.smallBlind) + "]"

