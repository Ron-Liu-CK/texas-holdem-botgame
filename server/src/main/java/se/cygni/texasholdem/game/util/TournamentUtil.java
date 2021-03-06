package se.cygni.texasholdem.game.util;

import se.cygni.texasholdem.dao.model.TournamentLog;
import se.cygni.texasholdem.server.room.Tournament;

import java.util.ArrayList;
import java.util.List;

public final class TournamentUtil {

    private TournamentUtil() {
    }

    public static TournamentLog createTournamentLog(Tournament tournament) {
        if (tournament == null) {
            return null;
        }

        return new TournamentLog(
                tournament.getTournamentId(),
                tournament.getTournamentCounter(),
                tournament.getCreated(),
                tournament.tournamentHasStarted(),
                tournament.tournamentHasEnded(),
                tournament.getPlayerRanking(),
                tournament.getTablePartitions(),
                tournament.getTablesPlayedIds());
    }

    public static List<TournamentLog> createTournamentLogs(List<Tournament> tournaments) {
        List<TournamentLog> tournamentLogs = new ArrayList<TournamentLog>();
        for (Tournament t : tournaments) {
            tournamentLogs.add(createTournamentLog(t));
        }

        return tournamentLogs;
    }
}
