#!/usr/bin/env python

""" generated source for module BasicPlayer """
from common.Util import Logger
from common.player.Player import Player
from common.communication.message.event import *
from common.game.Card import Card
from common.game.PlayerShowDown import PlayerShowDown


# 
#  * A convenience class to extend if you don't want to implement the whole
#  * Player interface. Most methods just log at DEBUG level what event was
#  * received.
#  *
#  * @see Player
#  
class BasicPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.log = Logger.getLogging()

    def serverIsShuttingDown(self, event):
        """ type hinting
        :type event: common.communication.message.event.ServerIsShuttingDownEvent
        """
        self.log.debug("Server is shutting down")

    def onPlayIsStarted(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayIsStartedEvent.PlayIsStartedEvent
        """
        self.log.debug("Play is started")

    def onTableChangedStateEvent(self, event):
        """ type hinting
        :type event: common.communication.message.event.TableChangedStateEvent
        """
        self.log.debug("Table changed state: %s" % event.getState())

    def onYouHaveBeenDealtACard(self, event):
        """
        :type event: YouHaveBeenDealtACardEvent.YouHaveBeenDealtACardEvent
        """
        self.log.debug("I, %s, got a card: %s" % (self.getName(), event.getCard()))

    def onCommunityHasBeenDealtACard(self, event):
        """ type hinting
        :type event: common.communication.message.event.CommunityHasBeenDealtACardEvent.CommunityHasBeenDealtACardEvent
        """
        self.log.debug("Community got a card: %s" % event.getCard())

    def onPlayerBetBigBlind(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerBetBigBlindEvent
        """
        self.log.debug("%s placed big blind with amount %s" % (event.getPlayer().getName(), event.getBigBlind()))

    def onPlayerBetSmallBlind(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerBetSmallBlindEvent
        """
        self.log.debug("%s placed small blind with amount %s" % (event.getPlayer().getName(), event.getSmallBlind()))

    def onPlayerFolded(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerFoldedEvent
        """
        self.log.debug("%s folded after putting %s in the pot" % (event.getPlayer().getName(), event.getInvestmentInPot()))

    def onPlayerCalled(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerCalledEvent
        """
        self.log.debug("%s called with amount %s" % (event.getPlayer().getName(), event.getCallBet()))

    def onPlayerForcedFolded(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerForcedFoldedEvent
        """
        self.log.warn("Holy crap, your bot has exceeded the time-limit and been forced to fold! %s called with amount %s" % (event.getPlayer().getName(), event.getInvestmentInPot()))

    def onPlayerRaised(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerRaisedEvent
        """
        self.log.debug("%s raised with bet %s" % (event.getPlayer().getName(), event.getRaiseBet()))

    def onTableIsDone(self, event):
        """ type hinting
        :type event: common.communication.message.event.TableIsDoneEvent
        """
        self.log.debug("Table is done!")

    def onPlayerWentAllIn(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerWentAllInEvent
        """
        self.log.debug("%s went all in with amount %s" % (event.getPlayer().getName(), event.getAllInAmount()))

    def onPlayerChecked(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerCheckedEvent
        """
        self.log.debug("%s checked" % event.getPlayer().getName())

    def onYouWonAmount(self, event):
        """ type hinting
        :type event: common.communication.message.event.YouWonAmountEvent
        """
        self.log.debug("I, %s, won: %s" % (self.getName(), event.getWonAmount()))

    def onShowDown(self, event):
        """ type hinting
        :type event: common.communication.message.event.ShowDownEvent
        """
        if not self.log.isDebugEnabled():
            return
        sb = " "
        sb += "ShowDown:\n"
        for psd in event.getPlayersShowDown():
            sb += "%-13s won: %6s  hand: %-15s " % (psd.getPlayer().getName(), "Fold" if psd.getHand().isFolded() else psd.getWonAmount(), psd.getHand().getPokerHand().getName())
            sb += " cards: | "
            for card in psd.getHand().getCards():
                sb += "%-13s | " % card
            sb += "\n"
        self.log.debug(sb)

    def onPlayerQuit(self, event):
        """ type hinting
        :type event: common.communication.message.event.PlayerQuitEvent
        """
        self.log.debug("Player %s has quit" % event.getPlayer())

    def connectionToGameServerLost(self):
        self.log.debug("Lost connection to game server")

    def connectionToGameServerEstablished(self):
        self.log.debug("Connection to game server established")


