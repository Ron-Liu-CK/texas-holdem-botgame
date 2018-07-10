#!/usr/bin/env python

from TexasEvent import TexasEvent


class YouWonAmountEvent(TexasEvent):
    """ generated source for class YouWonAmountEvent """
    wonAmount = None            # type: long
    yourChipAmount = None       # type: long

    def __init__(self, wonAmount, yourChipAmount):
        """ generated source for method __init__ """
        super(YouWonAmountEvent, self).__init__()
        self.wonAmount = wonAmount
        self.yourChipAmount = yourChipAmount

    def getWonAmount(self):
        """ generated source for method getWonAmount """
        return self.wonAmount

    def getYourChipAmount(self):
        """ generated source for method getYourChipAmount """
        return self.yourChipAmount

    def __str__(self):
        """ generated source for method toString """
        return "YouWonAmountEvent [wonAmount=" + self.wonAmount + ", yourChipAmount=" + self.yourChipAmount + "]"

