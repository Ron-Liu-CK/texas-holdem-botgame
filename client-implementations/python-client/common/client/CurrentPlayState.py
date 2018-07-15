#!/usr/bin/env python

from common.communication.message.event import *
from common.communication.message.request.ActionRequest import ActionRequest
from common.game.Action import Action
from common.game.Card import Card
from common.game.PlayerShowDown import PlayerShowDown
from common.game.GamePlayer import GamePlayer
from common.game.definitions.PlayState import *
from common.player.Player import Player
import traceback
import sys

# 
#  * A helper for keeping tabs on the current state of a game round
#  
class CurrentPlayState(object):
    """ generated source for class CurrentPlayState """
    #  Values are reset per GameRound
    tableId = long()
    myCards = []
    communityCards = []
    currentPlayState = PlayStateInstance.PRE_FLOP
    foldedPlayers = []
    allInPlayers = []
    players = []
    potTotal = long()
    potInvestmentPerPlayer = []
    smallBlind = long()
    bigBlind = long()
    dealerPlayer = GamePlayer('', 0)
    smallBlindPlayer = GamePlayer('', 0)
    bigBlindPlayer = GamePlayer('', 0)

    #  Values that are kept between GameRounds
    myCurrentChipAmount = 0
    myPlayersName = str()

    def __init__(self, myPlayersName):
        """ generated source for method __init__ """
        self.myPlayersName = myPlayersName
        self.dummy = CurrentPlayStatePlayer(self)

    def getPlayerImpl(self):
        """ generated source for method getPlayerImpl """
        return self.dummy

    # 
    #      * The tableId is used to identify the table you are playing on. If you
    #      * want to inspect a game afterwards the whole game is available for viewing
    #      * here: http://poker.cygni.se/showgame/table/{tableId}
    #      *
    #      * @return The tableId for the current game
    #      
    def getTableId(self):
        """ generated source for method getTableId """
        return self.tableId

    # 
    #      * A list of your current cards
    #      *
    #      * @return your List<Card> of cards
    #      *
    #      * @see Card
    #      
    def getMyCards(self):
        """ generated source for method getMyCards """
        return self.myCards

    # 
    #      * The list of cards played to the community so far.
    #      *
    #      * @return List<Card> of currently played community cards
    #      *
    #      * @see Card
    #      
    def getCommunityCards(self):
        """ generated source for method getCommunityCards """
        return self.communityCards

    # 
    #      * The list of your two cards and the available community
    #      * cards.
    #      *
    #      * @return List<Card> of your cards and the currently played community cards
    #      *
    #      * @see Card
    #      
    def getMyCardsAndCommunityCards(self):
        """ generated source for method getMyCardsAndCommunityCards """
        cards = self.myCards
        cards.append(self.communityCards)
        return cards

    # 
    #      * The current state the game play is in.
    #      *
    #      * @return PlayState
    #      *
    #      * @see CurrentPlayState
    #      
    def getCurrentPlayState(self):
        """ generated source for method getCurrentPlayState """
        return self.currentPlayState

    # 
    #      * The sum of all bets placed during this round
    #      *
    #      * @return The long value of the sum of all bets placed
    #      
    def getPotTotal(self):
        """ generated source for method getPotTotal """
        return self.potTotal

    # 
    #      * The small blind bet this game round
    #      *
    #      * @return The long value of the current small blind bet
    #      
    def getSmallBlind(self):
        """ generated source for method getSmallBlind """
        return self.smallBlind

    # 
    #      * The big blind bet this game round
    #      *
    #      * @return The long value of the current big blind bet
    #      
    def getBigBlind(self):
        """ generated source for method getBigBlind """
        return self.bigBlind

    # 
    #      * The player that acts as dealer during this game round
    #      *
    #      * @return the Dealer player
    #      *
    #      * @see GamePlayer
    #      
    def getDealerPlayer(self):
        """ generated source for method getDealerPlayer """
        return self.dealerPlayer

    # 
    #      * Convenience method for finding out if the bot
    #      * is acting dealer.
    #      *
    #      * @return TRUE if this bot is dealer this round.
    #      
    def amIDealerPlayer(self):
        """ generated source for method amIDealerPlayer """
        return self.myPlayersName == self.getDealerPlayer().getName()

    # 
    #      * The player that is small blind better during this game round
    #      *
    #      * @return the small blind player
    #      *
    #      * @see GamePlayer
    #      
    def getSmallBlindPlayer(self):
        """ generated source for method getSmallBlindPlayer """
        return self.smallBlindPlayer

    # 
    #      * Convenience method for finding out if the bot
    #      * is playing Small Blind this round.
    #      *
    #      * @return TRUE if this bot is Small Blind this round.
    #      
    def amISmallBlindPlayer(self):
        """ generated source for method amISmallBlindPlayer """
        return self.myPlayersName == self.getSmallBlindPlayer().getName()

    # 
    #      * The player that big blind better during this game round
    #      *
    #      * @return the big blind player
    #      *
    #      * @see GamePlayer
    #      
    def getBigBlindPlayer(self):
        """ generated source for method getBigBlindPlayer """
        return self.bigBlindPlayer

    # 
    #      * Convenience method for finding out if the bot
    #      * is playing Big Blind this round.
    #      *
    #      * @return TRUE if this bot is Big Blind this round.
    #      
    def amIBigBlindPlayer(self):
        """ generated source for method amIBigBlindPlayer """
        return self.myPlayersName == self.getBigBlindPlayer().getName()

    # 
    #      * The amount of chips you have left
    #      *
    #      * @return the long value of your current amount of chips
    #      
    def getMyCurrentChipAmount(self):
        """ generated source for method getMyCurrentChipAmount """
        return self.myCurrentChipAmount

    # 
    #      * @param player
    #      *
    #      * @return True if player has folded this game round
    #      
    def hasPlayerFolded(self, player):
        """ generated source for method hasPlayerFolded """
        return self.foldedPlayers[player]

    # 
    #      * @return True if you have folded this game round
    #      
    def haveIFolded(self):
        """ generated source for method haveIFolded """
        player = GamePlayer(self.myPlayersName, 0)
        return self.hasPlayerFolded[player]

    # 
    #      * @param player
    #      *
    #      * @return True if player has gone all in this game round
    #      
    def hasPlayerGoneAllIn(self, player):
        """ generated source for method hasPlayerGoneAllIn """
        return self.allInPlayers[player]

    # 
    #      * @return True if you have gone all in this game round
    #      
    def haveIGoneAllIn(self):
        """ generated source for method haveIGoneAllIn """
        player = GamePlayer(self.myPlayersName, 0)
        return self.hasPlayerFolded[player]

    # 
    #      * Gives the total amount a player has invested in the pot
    #      * during this game round.
    #      *
    #      * @param player
    #      *
    #      * @return the long value of the chip amount this player has invested in the pot
    #      
    def getInvestmentInPotFor(self, player):
        """ generated source for method getInvestmentInPotFor """
        return self.potInvestmentPerPlayer.get(player, 0)

    # 
    #      * Gives the total amount you have invested in the pot
    #      * during this game round.
    #      *
    #      * @return the long value of the chip amount you have invested in the pot
    #      
    def getMyInvestmentInPot(self):
        """ generated source for method getMyInvestmentInPot """
        return self.getInvestmentInPotFor(GamePlayer(self.myPlayersName, 0))

    # 
    #      * @return A List<GamePlayer> participating in this game round
    #      
    def getPlayers(self):
        """ generated source for method getPlayers """
        return self.players

    # 
    #      * @return The number of folded players this game round
    #      
    def getNumberOfFoldedPlayers(self):
        """ generated source for method getNumberOfFoldedPlayers """
        return len(self.foldedPlayers)

    # 
    #      * @return The total numbers players in this game round
    #      
    def getNumberOfPlayers(self):
        """ generated source for method getNumberOfPlayers """
        return len(self.players)

    def reset(self):
        """ generated source for method reset """
        self.myCards = []
        self.communityCards = []
        self.currentPlayState = PlayStateInstance.PRE_FLOP
        self.foldedPlayers = []
        self.allInPlayers = []
        self.players = []
        self.potTotal = 0L
        self.potInvestmentPerPlayer = {}
        self.smallBlind = 0L
        self.bigBlind = 0L
        self.dealerPlayer = None
        self.smallBlindPlayer = None
        self.bigBlindPlayer = None
        self.tableId = 0

    def addPotInvestmentToPlayer(self, player, amount):
        """
        :type player: GamePlayer
        :type amount: int
        """
        self.potTotal = self.potTotal + amount
        if not player in self.potInvestmentPerPlayer.keys():
            self.potInvestmentPerPlayer[player.getName()] = 0
        prevInv = self.potInvestmentPerPlayer[player.getName()]
        self.potInvestmentPerPlayer[player.getName()] = prevInv + amount


class CurrentPlayStatePlayer(Player):
    def __init__(self, currentPlayState):
        """
        :param currentPlayState: CurrentPlayState
        """
        Player.__init__(self)
        self.state = currentPlayState

    """ generated source for class CurrentPlayStatePlayer """
    def getName(self):
        """ generated source for method getName """
        return None

    def serverIsShuttingDown(self, event):
        """ generated source for method serverIsShuttingDown """

    def onPlayIsStarted(self, event):
        """
        :param event: PlayIsStartedEvent
        :return:
        """
        self.state.reset()
        self.state.players = event.getPlayers()
        self.state.dealerPlayer = event.getDealer()
        self.state.smallBlindPlayer = event.getSmallBlindPlayer()
        self.state.bigBlindPlayer = event.getBigBlindPlayer()
        self.state.smallBlind = event.getSmallBlindAmount()
        self.state.bigBlind = event.getBigBlindAmount()
        self.state.tableId = event.getTableId()

        for gamePlayer in event.getPlayers():
            if self.state.myPlayersName == gamePlayer.getName():
                self.state.myCurrentChipAmount = gamePlayer.getChipCount()

    def onTableChangedStateEvent(self, event):
        """ generated source for method onTableChangedStateEvent """
        self.state.currentPlayState = event.getState()

    def onYouHaveBeenDealtACard(self, event):
        """ generated source for method onYouHaveBeenDealtACard """
        self.state.myCards.append(event.getCard())

    def onCommunityHasBeenDealtACard(self, event):
        """ generated source for method onCommunityHasBeenDealtACard """
        self.state.communityCards.append(event.getCard())

    def onPlayerBetBigBlind(self, event):
        """ generated source for method onPlayerBetBigBlind """
        self.state.addPotInvestmentToPlayer(event.getPlayer(), event.getBigBlind())

    def onPlayerBetSmallBlind(self, event):
        """ generated source for method onPlayerBetSmallBlind """
        self.state.addPotInvestmentToPlayer(event.getPlayer(), event.getSmallBlind())

    def onPlayerFolded(self, event):
        """ generated source for method onPlayerFolded """
        self.state.foldedPlayers.append(event.getPlayer())

    def onPlayerForcedFolded(self, event):
        """ generated source for method onPlayerForcedFolded """
        self.state.foldedPlayers.append(event.getPlayer())

    def onPlayerCalled(self, event):
        """ generated source for method onPlayerCalled """
        self.state.addPotInvestmentToPlayer(event.getPlayer(), event.getCallBet())
        if event.getPlayer().getChipCount() == 0:
            self.state.allInPlayers.append(event.getPlayer())

    def onPlayerRaised(self, event):
        """ generated source for method onPlayerRaised """
        self.state.addPotInvestmentToPlayer(event.getPlayer(), event.getRaiseBet())
        if event.getPlayer().getChipCount() == 0:
            self.state.allInPlayers.append(event.getPlayer())

    def onPlayerWentAllIn(self, event):
        """ generated source for method onPlayerWentAllIn """
        self.state.addPotInvestmentToPlayer(event.getPlayer(), event.getAllInAmount())
        self.state.allInPlayers.append(event.getPlayer())

    def onPlayerChecked(self, event):
        """ generated source for method onPlayerChecked """

    def onYouWonAmount(self, event):
        """ generated source for method onYouWonAmount """

    def onShowDown(self, event):
        """ generated source for method onShowDown """
        for psd in event.getPlayersShowDown():
            self.state.players.append(psd.getPlayer())
            if self.state.myPlayersName == psd.getPlayer().getName():
                self.state.myCurrentChipAmount = psd.getPlayer().getChipCount()

    def onTableIsDone(self, event):
        """ generated source for method onTableIsDone """

    def onPlayerQuit(self, event):
        """ generated source for method onPlayerQuit """

    def actionRequired(self, request):
        """ generated source for method actionRequired """
        return None

    def connectionToGameServerLost(self):
        """ generated source for method connectionToGameServerLost """

    def connectionToGameServerEstablished(self):
        """ generated source for method connectionToGameServerEstablished """