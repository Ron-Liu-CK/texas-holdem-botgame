#!/usr/bin/env python

from common.game.definitions.Suit import *
from common.game.definitions.Rank import *
from common.game.definitions.CardSortBy import *
from common.game.Card import Card

#
#  * A set of utilities for searching and manipulating a List of Cards.
#  *
#  * @author emil
#  
class CardsUtil(object):
    #
    #      * Creates a map where cards are organized according to their Rank.
    #      *
    #      * @param cards
    #      *
    #      * @return a map where cards are organized according to their Rank
    #      
    @staticmethod
    def getRankDistribution(cards):
        """
        :param cards:
        :return: dict[Rank, list[Card]]
        """
        distribution = {}       # type: dict[Rank, list[Card]]
        for c in cards:
            if c.getRank() in distribution:
                distribution[c.getRank()].append(c)
            else:
                card_list = [c]
                distribution[c.getRank()] = card_list

        return distribution

    # 
    #      * Creates a map where cards are organized according to their Suit.
    #      *
    #      * @param cards
    #      *
    #      * @return a map where cards are organized according to their Suit
    #      
    @staticmethod
    def getSuitDistribution(cards):
        """
        :param cards:
        :return: Card
        """
        distribution = {}       # type: dict[Suit, list[Card]]
        for c in cards:
            if c.getSuit() in distribution:
                distribution[c.getSuit()].append(c)
            else:
                card_list = [c]
                distribution[c.getSuit()] = card_list
        return distribution

    # 
    #      * Null safe merge of two lists. If both lists are empty or null an empty
    #      * list is returned.
    #      *
    #      * @param first
    #      * @param second
    #      *
    #      * @return The merge of the lists first and second
    #      
    @staticmethod
    def merge(first, second):
        """
        :param first: list[Card]
        :param second: list[Card]
        :return:
        """
        return first + second

    # 
    #      * Creates a new list containing only the cards in target that don't exist
    #      * in remove. Null safe. If target is empty or null an empty list will be
    #      * returned.
    #      *
    #      * @param target
    #      * @param remove
    #      *
    #      * @return A copy of the target list with all elements from remove removed.
    #      
    @staticmethod
    def remove(target, remove):
        """
        :param target: list[Card]
        :param remove: list[Card]
        :return:
        """
        result = []

        if remove is None:
            remove = []

        for card in target:
            if not card in remove:
                result.append(card)

        return result


    # 
    #      * Sorts the list of cards by Rank in descending order and removes any
    #      * occurrences of cards in the list of excluded cards.
    #      * <p/>
    #      * Example: getHighestSortedAndExclude(2, {5d, 9c, Jd, 2c, Qs}, {Qs, 9c})
    #      * Result: {Jd, 5d}
    #      *
    #      * @param noof    The max length of the resulting list of cards
    #      * @param cards
    #      * @param exclude A list of cards to exclude from the result
    #      *
    #      * @return A descending (by Rank) list of cards
    #      
    @staticmethod
    def getHighestSortedAndExclude(noof, cards, exclude):
        """
        :param noof: int
        :param cards:  list[Card]
        :param exclude: list[Card]
        :return:
        """
        removed = CardsUtil.remove(cards, exclude)
        removed = sorted(removed, key=lambda x: card_sort_value_by_rank(x), reverse=True)
        if noof > len(removed):
            return removed
        return removed[0:noof]

    # 
    #      * Sorts the list of cards in a new List.
    #      *
    #      * @param sortMethod
    #      * @param cards
    #      *
    #      * @return A new List sorted by Rank och Suit.
    #      
    @staticmethod
    def sortBy(sortMethod, cards):
        return sorted(cards, key=lambda x: sortMethod(x))

    # 
    #      * Returns the longest possible list of cards in Rank order. A card ranked
    #      * ACE can be both at the beginning of a list or at the end. If no
    #      * consecutive list can be found in the list of cards an empty list is
    #      * returned.
    #      * <p/>
    #      * Example: getLongestConsecutiveSubset({5h, 3s, Ad, As, 2c, Kh, 4c})
    #      * Returns: {Ad, 2c, 3s, 4c, 5h}
    #      *
    #      * @param cards
    #      *
    #      * @return The longest consecutive sublist of cards found or the empty list
    #      *         if none found.
    #      
    @staticmethod
    def getLongestConsecutiveSubset(cards):
        """
        :param cards: list[Card]
        :return: list[Card]
        """
        sortedCards = CardsUtil.removeDuplicatesByRankAndSortByRank(cards)

        #  If an ACE exists in cards place it at beginning as well since
        #  in a straight it may act as numeric value 14 or 1.
        lastCard = sortedCards[-1]  # type: Card
        if lastCard.getRank() == Rank.ACE:
            sortedCards.insert(0, lastCard)
        largestConsecutive = []
        currStartPos = 0
        previousCard = None
        i = 0
        while i < len(sortedCards):
            currentCard = sortedCards[i]
            if previousCard is None or ((previousCard.getRank().getOrderValue() + 1 != currentCard.getRank().getOrderValue()) and not (previousCard.getRank() == Rank.ACE and currentCard.getRank().getOrderValue() == 2)):
                #  Found consecutive subset larger than one,
                #  check if it is longer than the previously
                #  known one.
                if currStartPos < i - 1 and i - currStartPos > len(largestConsecutive) - 1:
                    largestConsecutive = sortedCards[currStartPos:(i+currStartPos)]
                currStartPos = i
            previousCard = currentCard
            i += 1
        #  In case the end is part of the largest consecutive sublist
        if currStartPos < len(sortedCards) - 1 and len(sortedCards) - 1 - currStartPos > len(largestConsecutive) - 1:
            largestConsecutive = sortedCards[currStartPos:len(sortedCards)]

        return largestConsecutive

    # 
    #      * Sorts the list of cards by Rank and then removes any cards of the same
    #      * Rank.
    #      * <p/>
    #      * Example: removeDuplicatesByRankAndSortByRank({5h, Jd, 3s, 5d, Js}
    #      * Returns: {3s, 5d, Jd}
    #      *
    #      * @param cards
    #      *
    #      * @return A sorted list of Cards with no duplicate Ranks.
    #      
    @staticmethod
    def removeDuplicatesByRankAndSortByRank(cards):
        """ generated source for method removeDuplicatesByRankAndSortByRank """
        sortedCards = CardsUtil.sortBy(card_sort_value_by_rank, cards)  # type: list[Card]
        result = []
        previousCard = None
        for c in sortedCards:
            if previousCard is None or previousCard.getRank() != c.getRank():
                result.append(c)
            previousCard = c

        return result

    # 
    #      * Searches a List of Cards for cards of the same rank that exist in least
    #      * noof times and returns the highest ranking list, excluded any Card of the
    #      * excluded Rank.
    #      *
    #      * @param noof         The minimum number of cards of same rank
    #      * @param cards        The list of cards available
    #      * @param excludedRank A rank to exclude from the result
    #      *
    #      * @return A list of cards of noof length of the highest rank.
    #      *
    #      * @see #getHighestOfSameRank(int, List)
    #      
    @staticmethod
    def getHighestOfSameRankExcluding(noof, cards, excludedRank):
        """
        :param noof: int
        :param cards: list[Card]
        :param excludedRank: Rank
        :return: list[Card]
        """
        activeCardList = []
        for c in cards:
            if c.getRank() != excludedRank:
                activeCardList.append(c)

        return CardsUtil.getHighestOfSameRank(noof, activeCardList)

    # 
    #      * Searches a List of Cards for cards of the same rank that exist in least
    #      * noof times and returns the highest ranking list.
    #      * <p/>
    #      * Example: getHighestOfSameRank(2, {5h, Jd, 3s, 5d, Js} Returns: {Jd, Js}
    #      *
    #      * @param noof  The minimum number of cards of same rank
    #      * @param cards The list of cards available
    #      *
    #      * @return A list of cards of noof length of the highest rank.
    #      
    @staticmethod
    def getHighestOfSameRank(noof, cards):
        """
        :param noof: int
        :param cards: list[Card]
        :return: list[Card]
        """
        result = []
        currBestRank = None     # type: Rank
        distribution = CardsUtil.getRankDistribution(cards)

        for key, cards in distribution:
            if len(cards) >= noof:
                if currBestRank is None or currBestRank.compareTo(key) < 0:
                    currBestRank = key
                    result = cards

        result = sorted(result, key=lambda x: card_sort_value_by_suit(x))
        if len(result) > noof:
            result = result[0:noof]

        return result

