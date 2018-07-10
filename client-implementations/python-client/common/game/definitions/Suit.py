#!/usr/bin/env python


class Suit:
    shortName = ""
    longName = ""
    lookupTable = {}

    def __init__(self, shortName, longName):
        """
        :param shortName: str
        :param longName: str
        """
        self.shortName = shortName
        self.longName = longName
        Suit.lookupTable[longName.upper()] = self

    def getShortName(self):
        """ generated source for method getShortName """
        return self.shortName

    def getLongName(self):
        """ generated source for method getLongName """
        return self.longName

    def hashCode(self):
        try:
            return Suit.lookupTable.keys().index(self.longName) + 1
        except ValueError:
            return 0

    def __str__(self):
        """ generated source for method toString """
        return self.longName

    @staticmethod
    def get(name):
        """ generated source for method get """
        return Suit.lookupTable[name.upper()]

    @staticmethod
    def getLookup():
        return Suit.lookupTable


Suit.CLUBS = Suit("c", "Clubs")
Suit.DIAMONDS = Suit("d", "Diamonds")
Suit.HEARTS = Suit("h", "Hearts")
Suit.SPADES = Suit("s", "Spades")

