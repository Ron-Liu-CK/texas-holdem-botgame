#!/usr/bin/env python

from common.game.Card import Card


def card_sort_value_by_rank(card):
    """
    :param card: Card
    :return: int
    """
    return card.getRank().hashCode() * 100 + card.getSuit().hashCode()


def card_sort_value_by_suit(card):
    """
    :param card: Card
    :return: int
    """
    return card.getSuit().hashCode() * 100 + card.getRank().hashCode()