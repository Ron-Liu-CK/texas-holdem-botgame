package se.cygni.texasholdem.communication.message.response;

import java.util.List;

import se.cygni.texasholdem.communication.message.type.IsATexasMessage;
import se.cygni.texasholdem.game.Card;

@IsATexasMessage
public class CommunityCardsResponse extends TexasResponse {

    public List<Card> communityCards;
}
