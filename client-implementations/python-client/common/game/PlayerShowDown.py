#!/usr/bin/env python

import GamePlayer
import Hand


class PlayerShowDown(object):
    """ generated source for class PlayerShowDown """
    player = None       # type: GamePlayer
    hand = None         # type: Hand
    wonAmount = None    # type: int

    def __init__(self, player, hand, wonAmount):
        """ generated source for method __init__ """
        self.player = player
        self.hand = hand
        self.wonAmount = wonAmount

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def getHand(self):
        """ generated source for method getHand """
        return self.hand

    def getWonAmount(self):
        """ generated source for method getWonAmount """
        return self.wonAmount

