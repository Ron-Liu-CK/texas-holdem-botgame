#!/usr/bin/env python

import json
from common.Util import Logger
from common.communication.message.event import *
from common.communication.message.response import *
from common.communication.message.request.ActionRequest import ActionRequest
from common.game import *
from common.game.definitions import *
from TexasMessage import TexasMessage

class TexasMessageParser(object):
    """ generated source for class TexasMessageParser """
    currentVersion = "1.1.21-SNAPSHOT"
    TYPE_IDENTIFIER = "type"

    log = Logger.getLogging()

    @classmethod
    def decodeMessage(cls, msg):
        """ generated source for method decodeMessage """
        message = cls.parseAndGetClassForMessage(msg)
        try:
            if not cls.currentVersion == message.getVersion():
                cls.log.warn("The node you are communicating with is at version: [%s] and this client is at version: [%s]" % (message.getVersion(), cls.currentVersion))
            return message
        except Exception as e:
            cls.log.error(msg)
            raise e

    @classmethod
    def encodeMessage(cls, message):
        """
        :type message: TexasMessage
        :return: string
        """
        message.setVersion(cls.currentVersion)
        return message.toJSON()

    @classmethod
    def parseAndGetClassForMessage(cls, message):
        """ generated source for method parseAndGetClassForMessage """
        try:
            json_obj = json.loads(message)
            if json_obj is None:
                #  Nothing found
                raise Exception("Could not find [" + cls.TYPE_IDENTIFIER + "] in message: " + message)
            clazz = cls.getClassForIdentifier(json_obj)
            clazz.setVersion(json_obj["version"])

            return clazz
        except Exception as e:
            #  JSON exception
            raise Exception("Could not parse message: " + message, e)

    @classmethod
    def getClassForIdentifier(cls, json_obj):
        type = str(json_obj[cls.TYPE_IDENTIFIER])
        if not type.startswith("se.cygni"):
            raise Exception("Unknown identifier: " + type)

        event_class = type.split('.')[-1]
        if event_class == "RegisterForPlayResponse":
            response = RegisterForPlayResponse.RegisterForPlayResponse()
            response.sessionId = json_obj["sessionId"]
            response.setRequestId(json_obj["requestId"])
            return response

        if event_class == "ActionRequest":
            actions = []  # type: list[Action.Action]
            for json_action in json_obj["possibleActions"]:
                action = Action.Action(json_action['actionType'], json_action['amount'])
                actions.append(action)
            request = ActionRequest(actions)
            request.setSessionId(json_obj["sessionId"])
            request.setRequestId(json_obj["requestId"])
            return request

        if event_class == "CommunityHasBeenDealtACardEvent":
            json_card = json_obj["card"]
            card = cls.getClassForCard(json_card)
            return CommunityHasBeenDealtACardEvent.CommunityHasBeenDealtACardEvent(card)

        if event_class == "PlayIsStartedEvent":
            players = []      # type: list[GamePlayer.GamePlayer]
            for json_action in json_obj["players"]:
                players.append(cls.getClassForGamePlayer(json_action))
            return PlayIsStartedEvent.PlayIsStartedEvent(
                players,
                json_obj['smallBlindAmount'],
                json_obj['bigBlindAmount'],
                cls.getClassForGamePlayer(json_obj['dealer']),
                cls.getClassForGamePlayer(json_obj['smallBlindPlayer']),
                cls.getClassForGamePlayer(json_obj['bigBlindPlayer']),
                json_obj['tableId']
            )

        if event_class == "PlayerBetBigBlindEvent":
            return PlayerBetBigBlindEvent.PlayerBetBigBlindEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['bigBlind']
            )

        if event_class == "PlayerBetSmallBlindEvent":
            return PlayerBetSmallBlindEvent.PlayerBetSmallBlindEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['smallBlind']
            )

        if event_class == "PlayerCalledEvent":
            return PlayerCalledEvent.PlayerCalledEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['callBet']
            )

        if event_class == "PlayerCheckedEvent":
            return PlayerCheckedEvent.PlayerCheckedEvent(cls.getClassForGamePlayer(json_obj['player']))

        if event_class == "PlayerFoldedEvent":
            return PlayerFoldedEvent.PlayerFoldedEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['investmentInPot']
            )

        if event_class == "PlayerRaisedEvent":
            return PlayerRaisedEvent.PlayerRaisedEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['raiseBet']
            )

        if event_class == "PlayerWentAllInEvent":
            return PlayerWentAllInEvent.PlayerWentAllInEvent(
                cls.getClassForGamePlayer(json_obj['player']),
                json_obj['allInAmount']
            )

        if event_class == "ShowDownEvent":
            players = []      # type: list[PlayerShowDown.PlayerShowDown]
            for json_player in json_obj["playersShowDown"]:
                player = cls.getClassForGamePlayer(json_player['player'])
                json_hand = json_player["hand"]
                cards = []        # type: list[Card.Card]
                for json_card in json_hand["cards"]:
                    cards.append(cls.getClassForCard(json_card))
                hand = Hand.Hand(cards, PokerHand.PokerHand.get(json_hand['pokerHand']), json_hand['folded'])
                players.append(PlayerShowDown.PlayerShowDown(player, hand, json_player['wonAmount']))
            return ShowDownEvent.ShowDownEvent(players)

        if event_class == "TableChangedStateEvent":
            return TableChangedStateEvent.TableChangedStateEvent(PlayState.PlayStateInstance.get(json_obj["state"]))

        if event_class == "TableIsDoneEvent":
            players = []      # type: list[GamePlayer.GamePlayer]
            for json_player in json_obj["players"]:
                players.append(cls.getClassForGamePlayer(json_player))
            return TableIsDoneEvent.TableIsDoneEvent(players)

        if event_class == "YouHaveBeenDealtACardEvent":
            return YouHaveBeenDealtACardEvent.YouHaveBeenDealtACardEvent(cls.getClassForCard(json_obj["card"]))

        if event_class == "YouWonAmountEvent":
            return YouWonAmountEvent.YouWonAmountEvent(json_obj["wonAmount"], json_obj["yourChipAmount"])

        raise Exception("Unknown Class: " + event_class)

    @classmethod
    def getClassForGamePlayer(cls, json_obj):
        return GamePlayer.GamePlayer(json_obj['name'], json_obj['chipCount'])

    @classmethod
    def getClassForCard(cls, json_obj):
        return Card.Card(Rank.Rank.get(json_obj['rank']), Suit.Suit.get(json_obj['suit']))
