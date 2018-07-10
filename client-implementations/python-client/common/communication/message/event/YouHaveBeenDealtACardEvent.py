#!/usr/bin/env python

from common.game.Card import Card
from TexasEvent import TexasEvent


class YouHaveBeenDealtACardEvent(TexasEvent):
    """ generated source for class YouHaveBeenDealtACardEvent """
    card = None       # type: Card

    def __init__(self, card):
        """ generated source for method __init__ """
        super(YouHaveBeenDealtACardEvent, self).__init__()
        self.card = card

    def getCard(self):
        """ generated source for method getCard """
        return self.card

    def __str__(self):
        """ generated source for method toString """
        return "YouHaveBeenDealtACardEvent [card=" + self.card.toShortString() + "]"

