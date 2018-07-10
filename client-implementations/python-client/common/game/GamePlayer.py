#!/usr/bin/env python


class GamePlayer(object):
    """ generated source for class GamePlayer """
    name = str()
    chipCount = long()

    def __init__(self, name, chipCount):
        """ generated source for method __init__ """
        self.name = name
        self.chipCount = chipCount

    def getName(self):
        """ generated source for method getName """
        return self.name

    def getChipCount(self):
        """ generated source for method getChipCount """
        return self.chipCount

    def equals(self, o):
        """
        :type o: GamePlayer
        :return: bool
        """
        if o is None or GamePlayer.__class__ != o.__class__:
            return False
        player = o
        if not self.name == player.name:
            return False
        return True

    def hashCode(self):
        """ generated source for method hashCode """
        return self.name

    def __str__(self):
        """ generated source for method toString """
        return "GamePlayer [name=" + self.name + "]"

    def __hash__(self):
        return self.hashCode()

    def __eq__(self, other):
        """
        :param other: Player
        :return: bool
        """
        return self.equals(other)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)