#!/usr/bin/env python

""" generated source for module BasicPlayer """
import logging


class Logger:
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    @staticmethod
    def getLogging():
        return Logger.log
