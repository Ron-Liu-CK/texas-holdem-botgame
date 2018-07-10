#!/usr/bin/env python

from TexasEvent import TexasEvent
from common.game.Card import Card


class CommunityHasBeenDealtACardEvent(TexasEvent):
    card = None     # type: Card

    def __init__(self, card):
        """ generated source for method __init__ """
        super(CommunityHasBeenDealtACardEvent, self).__init__()
        self.card = card

    def getCard(self):
        """ generated source for method getCard """
        return self.card

    def __str__(self):
        """ generated source for method toString """
        return "CommunityHasBeenDealtACardEvent [card=" + self.card.toShortString() + "]"

