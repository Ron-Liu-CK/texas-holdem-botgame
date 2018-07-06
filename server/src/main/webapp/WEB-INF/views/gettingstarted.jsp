<%@ taglib prefix="spring" uri="http://www.springframework.org/tags" %>

<script type="text/javascript">
    $(document).ready(function () {
        prettyPrint();
    });
</script>

<div class="container">
    <div class="hero-unit">
        <h1>Poker Clients</h1>
    </div>

    <div class="row">
        <div class="span6">
            <div class="well well-large">
                <h2>Java client</h2>


                <a name="java_client_prereq"></a>
                <h3>Prerequisites</h3>

                <p>
                    You need a Java JDK of version 6 or above: <a
                        href="http://www.oracle.com/technetwork/java/javase/downloads/index.html" target="_blank">download
                    Java</a>
                </p>

                <p>
                    You need to install Maven: <a href="http://maven.apache.org/download.html" target="_blank">download
                    Maven</a> </br>
                    Installation instructions: <a href="http://maven.apache.org/download.html#Installation" target="_blank">Maven
                    installation</a>
                </p>


                <h3>Set Up Instructions</h3>
                <p>You need to have a sane Java environment, version 6 or above is okay:</p>
                <pre class="prettyprint">
> java -version
java version "1.7.0_04"
Java(TM) SE Runtime Environment (build 1.7.0_04-b20)
Java HotSpot(TM) Server VM (build 23.0-b21, mixed mode)</pre>

                <p>Maven is needed for project builds and dependency management, version 3 or above:</p>
                <pre class="prettyprint">
> mvn -version
Apache Maven 3.0.4 (r1232337; 2012-01-17 09:44:56+0100)
Maven home: /opt/java/maven-3.0.4
Java version: 1.7.0_04, vendor: Oracle Corporation
Java home: /usr/lib/jvm/jdk1.7.0/jre
Default locale: en_US, platform encoding: ANSI_X3.4-1968
OS name: "linux", version: "3.5.2-linode45", arch: "i386", family: "unix"</pre>

                <p>Download the example project:
                    <a href="/resources/clients/holdem-bot-java-client.zip">texas-holdem-java-client</a>
                    Extract the zip.
                </p>
 <pre class="prettyprint">
> unzip holdem-bot-java-client.zip</pre>
                <p>
                    A simple test run with maven:
                </p>
                    <pre class="prettyprint">
> cd holdem-bot-java-client
> mvn compile exec:java -Dexec.args="<spring:eval
                            expression="@applicationProperties.getProperty('bot.host')"/> <spring:eval
                            expression="@applicationProperties.getProperty('bot.port')"/>"

[INFO] Scanning for projects...
[INFO]
[INFO] -------------------------------------------------------
[INFO] Building texas-holdem-java-client 1.1.10
[INFO] -------------------------------------------------------

    ...
[INFO]
[INFO] --- exec-maven-plugin:1.2.1:java (default-cli) @ texas-holdem-java-client ---
[WARNING]
java.lang.reflect.InvocationTargetException
	...
Caused by: java.lang.RuntimeException:
        Did you forget to specify a name for your bot (hint: your email address is a good idea)?
	at se.cygni.texasholdem.player.FullyImplementedBot.getName(FullyImplementedBot.java:85)
	at se.cygni.texasholdem.client.PlayerClient.(PlayerClient.java:74)
        at se.cygni.texasholdem.player.FullyImplementedBot.(FullyImplementedBot.java:52)
            at se.cygni.texasholdem.player.FullyImplementedBot.main(FullyImplementedBot.java:66)
            ... 6 more
[INFO] -------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] -------------------------------------------------------
[INFO] Total time: 18.871s
[INFO] Finished at: Sun Sep 30 01:44:27 CEST 2012
[INFO] Final Memory: 28M/260M
[INFO] -------------------------------------------------------
[ERROR] Failed to execute goal org.codehaus.mojo:exec-maven-plugin:1.2.1:java (default-cli) on project texas-holdem-java-client: An exception occured while executing the Java class. null: InvocationTargetException: Did you forget to specify a name for your bot (hint: your email address is a good idea)? -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoExecutionException
</pre>
                <p>OOOPs! You need to implement the method getName() properly. Get started and create the best Poker
                    playing Bot possible!</p>

                <p>Hint: The class se.cygni.texasholdem.player.FullyImplementedBot is an example bot that you can use as
                    a starting point.</p>
            </div>
        </div>
        <!--/span-->

        <div class="span6">
            <div class="well well-large">
                <h2>Node.js client</h2>

                <a name="nodejs_client_prereq"></a>

                <h3>Prerequisites</h3>

                <p>
                    Download and install node.js: <a href="http://nodejs.org/" target="_blank">node.js</a>
                </p>

                <h3>Set Up Instructions</h3>

                <p>The commands below illustrate how to run the example bot in node.js</p>

                <p>The texas-holdem-nodejs-client is verified to work with node.js v0.8.8. Older and newer versions may
                    be okay.</p>
                <pre class="prettyprint">
> node -v
v0.8.8</pre>

                <p>Download the example project: <a
                        href="/resources/clients/holdem-bot-nodejs-client.zip">texas-holdem-nodejs-client</a>
                </p>

                <p>Extract the zip</p>
                    <pre class="prettyprint">
> unzip holdem-bot-nodejs-client.zip</pre>

                <p>Do a test run:

                    <pre class="prettyprint">
> cd holdem-bot-nodejs-client
> node play.js <spring:eval
                    expression="@applicationProperties.getProperty('bot.host')"/> <spring:eval
                    expression="@applicationProperties.getProperty('bot.port')"/>
            </pre></p>
                <p>If seeing this error:

                <pre class="prettyprint">

        throw new Error('Did you forget to specify your name? A good idea is t
              ^
Error: Did you forget to specify your name? A good idea is to use your e-mail as username! </pre>
                </p>

                <p>OOOPs! You need to specify a value for the variable playerName in botplayer.js!</p>

                <p>Hint: The file botplayer.js is an example bot that you can use as a starting point.</p>
            </div>

            <div class="well well-large">
                <h2>Python client</h2>

                <a name="nodejs_client_prereq"></a>

                <h3>Prerequisites</h3>

                <p>
                    Download and install Python 2.7: <a href="https://www.python.org/downloads/release/python-2715/" target="_blank">Python 2.7</a>
                </p>

                <h3>Set Up Instructions</h3>

                <p>Download the example project: <a
                        href="/resources/clients/holdem-bot-python-client.zip">texas-holdem-python-client</a>
                </p>

                <p>Extract the zip</p>
                <pre class="prettyprint">
> unzip holdem-bot-python-client.zip</pre>

                <p>Do a test run:

                <pre class="prettyprint">
> cd holdem-bot-python-client
> python run_bot.py <spring:eval
                        expression="@applicationProperties.getProperty('bot.host')"/> <spring:eval
                        expression="@applicationProperties.getProperty('bot.port')"/>
                </pre></p>
            </div>

            <div class="well well-large">
                <h2>Additional Documentation</h2>
                <Ul>
                    <li><a href="http://poker.cygni.se/mavensite/texas-holdem-client/apidocs/">http://poker.cygni.se/mavensite/texas-holdem-client/apidocs/</a></li>
                    <li><a href="http://poker.cygni.se/mavensite/texas-holdem-common/apidocs/">http://poker.cygni.se/mavensite/texas-holdem-common/apidocs/</a></li>
                </Ul>
            </div>
            <!--/span-->
        </div>
    </div>

    <!--/span-->
    <!--/row-->
</div>
<!--/.fluid-container-->
