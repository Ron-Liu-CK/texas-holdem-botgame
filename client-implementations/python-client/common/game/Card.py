#!/usr/bin/env python

from common.game.definitions.Rank import *
from common.game.definitions.Suit import *


class Card(object):
    """ generated source for class Card """
    rank = None     # type: Rank
    suit = None     # type: Suit
    table = {}      # type: dict[Suit, dict[Rank, Card]]
    suitTable = {}  # type: dict[Rank, Card]

    def __init__(self, rank, suit):
        """
        :param rank: Rank
        :param suit: Suit
        """
        self.rank = rank
        self.suit = suit

    def getRank(self):
        """
        :return: Rank
        """
        return self.rank

    def getSuit(self):
        """
        :return: Suit
        """
        return self.suit

    def hashCode(self):
        """ generated source for method hashCode """
        prime = 31
        result = 1
        result = prime * result + (0 if (self.rank == None) else self.rank.hashCode())
        result = prime * result + (0 if (self.suit == None) else self.suit.hashCode())
        return result

    def equals(self, obj):
        if obj == None:
            return False
        if self.__class__ != obj.__class__:
            return False

        other = obj
        if self.rank != other.rank:
            return False
        if self.suit != other.suit:
            return False

        return True

    def toShortString(self):
        """ generated source for method toShortString """
        return self.rank.getName() + self.suit.getShortName()

    def getNameForImage(self):
        """ generated source for method getNameForImage """
        return self.toShortString()

    def __str__(self):
        """ generated source for method toString """
        return self.rank.getName() + " of " + self.suit

    def __eq__(self, other):
        return self.equals(other)

    @staticmethod
    def valueOf(rank, suit):
        """
        :param rank: Rank
        :param suit: Suit
        """
        return Card.table[suit][rank]


for suitKey, suit in Suit.getLookup().iteritems():
    for rankKey, rank in Rank.getLookup().iteritems():
        Card.suitTable[rank] = Card(rank, suit)
    Card.table[suit] = Card.suitTable
