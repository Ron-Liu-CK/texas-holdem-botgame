#!/usr/bin/env python

from common.Util import Logger
from client.client.PlayerClient import PlayerClient
from common.client.CurrentPlayState import *
from common.client.ClientEventDispatcher import *
from common.communication.message.request.ActionRequest import ActionRequest
from common.communication.message.event import *
from common.game.definitions.PlayState import *
from common.game.definitions.PokerHand import PokerHand
from common.game.util.PokerHandUtil import PokerHandUtil
from common.game.Room import Room
from common.game.ActionType import ActionType
import logging

#
#  * This is an example Poker bot player, you can use it as
#  * a starting point when creating your own.
#  * <p/>
#  * If you choose to create your own class don't forget that
#  * it must implement the interface Player
#  *
#  * @see Player
#  *      <p/>
#  *      Javadocs for common utilities and classes used may be
#  *      found here:
#  *      http://poker.cygni.se/mavensite/texas-holdem-common/apidocs/index.html
#  *      <p/>
#  *      You can inspect the games you bot has played here:
#  *      http://poker.cygni.se/showgame
#  
class FullyImplementedBot(Player):
    """ generated source for class FullyImplementedBot """
    serverHost = ""                 # type: str
    serverPort = None               # type: int
    name = ""                       # type: str
    playerClient = None             # type: PlayerClient
    log = Logger.getLogging()

    # 
    #      * Default constructor for a Java Poker Bot.
    #      *
    #      * @param serverHost IP or hostname to the poker server
    #      * @param serverPort port at which the poker server listens
    #      
    def __init__(self, name, serverHost, serverPort):
        """ generated source for method __init__ """
        super(FullyImplementedBot, self).__init__()
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.name = name
        #  Initialize the player client
        self.playerClient = PlayerClient(self, serverHost, serverPort)

    def playATrainingGame(self):
        """ generated source for method playATrainingGame """
        self.playerClient.connect(Room.TRAINING)

    def playTournamentGame(self):
        """ generated source for method playTournamentGame """
        self.playerClient.connect(Room.TOURNAMENT)

    # 
    #      * The name you choose must be unique, if another connected bot has
    #      * the same name your bot will be denied connection.
    #      *
    #      * @return The name under which this bot will be known
    #      
    def getName(self):
        """ generated source for method getName """
        return self.name
        #         throw new RuntimeException("Did you forget to specify a name for your bot (hint: your email address is a good idea)?");

    # 
    #      * This is where you supply your bot with your special mojo!
    #      * <p/>
    #      * The ActionRequest contains a list of all the possible actions
    #      * your bot can perform.
    #      *
    #      * @param request The list of Actions that the bot may perform.
    #      *
    #      * @return The action the bot wants to perform.
    #      *
    #      * @see ActionRequest
    #      *      <p/>
    #      *      Given the current situation you need to choose the best
    #      *      action. It is not allowed to change any values in the
    #      *      ActionRequest. The amount you may RAISE or CALL is already
    #      *      predermined by the poker server.
    #      *      <p/>
    #      *      If an invalid Action is returned the server will ask two
    #      *      more times. Failure to comply (i.e. returning an incorrect
    #      *      or non valid Action) will result in a forced FOLD for the
    #      *      current Game Round.
    #      * @see Action
    #      
    def actionRequired(self, request):
        """ generated source for method actionRequired """
        response = self.getBestAction(request)      # type: Action
        self.log.info("I'm going to %s %s" % (response.getActionType(), "with " + str(response.getAmount()) if response.getAmount() > 0 else ""))

        return response

    # 
    #      * A helper method that returns this bots idea of the best action.
    #      * Note! This is just an example, you need to add your own smartness
    #      * to win.
    #      *
    #      * @param request
    #      *
    #      * @return
    #      
    def getBestAction(self, request):
        """ generated source for method getBestAction """
        callAction = None
        checkAction = None
        raiseAction = None
        foldAction = None
        allInAction = None

        for action in request.getPossibleActions():
            if action.getActionType() == ActionType.CALL:
                callAction = action
            elif action.getActionType() == ActionType.CHECK:
                checkAction = action
            elif action.getActionType() == ActionType.FOLD:
                foldAction = action
            elif action.getActionType() == ActionType.RAISE:
                raiseAction = action
            elif action.getActionType() == ActionType.ALL_IN:
                allInAction = action
            else:
                raise Exception("Invalid Action in the options")

        #  The current play state is accessible through this class. It
        #  keeps track of basic events and other players.
        playState = self.playerClient.getCurrentPlayState()

        #  The current BigBlind
        currentBB = playState.getBigBlind()

        #  PokerHandUtil is a hand classifier that returns the best hand given
        #  the current community cards and your cards.
        pokerHandUtil = PokerHandUtil(playState.getCommunityCards(), playState.getMyCards())
        myBestHand = pokerHandUtil.getBestHand()
        myBestPokerHand = myBestHand.getPokerHand()

        #  Let's go ALL IN if hand is better than or equal to THREE_OF_A_KIND
        if allInAction != None and self.isHandBetterThan(myBestPokerHand, PokerHand.TWO_PAIRS):
            return allInAction

        #  Otherwise, be more careful CHECK if possible.
        if checkAction != None:
            return checkAction
        #  Okay, we have either CALL or RAISE left
        callAmount = -1 if callAction == None else callAction.getAmount()
        raiseAmount = -1 if raiseAction == None else raiseAction.getAmount()

        #  Only call if ONE_PAIR or better
        if self.isHandBetterThan(myBestPokerHand, PokerHand.ONE_PAIR) and callAction != None:
            return allInAction
            #             return callAction;
        #  Do I have something better than TWO_PAIR and can RAISE?
        if self.isHandBetterThan(myBestPokerHand, PokerHand.TWO_PAIRS) and raiseAction != None:
            return raiseAction

        #  I'm small blind and we're in PRE_FLOP, might just as well call
        if playState.amISmallBlindPlayer() and playState.getCurrentPlayState() == PlayStateInstance.PRE_FLOP and callAction != None:
            return callAction

        #  failsafe
        return foldAction

    # 
    #      * Compares two pokerhands.
    #      *
    #      * @param myPokerHand
    #      * @param otherPokerHand
    #      *
    #      * @return TRUE if myPokerHand is valued higher than otherPokerHand
    #      
    def isHandBetterThan(self, myPokerHand, otherPokerHand):
        """ generated source for method isHandBetterThan """
        return myPokerHand.getOrderValue() > otherPokerHand.getOrderValue()

    # 
    #      * **********************************************************************
    #      * <p/>
    #      * Event methods
    #      * <p/>
    #      * These methods tells the bot what is happening around the Poker Table.
    #      * The methods must be implemented but it is not mandatory to act on the
    #      * information provided.
    #      * <p/>
    #      * The helper class CurrentPlayState provides most of the book keeping
    #      * needed to keep track of the total picture around the table.
    #      *
    #      * @see CurrentPlayState
    #      *      <p/>
    #      *      ***********************************************************************
    #      
    def onPlayIsStarted(self, event):
        """ generated source for method onPlayIsStarted """
        self.log.debug("Play is started")

    def onTableChangedStateEvent(self, event):
        """ generated source for method onTableChangedStateEvent """
        self.log.debug("Table changed state: %s" % event.getState())

    def onYouHaveBeenDealtACard(self, event):
        """ generated source for method onYouHaveBeenDealtACard """
        self.log.debug("I, %s, got a card: %s" % (self.getName(), event.getCard().toShortString()))

    def onCommunityHasBeenDealtACard(self, event):
        """ generated source for method onCommunityHasBeenDealtACard """
        self.log.debug("Community got a card: %s" % event.getCard().toShortString())

    def onPlayerBetBigBlind(self, event):
        """ generated source for method onPlayerBetBigBlind """
        self.log.debug("%s placed big blind with amount %s" % (event.getPlayer().getName(), event.getBigBlind()))

    def onPlayerBetSmallBlind(self, event):
        """ generated source for method onPlayerBetSmallBlind """
        self.log.debug("%s placed small blind with amount %s" % (event.getPlayer().getName(), event.getSmallBlind()))

    def onPlayerFolded(self, event):
        """ generated source for method onPlayerFolded """
        self.log.debug("%s folded after putting %s in the pot" % (event.getPlayer().getName(), event.getInvestmentInPot()))

    def onPlayerForcedFolded(self, event):
        """ generated source for method onPlayerForcedFolded """
        self.log.debug("NOT GOOD! %s was forced to fold after putting %s in the pot because exceeding the time limit" % (event.getPlayer().getName(), event.getInvestmentInPot()))

    def onPlayerCalled(self, event):
        """ generated source for method onPlayerCalled """
        self.log.debug("%s called with amount %s" % (event.getPlayer().getName(), event.getCallBet()))

    def onPlayerRaised(self, event):
        """ generated source for method onPlayerRaised """
        self.log.debug("%s raised with bet %s" % (event.getPlayer().getName(), event.getRaiseBet()))

    def onTableIsDone(self, event):
        """ generated source for method onTableIsDone """
        self.log.debug("Table is done, I'm leaving the table with $%d" % (self.playerClient.getCurrentPlayState().getMyCurrentChipAmount()))
        self.log.info("Ending poker session, the last game may be viewed at: http://%s/showgame/table/%d" % (self.serverHost, self.playerClient.getCurrentPlayState().getTableId()))
        quit()

    def onPlayerWentAllIn(self, event):
        """ generated source for method onPlayerWentAllIn """
        self.log.debug("%s went all in with amount %s" % (event.getPlayer().getName(), event.getAllInAmount()))

    def onPlayerChecked(self, event):
        """ generated source for method onPlayerChecked """
        self.log.debug("%s checked" % event.getPlayer().getName())

    def onYouWonAmount(self, event):
        """ generated source for method onYouWonAmount """
        self.log.debug("I, %s, won: %s" % (self.getName(), event.getWonAmount()))

    def onShowDown(self, event):
        """ generated source for method onShowDown """
        if not self.log.isEnabledFor(logging.INFO):
            return

        sb = "ShowDown:\n"
        for psd in event.getPlayersShowDown():
            won = "Fold" if psd.getHand().isFolded() else str(psd.getWonAmount())
            sb = sb + "%-13s won: %6s  hand: %-15s " % (psd.getPlayer().getName(), won, psd.getHand().getPokerHand().getName())
            sb = sb + " cards: | "
            for card in psd.getHand().getCards():
                sb = sb + "%-13s | " % card.toShortString()
            sb = sb + "\n"
        self.log.info(sb)

    def onPlayerQuit(self, event):
        """ generated source for method onPlayerQuit """
        self.log.debug("Player %s has quit" % event.getPlayer())

    def connectionToGameServerLost(self):
        """ generated source for method connectionToGameServerLost """
        self.log.debug("Lost connection to game server, exiting")
        exit(0)

    def connectionToGameServerEstablished(self):
        """ generated source for method connectionToGameServerEstablished """
        self.log.debug("Connection to game server established")

    def serverIsShuttingDown(self, event):
        """ generated source for method serverIsShuttingDown """
        self.log.debug("Server is shutting down")

