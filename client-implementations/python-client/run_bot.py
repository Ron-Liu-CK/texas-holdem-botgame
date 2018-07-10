#!/usr/bin/env python

from FullyImplementedBot import FullyImplementedBot
import sys

BOT_NAME = "__NiftyTopicHourPythonClient"

host = sys.argv[1]
port = int(sys.argv[2])

bot = FullyImplementedBot(BOT_NAME, host, port)
bot.playATrainingGame()
