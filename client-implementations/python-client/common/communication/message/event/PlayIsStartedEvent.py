#!/usr/bin/env python

from common.communication.message.type.IsATexasMessage import IsATexasMessage
from common.game.GamePlayer import GamePlayer
from TexasEvent import TexasEvent


class PlayIsStartedEvent(TexasEvent):
    """ generated source for class PlayIsStartedEvent """
    players = []
    smallBlindAmount = None         # type: int
    bigBlindAmount = None           # type: int
    dealer = None                   # type: GamePlayer
    smallBlindPlayer = None         # type: GamePlayer
    bigBlindPlayer = None           # type: GamePlayer
    tableId = None                  # type: int

    def __init__(self, players, smallBlindAmount, bigBlindAmount, dealer, smallBlindPlayer, bigBlindPlayer, tableId):
        """ generated source for method __init__ """
        super(PlayIsStartedEvent, self).__init__()
        self.players = players
        self.smallBlindAmount = smallBlindAmount
        self.bigBlindAmount = bigBlindAmount
        self.dealer = dealer
        self.smallBlindPlayer = smallBlindPlayer
        self.bigBlindPlayer = bigBlindPlayer
        self.tableId = tableId

    def getPlayers(self):
        """ generated source for method getPlayers """
        return self.players

    def getSmallBlindAmount(self):
        """ generated source for method getSmallBlindAmount """
        return self.smallBlindAmount

    def getBigBlindAmount(self):
        """ generated source for method getBigBlindAmount """
        return self.bigBlindAmount

    def getDealer(self):
        """ generated source for method getDealer """
        return self.dealer

    def getSmallBlindPlayer(self):
        """ generated source for method getSmallBlindPlayer """
        return self.smallBlindPlayer

    def getBigBlindPlayer(self):
        """ generated source for method getBigBlindPlayer """
        return self.bigBlindPlayer

    def getTableId(self):
        """ generated source for method getTableId """
        return self.tableId

    def __str__(self):
        """ generated source for method toString """
        return "PlayIsStartedEvent [tableId: #" + str(self.tableId) + "]"

