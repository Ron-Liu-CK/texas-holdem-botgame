#!/usr/bin/env python

import re

class ValidPlayerNameVerifier(object):
    @classmethod
    def verifyName(cls, name):
        """
        :param name: String
        :return: bool
        """
        if not re.match("^[A-Za-z0-9_-]+$", name):
            raise Exception(name + " is not a legal user name. a-z, A-X, 1-9 and -_ are allowed.")



