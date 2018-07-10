#!/usr/bin/env python
""" generated source for module ClientEventDispatcher """

from common.Util import Logger
from common.player.Player import Player
from common.communication.message.event.TexasEvent import TexasEvent
from common.communication.message.event.PlayIsStartedEvent import PlayIsStartedEvent
import inspect
import logging

#
#  * This ClientEventDispatcher uses reflection to notify a player of incoming events.
#  * <p/>
#  * Upon instantiation of this class the target object is analyzed for methods
#  * that take an event class as argument (and also has that same method declared
#  * in the interface).
#  * <p/>
#  * The matching methods are stored in a map for quick lookups.
#  *
#  * @author emil
#


class ClientEventDispatcher(object):
    target = None       # type: Player
    invokeMap = {}

    def __init__(self, target):
        """
        :type target: Player
        """
        self.target = target
        self.log = Logger.getLogging()
        self.populateInvokeMap()

    # 
    #      * Populates the invoke map with matching methods and arguments.
    #      
    def populateInvokeMap(self):
        self.log.info("Populating invoke map")
        ms = inspect.getmembers(self.target, predicate=inspect.ismethod)
        for m in ms:
            key = method = m[0]
            if key.startswith("__"):
                continue
            if key.startswith("on"):
                key = key[2:]

            key = key[0].upper() + key[1:]
            if not key.endswith("Event"):
                key = key + "Event"
            self.invokeMap[key] = method

        if self.log.isEnabledFor(logging.DEBUG):
            self.printInvokeMap()

    # 
    #      * Prints the invoke map
    #      
    def printInvokeMap(self):
        """ generated source for method printInvokeMap """
        self.log.debug("Invoke map:")
        for key, value in self.invokeMap.iteritems():
            self.log.debug("%s => %s" % (key, value))

    # 
    #      * Invokes the corresponding method for the Player matching
    #      * the current event.
    #      *
    #      * @param event
    #      
    def onEvent(self, event):
        """ generated source for method onEvent """
        if event is None:
            return

        target_class = type(self.target).__name__
        event_class = type(event).__name__
        self.log.debug("onEvent, looking for matching method for argument: %s" % event_class)

        if event_class in self.invokeMap:
            try:
                func = getattr(self.target, self.invokeMap[event_class])
                func(event)
            except Exception as e:
                self.log.error("Failed to invoke target method %s.%s for %s: %s" % (target_class, self.invokeMap[event_class], event_class,  e.message))
        else:
            self.log.warn("Could not dispatch for event of type %s in %s:, no matching method found " % (event_class, target_class))
