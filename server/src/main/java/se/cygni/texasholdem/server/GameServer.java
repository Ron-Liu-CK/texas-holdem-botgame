package se.cygni.texasholdem.server;

import java.util.HashMap;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import se.cygni.texasholdem.game.BotPlayer;
import se.cygni.texasholdem.table.Table;
import se.cygni.texasholdem.table.TableManager;

import com.googlecode.protobuf.pro.duplex.RpcClientChannel;

@Component
public class GameServer {

    private static Logger log = LoggerFactory
            .getLogger(GameServer.class);

    final Map<String, RpcClientChannel> sessionChannelMap = new HashMap<String, RpcClientChannel>();
    final Map<String, BotPlayer> sessionPlayerMap = new HashMap<String, BotPlayer>();

    private final TableManager tableManager;

    @Autowired
    public GameServer(final TableManager tableManager) {

        this.tableManager = tableManager;
    }

    public BotPlayer getPlayer(final String sessionId) {

        return sessionPlayerMap.get(sessionId);
    }

    public boolean isValidSession(final String sessionId) {

        if (!sessionChannelMap.containsKey(sessionId))
            return false;

        if (!sessionPlayerMap.containsKey(sessionId))
            return false;

        return true;
    }

    public void registerNewClientConnection(
            final String sessionId,
            final RpcClientChannel channel) {

        log.debug("New client connection registered. sessionId: {}", sessionId);

        sessionChannelMap.put(sessionId, channel);
    }

    public void registerClientDisconnect(final String sessionId) {

        log.debug("Player disconnected. sessionId: {}", sessionId);

        sessionChannelMap.remove(sessionId);
        sessionPlayerMap.remove(sessionId);

        final BotPlayer player = getPlayer(sessionId);
        final Table table = tableManager.getTableForSessionId(sessionId);
        if (table != null && player != null) {
            table.removePlayer(player);
        }
    }

    public void registerNewPlayer(final String name, final String sessionId) {

        log.debug("New player registered. Name: {} sessionId: {}", name,
                sessionId);

        // TODO: handle unique name
        final BotPlayer player = new BotPlayer(name, sessionId);
        sessionPlayerMap.put(sessionId, player);

        tableManager.assignPlayerToFreeTable(player);
    }
}
