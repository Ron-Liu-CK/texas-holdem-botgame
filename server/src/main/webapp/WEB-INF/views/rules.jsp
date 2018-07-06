<div class="container">
    <div class="hero-unit">
        <h1>House Rules</h1>

        <p>and testing your bot</p>
    </div>

    <div class="row">
        <div class="span6">
            <div class="well well-large">
                <h2>House rules</h2>

                <p>
                    A table will play until either a winner has been established or all players have quit.
                </p>

                <p>
                    A game plays till either all players but one has folded, or the game has entered the state SHOWDOWN.
                    If the latter the pot is divided according to player hands, bet amounts, etc.
                </p>

                <p>
                    A maximum of ${gamePlan.maxNoofTurnsPerState} turns is allowed per player and state.
                    This is to hinder raise races between players. It is always possible to go ALL-IN.
                </p>

                <p>
                    Raises are always fixed to the current value of the big blind ($10).
                </p>

                <p>
                    A bot player that <em>fails to respond in time (3 sec)</em> or responds with non valid actions (i.e.
                    trying to CHECK when a CALL or RAISE is needed) more than ${gamePlan.maxNoofActionRetries}
                    times in a row will automatically be folded in the current game bout.
                </p>

                <p>
                    Player names must be unique if your name is taken you will not be able to connect and play.
                </p>

                <h2>Training</h2>

                <p>
                    A bot player may train against a few server-bot players that are always alive and eager to play!
                    You can join the TRAINING room upon connection.  The table stops playing as soon as the bot player
                    has either won or lost all of its chips.
                </p>

                <h2>Free play</h2>

                <p>
                    If you'd rather play against other bot players, or battle different versions of your bot,
                    you can join the FREEPLAY room. When there are 3 or more players are connected to FREEPLAY room,
                    the game starts (after an extra minute of waiting to let latecomers join).
                </p>
            </div>
        </div>
        <!--/span-->

        <div class="span6">
            <div class="well well-large">
                <table class="table table-striped">
                    <thead>
                    <tr>
                        <th colspan="2">Numbers</th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>Starting chip amount</td>
                        <td>
                            <div class="pull-right">$${gamePlan.startingChipsAmount}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Big blind</td>
                        <td>
                            <div class="pull-right">$${gamePlan.bigBlindStart}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Small blind</td>
                        <td>
                            <div class="pull-right">$${gamePlan.smallBlindStart}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Blind raise strategy</td>
                        <td>
                            <div class="pull-right">${gamePlan.blindRaiseStrategy}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Big blind raise</td>
                        <td>
                            <div class="pull-right">${gamePlan.bigBlindRaiseStrategyValue}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Small blind raise</td>
                        <td>
                            <div class="pull-right">${gamePlan.smallBlindRaiseStrategyValue}</div>
                        </td>
                    </tr>
                    <tr>
                        <td># rounds between blind raise</td>
                        <td>
                            <div class="pull-right">${gamePlan.playsBetweenBlindRaise}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Max # turns per state</td>
                        <td>
                            <div class="pull-right">${gamePlan.maxNoofTurnsPerState}</div>
                        </td>
                    </tr>
                    <tr>
                        <td>Max # action retries</td>
                        <td>
                            <div class="pull-right">${gamePlan.maxNoofActionRetries}</div>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <!--/span-->
    </div>

    <!--/span-->
    <!--/row-->
</div>
<!--/.fluid-container-->
