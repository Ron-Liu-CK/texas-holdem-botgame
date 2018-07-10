#!/usr/bin/env python

from common.game.Card import Card
from common.game.definitions import *
from random import shuffle
from copy import deepcopy


class Deck(object):
    """ generated source for class Deck """
    protoDeck = []      # type: list[Card]
    cards = []          # type: list[Card]

    #  Initialize prototype deck
    def __init__(self, cards):
        """ generated source for method __init__ """
        self.cards = cards

    @classmethod
    def getShuffledDeck(cls):
        """ generated source for method getShuffledDeck """
        copyOfProtoDec = deepcopy(cls.getOrderedListOfCards())
        return Deck(shuffle(copyOfProtoDec))

    @classmethod
    def getOrderedListOfCards(cls):
        if len(cls.protoDeck):
            return cls.protoDeck

        for rank in Rank.Rank.getLookup().iteritems():
            for suit in Suit.Suit.getLookup().iteritems():
                cls.protoDeck.append(Card(rank, suit))

        return cls.protoDeck

    def getCardsLeft(self):
        """ generated source for method getCardsLeft """
        return len(self.cards)

    def getNextCard(self):
        """ generated source for method getNextCard """
        return self.cards.remove(0)

    def burn(self):
        """ generated source for method burn """
        self.cards.remove(0)
