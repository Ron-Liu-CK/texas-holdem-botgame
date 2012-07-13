package se.cygni.texasholdem.client.message;

import org.codemonkey.swiftsocketclient.ServerMessageToClient;
import org.codemonkey.swiftsocketclient.UnknownMessageException;

import se.cygni.texasholdem.communication.message.TexasMessage;
import se.cygni.texasholdem.communication.message.TexasMessageParser;

public class ServerToClientMessage implements
        ServerMessageToClient<ServerMessageReceiver> {

    private TexasMessage message;

    @Override
    public void execute(final ServerMessageReceiver serverMessageReceiver)
            throws UnknownMessageException {

    	serverMessageReceiver.onMessageReceived(message);

    }

    @Override
    public void decode(final String requestStr) {

        try {
            message = TexasMessageParser.decodeMessage(requestStr);
        } catch (final Exception e) {
            throw new IllegalArgumentException(e.getMessage());
        }

    }

}