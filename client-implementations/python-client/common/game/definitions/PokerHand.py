#!/usr/bin/env python


class PokerHand:
    """ generated source for enum PokerHand """
    orderValue = int()
    name = str()
    cardsRequired = int()

    lookupTable = {}     # type: dict[str, PokerHand]

    def __init__(self, orderValue, name, cardsRequired):
        """ generated source for method __init__ """
        self.orderValue = orderValue
        self.name = name
        self.cardsRequired = cardsRequired
        PokerHand.lookupTable[name.upper().replace(" ", "_")] = self

    def getOrderValue(self):
        """ generated source for method getOrderValue """
        return self.orderValue

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getCardsRequired(self):
        """ generated source for method getCardsRequired """
        return self.cardsRequired

    @staticmethod
    def get(name):
        """ generated source for method get """
        return PokerHand.lookupTable[name.upper().replace(" ", "_")]

    @staticmethod
    def getLookup():
        return PokerHand.lookupTable


PokerHand.ROYAL_FLUSH = PokerHand(10, "Royal flush", 5)
PokerHand.STRAIGHT_FLUSH = PokerHand(9, "Straight flush", 5)
PokerHand.FOUR_OF_A_KIND = PokerHand(8, "Four of a kind", 4)
PokerHand.FULL_HOUSE = PokerHand(7, "Full house", 5)
PokerHand.FLUSH = PokerHand(6, "Flush", 5)
PokerHand.STRAIGHT = PokerHand(5, "Straight", 5)
PokerHand.THREE_OF_A_KIND = PokerHand(4, "Three of a kind", 3)
PokerHand.TWO_PAIRS = PokerHand(3, "Two pairs", 4)
PokerHand.ONE_PAIR = PokerHand(2, "One pair", 2)
PokerHand.HIGH_HAND = PokerHand(1, "High hand", 1)
PokerHand.NOTHING = PokerHand(0, "Nothing", 0)

