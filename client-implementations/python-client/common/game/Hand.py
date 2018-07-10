#!/usr/bin/env python

from common.game.definitions.PokerHand import *


class Hand(object):
    """ generated source for class Hand """
    cards = []
    pokerHand = None    # type: PokerHand
    folded = False      # type: bool

    def __init__(self, cards, pokerHand, folded = False):
        """ generated source for method __init__ """
        self.folded = folded
        self.cards = [] if folded else cards
        self.pokerHand = PokerHand.NOTHING if folded else pokerHand

    def getCards(self):
        """ generated source for method getCards """
        return self.cards

    def getPokerHand(self):
        """ generated source for method getPokerHand """
        return self.pokerHand

    def isFolded(self):
        """ generated source for method isFolded """
        return self.folded

