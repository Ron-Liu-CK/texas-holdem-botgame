#!/usr/bin/env python
""" generated source for module InvalidAmountException """
# package: se.cygni.texasholdem.game.exception
class InvalidAmountException(GameException):
    """ generated source for class InvalidAmountException """
    serialVersionUID = 5009842166127191132L

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(InvalidAmountException, self).__init__()

    @__init__.register(object, str, Throwable)
    def __init___0(self, message, cause):
        """ generated source for method __init___0 """
        super(InvalidAmountException, self).__init__(cause)

    @__init__.register(object, str)
    def __init___1(self, message):
        """ generated source for method __init___1 """
        super(InvalidAmountException, self).__init__(message)

    @__init__.register(object, Throwable)
    def __init___2(self, cause):
        """ generated source for method __init___2 """
        super(InvalidAmountException, self).__init__(cause)

