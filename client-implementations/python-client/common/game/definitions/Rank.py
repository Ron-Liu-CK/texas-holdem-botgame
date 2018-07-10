#!/usr/bin/env python


class Rank:
    orderValue = 0
    name = ""
    lookupTable = {}     # type: dict[str, Rank]

    def __init__(self, orderValue, name):
        """ generated source for method __init__ """
        self.orderValue = orderValue
        self.name = name
        Rank.lookupTable[name.upper()] = self

    def getOrderValue(self):
        """ generated source for method getOrderValue """
        return self.orderValue

    def getName(self):
        """ generated source for method getName """
        return self.name

    def __str__(self):
        """ generated source for method toString """
        return self.name

    def hashCode(self):
        return self.getOrderValue()

    def compareTo(self, other):
        return ((self.getOrderValue() > other.getOrderValue()) - (self.getOrderValue() < other.getOrderValue()))

    @staticmethod
    def get(name):
        """ generated source for method get """
        return Rank.lookupTable[name.upper()]

    @staticmethod
    def getLookup():
        return Rank.lookupTable


Rank.DEUCE = Rank(2, "Deuce")
Rank.THREE = Rank(3, "Three")
Rank.FOUR = Rank(4, "Four")
Rank.FIVE = Rank(5, "Five")
Rank.SIX = Rank(6, "Six")
Rank.SEVEN = Rank(7, "Seven")
Rank.EIGHT = Rank(8, "Eight")
Rank.NINE = Rank(9, "Nine")
Rank.TEN = Rank(10, "Ten")
Rank.JACK = Rank(11, "Jack")
Rank.QUEEN = Rank(12, "Queen")
Rank.KING = Rank(13, "King")
Rank.ACE = Rank(14, "Ace")

