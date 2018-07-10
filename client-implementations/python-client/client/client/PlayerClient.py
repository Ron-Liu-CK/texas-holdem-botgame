#!/usr/bin/env python

from common.communication.lock.ResponseLock import ResponseLock
from common.communication.message.TexasMessage import TexasMessage
from common.communication.message.TexasMessageParser import TexasMessageParser
from common.communication.message.event.TexasEvent import TexasEvent
from common.communication.message.request.ActionRequest import ActionRequest
from common.communication.message.request.RegisterForPlayRequest import RegisterForPlayRequest
from common.communication.message.request.TexasRequest import TexasRequest
from common.communication.message.response.ActionResponse import ActionResponse
from common.communication.message.response.RegisterForPlayResponse import RegisterForPlayResponse
from common.communication.message.response.TexasResponse import TexasResponse
from common.communication.netty.JsonDelimiter import JsonDelimiter
from common.client.ClientEventDispatcher import ClientEventDispatcher
from common.client.CurrentPlayState import CurrentPlayState
from common.game.Action import Action
from common.game.Room import Room
from common.game.util.ValidPlayerNameVerifier import ValidPlayerNameVerifier
from common.player.Player import Player
from common.Util import *
from socket import *
import threading
import uuid


#
#  * This class handles the communication between client and server.
#  
class PlayerClient:
    """ generated source for class PlayerClient """
    RESPONSE_TIMEOUT_MS = 80000
    CONNECT_WAIT_MS = 1200

    clientEventDispatcher = None                    # type: ClientEventDispatcher
    currentPlayStateEventDispatcher = None          # type: ClientEventDispatcher
    player = None                                   # type: Player
    isConnected = False
    serverHost = ""
    serverPort = 0
    currentPlayState = None                         # type: CurrentPlayState

    # 
    #      * @param player     the Player in game
    #      * @param serverHost the host name or IP adr to the server
    #      * @param serverPort the port at which the server is accepting connections
    #      
    def __init__(self, player, serverHost, serverPort):
        self.player = player
        self.serverHost = serverHost
        self.serverPort = serverPort
        self.currentPlayState = CurrentPlayState(player.getName())
        self.clientEventDispatcher = ClientEventDispatcher(self.player)
        self.currentPlayStateEventDispatcher = ClientEventDispatcher(self.currentPlayState.getPlayerImpl())
        self.log = Logger.getLogging()
        self.client_socket = None

    # 
    #      * The reference to the CurrentPlayState is valid through the whole session and can
    #      * safely be referenced.
    #      *
    #      * @return the CurrentPlayState
    #      
    def getCurrentPlayState(self):
        """ generated source for method getCurrentPlayState """
        return self.currentPlayState

    def connect(self, room):
        """ generated source for method connect """
        self.log.info("Connecting to %s at port %s" % (self.serverHost, self.serverPort))
        self.client_socket = socket(AF_INET, SOCK_STREAM)  # instantiate
        self.client_socket.settimeout(10)
        self.client_socket.connect((self.serverHost, self.serverPort))  # connect to the server
        self.registerForPlay(room)

        data = ''
        while True:
            chunk = self.client_socket.recv(4096)
            data = data + chunk
            if data.endswith(str(JsonDelimiter.delimiter())):
                self.messageReceived(data)
                data = ''

            # try:
            #     chunk = self.client_socket.recv(4096)
            #     data = data + chunk
            #     print count + ":" + chunk
            #     if data.endswith(str(JsonDelimiter.delimiter())):
            #         self.messageReceived(data)
            #         data = ''
            #     count = count + 1
            # except Exception as e:
            #     raise e
            #     print "ERROR: " + e.message
            #     continue


    def disconnect(self):
        """ generated source for method disconnect """
        self.client_socket.close()
        self.isConnected = False

    def getPlayer(self):
        """ generated source for method getPlayer """
        return self.player

    def messageReceived(self, data):
        """ generated source for method messageReceived """
        messages = data.split(str(JsonDelimiter.delimiter()))
        for message in messages:
            if len(message):
                self.onMessageReceived(TexasMessageParser.decodeMessage(message))

    def onMessageReceived(self, message):
        """ generated source for method onMessageReceived """
        if isinstance(message, TexasEvent):
            self.currentPlayStateEventDispatcher.onEvent(message)
            self.clientEventDispatcher.onEvent(message)
            return
        elif isinstance(message, ActionRequest):
            action = self.player.actionRequired(message)    # type: Action
            response = ActionResponse()                     # type: ActionResponse
            response.setRequestId(message.getRequestId())
            response.setAction(action)
            self.sendMessage(response)
        elif isinstance(message, TexasResponse):
            response = message  # type: TexasResponse
            requestId = response.getRequestId()     # type: int
            self.log.info("Response recieved for %s: %s" % (requestId, message))


    def registerForPlay(self, room):
        """ generated source for method registerForPlay """
        request = RegisterForPlayRequest()
        request.setRequestId(self.getUniqueRequestId())
        request.name = self.getPlayerName()
        request.room = room
        #  Validate player name
        ValidPlayerNameVerifier.verifyName(request.name)
        return self.sendMessage(request)

    def getPlayerName(self):
        """ generated source for method getPlayerName """
        return self.player.getName()

    def sendMessage(self, message):
        """ generated source for method sendMessage """
        try:
            self.client_socket.sendall(TexasMessageParser.encodeMessage(message) + str(JsonDelimiter.delimiter()))
            return True
        except Exception as e:
            self.exceptionCaught(e)
            return False

    def getUniqueRequestId(self):
        """ generated source for method getUniqueRequestId """
        return str(uuid.uuid4())

    def exceptionCaught(self, e):
        """ generated source for method exceptionCaught """
        self.log.info("Client exception: %s (Don't worry this can happen if for example the server disconnects you just before you " + "disconnect yourself)" % e.getCause().__class__.getCanonicalName() if e.getCause() != None else e.__class__.getCanonicalName())

