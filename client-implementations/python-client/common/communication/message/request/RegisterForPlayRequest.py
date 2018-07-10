#!/usr/bin/env python

from common.game.Room import *
from common.communication.message.request.TexasRequest import TexasRequest


class RegisterForPlayRequest(TexasRequest):
    """ generated source for class RegisterForPlayRequest """
    name = ""
    room = None         # type: Room

