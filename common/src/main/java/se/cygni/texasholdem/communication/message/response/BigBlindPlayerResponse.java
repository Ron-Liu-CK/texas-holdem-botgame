package se.cygni.texasholdem.communication.message.response;

import se.cygni.texasholdem.communication.message.type.IsATexasMessage;
import se.cygni.texasholdem.game.Player;

@IsATexasMessage
public class BigBlindPlayerResponse extends TexasResponse {

    public Player bigBlindPlayer;
}
