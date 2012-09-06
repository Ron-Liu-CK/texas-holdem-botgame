<%@ include file="/WEB-INF/views/includes/taglibs.jsp" %>


<!DOCTYPE HTML>
<html>
<head>

    <title>Cygni Texas Hold'em</title>

    <%@ include file="/WEB-INF/views/includes/head.jsp" %>
</head>
<body onload="prettyPrint()">

<h:navbar section="gettingstarted"/>

<div class="container">
        <div class="hero-unit">
            <h1>Getting started</h1>
            <p>and code samples</p>
        </div>

        <div class="row">
            <div class="span6">
                <div class="well well-large">
                    <h2>Getting started with a Java client</h2>
                    <p>First download the example project:
                        <a href="http://192.168.10.100/download/texas-holdem-java-client.zip">texas-holdem-java-client.zip</a>
                    </p>
                    <p>
                        Extract the zip and import in your favorite IDE. If you are missing any dependencies download
                        this maven <a href="http://192.168.10.100/download/settings.xml">settings.xml</a> and place
                        it in ~/.m2.
                    </p>
                    <p>
                        The class SimplestPossibleBot is included in the project and shown below.
                    </p>
                    <pre class="prettyprint">
public class SimplestPossibleBot extends BasicPlayer {

    private static Logger log = LoggerFactory
            .getLogger(SimplestPossibleBot.class);

    private final String serverHost;
    private final int serverPort;
    private final PlayerClient playerClient;

    public SimplestPossibleBot(String serverHost, int serverPort) {
        this.serverHost = serverHost;
        this.serverPort = serverPort;

        // Initialize the player client
        playerClient = new PlayerClient(this, serverHost, serverPort);
    }

    public void playATrainingGame() throws Exception {
        playerClient.connect();
        playerClient.registerForPlay(Room.TRAINING);
    }

    @Override
    public String getName() {
        throw new RuntimeException("Did you forget to specify a name for your bot?");
    }

    @Override
    public Action actionRequired(ActionRequest request) {

        Action callAction = null;
        Action checkAction = null;
        Action foldAction = null;

        for (final Action action : request.getPossibleActions()) {
            switch (action.getActionType()) {
                case CALL:
                    callAction = action;
                    break;
                case CHECK:
                    checkAction = action;
                    break;
                case FOLD:
                    foldAction = action;
                    break;
                default:
                    break;
            }
        }

        Action action = null;
        if (callAction != null)
            action = callAction;
        else if (checkAction != null)
            action = checkAction;
        else
            action = foldAction;

        log.debug("{} returning action: {}", getName(), action);
        return action;
    }

    @Override
    public void connectionToGameServerLost() {
        log.info("Connection to game server is lost. Exit time");
        System.exit(0);
    }

    public static void main(String... args) {
        SimplestPossibleBot bot = new SimplestPossibleBot("192.168.10.100", 4711);

        try {
            bot.playATrainingGame();

        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }
    }
}

}</pre>
                    <p>This class extends BasicPlayer which has dummy methods for most event calls.
                        The methods getName() and actionRequired(...) must however be implemented.
                        You can use this class as a starting point for you player.</p>


                </div>
            </div>
            <!--/span-->

            <div class="span6">
                <div class="well well-large">
                    <h2>Getting started with a JavaScript client</h2>
                    <p>First download the example project:
                        <a href="http://192.168.10.100/download/texas-holdem-web-client.zip">texas-holdem-web-client.zip</a>
                    </p>
                    <p>Extract the zip and open a terminal window and run:</p>
                    <pre class="prettyprint">
start.sh
                    </pre>
                    <p>This starts a local web server which acts as a proxy to the real game server.</p>
                    <p>Open <a href="http://localhost:8080" target="_blank">localhost</a> and try a test
                    game by clicking on the Poker link.</p>
                    <p>Files to edit to create your own player are located in the subdirectory player.</p>
                </div>
            </div>
            <!--/span-->
        </div>

    <!--/span-->
<!--/row-->

<hr>

<footer>
    <p> &copy; Cygni AB 2012</p>
</footer>

</div><!--/.fluid-container-->


</body>
</html>