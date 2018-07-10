#!/usr/bin/env python


class PlayState:
    """ generated source for enum PlayState """
    name = str()

    def __init__(self, name):
        """ generated source for method __init__ """
        self.name = name

    def getName(self):
        """ generated source for method getName """
        return self.name

    def __str__(self):
        return self.name

    @classmethod
    def getNextState(cls, givenState):
        """ generated source for method getNextState """
        allStates = PlayState.values()
        if givenState.ordinal() == len(allStates):
            raise Exception("Already at last PlayState: " + givenState)
        return allStates[givenState.ordinal() + 1]

    @classmethod
    def getPreviousState(cls, givenState):
        """ generated source for method getPreviousState """
        allStates = PlayState.values()
        if givenState.ordinal() == 0:
            raise Exception("Already at first PlayState: " + givenState)
        return allStates[givenState.ordinal() - 1]

    @classmethod
    def hasNextState(cls, givenState):
        """ generated source for method hasNextState """
        return False if givenState.ordinal() == len(length) else True

    @classmethod
    def hasPreviousState(cls, givenState):
        """ generated source for method hasPreviousState """
        return False if givenState.ordinal() == 0 else True


class PlayStateInstance:
    PRE_FLOP = PlayState("Pre-flop")
    FLOP = PlayState("Flop")
    TURN = PlayState("Turn")
    RIVER = PlayState("River")
    SHOWDOWN = PlayState("Showdown")

    @staticmethod
    def get(name):
        if name.upper() == "PRE_FLOP":
            return PlayStateInstance.PRE_FLOP
        if name.upper() == "FLOP":
            return PlayStateInstance.FLOP
        if name.upper() == "TURN":
            return PlayStateInstance.TURN
        if name.upper() == "RIVER":
            return PlayStateInstance.RIVER
        if name.upper() == "SHOWDOWN":
            return PlayStateInstance.SHOWDOWN

