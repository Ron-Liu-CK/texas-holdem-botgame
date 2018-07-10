#!/usr/bin/env python

import abc
import uuid
from common.communication.message.request.ActionRequest import ActionRequest
from common.game.Action import Action


class Player(object):
    def __init__(self):
        self.playerId = str(uuid.uuid4())

    @abc.abstractmethod
    def getName(self):
        """ generated source for method getName """

    @abc.abstractmethod
    def serverIsShuttingDown(self, event):
        """ generated source for method serverIsShuttingDown """

    @abc.abstractmethod
    def onPlayIsStarted(self, event):
        """ generated source for method onPlayIsStarted """

    @abc.abstractmethod
    def onTableChangedStateEvent(self, event):
        """ generated source for method onTableChangedStateEvent """

    @abc.abstractmethod
    def onYouHaveBeenDealtACard(self, event):
        """ generated source for method onYouHaveBeenDealtACard """

    @abc.abstractmethod
    def onCommunityHasBeenDealtACard(self, event):
        """ generated source for method onCommunityHasBeenDealtACard """

    @abc.abstractmethod
    def onPlayerBetBigBlind(self, event):
        """ generated source for method onPlayerBetBigBlind """

    @abc.abstractmethod
    def onPlayerBetSmallBlind(self, event):
        """ generated source for method onPlayerBetSmallBlind """

    @abc.abstractmethod
    def onPlayerFolded(self, event):
        """ generated source for method onPlayerFolded """

    @abc.abstractmethod
    def onPlayerForcedFolded(self, event):
        """ generated source for method onPlayerForcedFolded """

    @abc.abstractmethod
    def onPlayerCalled(self, event):
        """ generated source for method onPlayerCalled """

    @abc.abstractmethod
    def onPlayerRaised(self, event):
        """ generated source for method onPlayerRaised """

    @abc.abstractmethod
    def onPlayerWentAllIn(self, event):
        """ generated source for method onPlayerWentAllIn """

    @abc.abstractmethod
    def onPlayerChecked(self, event):
        """ generated source for method onPlayerChecked """

    @abc.abstractmethod
    def onYouWonAmount(self, event):
        """ generated source for method onYouWonAmount """

    @abc.abstractmethod
    def onShowDown(self, event):
        """ generated source for method onShowDown """

    @abc.abstractmethod
    def onTableIsDone(self, event):
        """ generated source for method onTableIsDone """

    @abc.abstractmethod
    def onPlayerQuit(self, event):
        """ generated source for method onPlayerQuit """

    @abc.abstractmethod
    def actionRequired(self, request):
        """ generated source for method actionRequired """

    @abc.abstractmethod
    def connectionToGameServerLost(self):
        """ generated source for method connectionToGameServerLost """

    @abc.abstractmethod
    def connectionToGameServerEstablished(self):
        """ generated source for method connectionToGameServerEstablished """

    def __hash__(self):
        return hash((self.playerId, self.getName()))

    def __eq__(self, other):
        """
        :param other: Player
        :return: bool
        """
        return (self.playerId, self.getName()) == (other.playerId, other.getName())

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)