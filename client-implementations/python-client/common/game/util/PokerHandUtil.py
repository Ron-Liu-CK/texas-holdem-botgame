#!/usr/bin/env python

from common.game.Card import Card
from common.game.definitions.CardSortBy import *
from common.game.definitions.PokerHand import *
from common.game.definitions.Rank import *
from common.game.definitions.Suit import *
from common.game.Hand import Hand
from common.game.util.CardsUtil import CardsUtil


# 
#  * PokerHandUtil extracts the best possible hand for a Player.
#  *
#  * @author emil
#  
class PokerHandUtil(object):
    """ generated source for class PokerHandUtil """
    rankDistribution = {}
    suitDistribution = {}
    cards = []                  # type: list[Card]

    def __init__(self, communityCards, playerCards = []):
        """ generated source for method __init__ """
        self.cards = communityCards + playerCards
        self.rankDistribution = CardsUtil.getRankDistribution(self.cards)
        self.suitDistribution = CardsUtil.getSuitDistribution(self.cards)


    # 
    #      * Extracts the best possible hand and returns the type of PokerHand and the
    #      * List of cards that make that hand.
    #      *
    #      * @return The Best Hand given the current list of cards
    #      
    def getBestHand(self):
        """ generated source for method getBestHand """
        try:
            return self.isRoyalFlush()
        except Exception as e:
            pass
        try:
            return self.isStraightFlush()
        except Exception as e:
            pass
        try:
            return self.isFourOfAKind()
        except Exception as e:
            pass
        try:
            return self.isFullHouse()
        except Exception as e:
            pass
        try:
            return self.isFlush()
        except Exception as e:
            pass
        try:
            return self.isStraight()
        except Exception as e:
            pass
        try:
            return self.isThreeOfAKind()
        except Exception as e:
            pass
        try:
            return self.isTwoPairs()
        except Exception as e:
            pass
        try:
            return self.isOnePair()
        except Exception as e:
            pass
        return self.isHighHand()

    def isRoyalFlush(self):
        """ generated source for method isRoyalFlush """
        #  Is there a suit that contains 5 cards?
        potentialRoyalFlush = None
        for suit, cards in self.suitDistribution.iteritems():
            if len(cards) >= PokerHand.ROYAL_FLUSH.getCardsRequired():
                potentialRoyalFlush = cards
                break

        if potentialRoyalFlush == None:
            raise Exception("No Royal Flush found")

        potentialRoyalFlush = CardsUtil.getHighestSortedAndExclude(5, potentialRoyalFlush, None)
        counter = PokerHand.ROYAL_FLUSH.getCardsRequired() - 1

        checkList = [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING, Rank.ACE]
        for r in checkList:
            c = potentialRoyalFlush[counter];
            counter = counter - 1
            if r != c.getRank():
                raise Exception("No Royal Flush found")

        return Hand(potentialRoyalFlush, PokerHand.ROYAL_FLUSH)

    def isStraightFlush(self):
        """ generated source for method isStraightFlush """
        #  Is there a suit that contains 5 cards?
        potentialStraightFlush = None
        for suit, cards in self.suitDistribution.iteritems():
            if len(cards) >= PokerHand.STRAIGHT_FLUSH.getCardsRequired():
                potentialStraightFlush = cards
                break

        if potentialStraightFlush == None:
            raise Exception("No Straight Flush found")

        potentialStraightFlush = CardsUtil.getLongestConsecutiveSubset(potentialStraightFlush)
        if len(potentialStraightFlush) < PokerHand.STRAIGHT_FLUSH.getCardsRequired():
            raise Exception("No Straight Flush of sufficient length found")

        size = len(potentialStraightFlush)
        if size > PokerHand.STRAIGHT_FLUSH.getCardsRequired():
            potentialStraightFlush = potentialStraightFlush[size - PokerHand.STRAIGHT_FLUSH.getCardsRequired():size]

        return Hand(reversed(potentialStraightFlush), PokerHand.STRAIGHT_FLUSH)

    def isFourOfAKind(self):
        """ generated source for method isFourOfAKind """
        #  Is there a rank that contains 4 cards?
        potentialFourOfAKind = None
        for rank, cards in self.rankDistribution.iteritems():
            if len(cards) == PokerHand.FOUR_OF_A_KIND.getCardsRequired():
                potentialFourOfAKind = cards
                break

        if potentialFourOfAKind == None:
            raise Exception("No Four of a kind found")

        #  Sort by suit
        potentialFourOfAKind = sorted(potentialFourOfAKind, key=lambda x: card_sort_value_by_suit(x), reverse=True)
        restOfCards = CardsUtil.getHighestSortedAndExclude(5 - PokerHand.FOUR_OF_A_KIND.getCardsRequired(), self.cards, potentialFourOfAKind)
        potentialFourOfAKind = potentialFourOfAKind + restOfCards

        return Hand(potentialFourOfAKind, PokerHand.FOUR_OF_A_KIND)

    def isFullHouse(self):
        """ generated source for method isFullHouse """
        highestThreeOfAKind = CardsUtil.getHighestOfSameRank(PokerHand.THREE_OF_A_KIND.getCardsRequired(), self.cards)
        if len(highestThreeOfAKind) == 0:
            raise Exception("No three of a kind found for Full House")
        highestTwoOfAKind = CardsUtil.getHighestOfSameRankExcluding(PokerHand.ONE_PAIR.getCardsRequired(), self.cards, highestThreeOfAKind[0].getRank())
        if len(highestTwoOfAKind):
            raise Exception("No two of a kind found for Full House")
        fullHouse = highestThreeOfAKind + highestTwoOfAKind
        return Hand(fullHouse, PokerHand.FULL_HOUSE)

    def isFlush(self):
        """ generated source for method isFlush """
        potentialFlush = None
        for suit, cards in self.suitDistribution.iteritems():
            if len(cards) >= PokerHand.FLUSH.getCardsRequired():
                potentialFlush = cards
                break
        if potentialFlush == None:
            raise Exception("No Flush found")
        potentialFlush = CardsUtil.getHighestSortedAndExclude(PokerHand.FLUSH.getCardsRequired(), potentialFlush, None)
        return Hand(potentialFlush, PokerHand.FLUSH)

    def isStraight(self):
        """ generated source for method isStraight """
        potentialStraight = CardsUtil.getLongestConsecutiveSubset(self.cards)
        if len(potentialStraight) < PokerHand.STRAIGHT.getCardsRequired():
            raise Exception("No straight found")

        size = len(potentialStraight)
        if size > PokerHand.STRAIGHT.getCardsRequired():
            potentialStraight = potentialStraight[size - PokerHand.STRAIGHT.getCardsRequired():size]

        return Hand(reversed(potentialStraight), PokerHand.STRAIGHT)

    def isThreeOfAKind(self):
        """ generated source for method isThreeOfAKind """
        #  Is there a rank that contains 3 cards?
        potentialThreeOfAKind = None
        for rank, threeOfAKind in self.rankDistribution.iteritems():
            if len(threeOfAKind) == PokerHand.THREE_OF_A_KIND.getCardsRequired():
                #  There might be more than one set of three-of-a-kind, choose
                #  the highest ranking one.
                if potentialThreeOfAKind != None:
                    if potentialThreeOfAKind[0].getRank().getOrderValue() < threeOfAKind[0].getRank().getOrderValue():
                        potentialThreeOfAKind = threeOfAKind
                else:
                    potentialThreeOfAKind = threeOfAKind

        if potentialThreeOfAKind is None:
            raise Exception("No Three of a kind found")

        potentialThreeOfAKind = sorted(potentialThreeOfAKind, key=lambda x: card_sort_value_by_suit(x), reverse=True)
        potentialThreeOfAKind = potentialThreeOfAKind + CardsUtil.getHighestSortedAndExclude(5 - PokerHand.THREE_OF_A_KIND.getCardsRequired(), self.cards, potentialThreeOfAKind)
        return Hand(potentialThreeOfAKind, PokerHand.THREE_OF_A_KIND)

    def isTwoPairs(self):
        """ generated source for method isTwoPairs """
        highestTwoOfAKind = CardsUtil.getHighestOfSameRank(PokerHand.ONE_PAIR.getCardsRequired(), self.cards)
        if len(highestTwoOfAKind) == 0:
            raise Exception("No two of a kind found in Two pairs")
        nextHighestTwoOfAKind =CardsUtil.getHighestOfSameRankExcluding(PokerHand.ONE_PAIR.getCardsRequired(), self.cards, highestTwoOfAKind[0].getRank())
        if len(nextHighestTwoOfAKind) == 0:
            raise Exception("No second two of a kind found in Two pairs")
        twoPairs = highestTwoOfAKind + nextHighestTwoOfAKind
        twoPairs = twoPairs + CardsUtil.getHighestSortedAndExclude(5 - PokerHand.TWO_PAIRS.getCardsRequired(), self.cards, twoPairs)
        return Hand(twoPairs, PokerHand.TWO_PAIRS)

    def isOnePair(self):
        """ generated source for method isOnePair """
        potentialOnePair = None
        for rank, cards in self.rankDistribution.iteritems():
            if len(cards) == 2:
                if potentialOnePair != None:
                    raise Exception("Already found a pair, this hand contains two pairs")
                potentialOnePair = cards
            elif len(cards) > 2:
                raise Exception("There exists a better match than one pair")
        if potentialOnePair == None:
            raise Exception("No One pair found")
        restOfCards = CardsUtil.getHighestSortedAndExclude(5 - PokerHand.ONE_PAIR.getCardsRequired(), self.cards, potentialOnePair)
        potentialOnePair = sorted(potentialOnePair, key=lambda x: card_sort_value_by_suit(x))
        potentialOnePair = potentialOnePair + restOfCards
        return Hand(potentialOnePair, PokerHand.ONE_PAIR)

    def isHighHand(self):
        """ generated source for method isHighHand """
        return Hand(CardsUtil.getHighestSortedAndExclude(5, self.cards, None), PokerHand.HIGH_HAND)

