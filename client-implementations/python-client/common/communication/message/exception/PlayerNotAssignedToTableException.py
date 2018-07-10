#!/usr/bin/env python
""" generated source for module PlayerNotAssignedToTableException """
# package: se.cygni.texasholdem.communication.message.exception
import se.cygni.texasholdem.communication.message.type_.IsATexasMessage

class PlayerNotAssignedToTableException(TexasException):
    """ generated source for class PlayerNotAssignedToTableException """
    def throwException(self):
        """ generated source for method throwException """
        raise se.cygni.texasholdem.game.exception.PlayerNotAssignedToTableException(message)

