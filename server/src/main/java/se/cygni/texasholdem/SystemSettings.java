package se.cygni.texasholdem;

import org.springframework.stereotype.Component;
import se.cygni.texasholdem.util.SystemFieldPopulator;
import java.lang.*;

/**
 * This class configures the system. All properties defined here must have
 * default values. The values may be overridden by a system property of the same
 * name as the field.
 *
 * @author emil
 */
@Component
public class SystemSettings {

    public static final String PREFIX_PROPERTY = "texas.";

    private int defaultPort = 9915;
    private String host = "localhost";

    public SystemSettings() {

        final SystemFieldPopulator fieldPopulator = new SystemFieldPopulator(
                this, PREFIX_PROPERTY);
        fieldPopulator.populateValuesFromSystemProperties();
    }

    public int getPort() {
        String botPort = System.getProperty("botPort");
        if (botPort != null) {
            int port = Integer.valueOf(botPort);
            if (port > 0)
                return port;
        }

        return this.defaultPort;
    }

    public String getHost() {

        return host;
    }

    @SuppressWarnings("unused")
    private void setPort(final int port) {

        this.defaultPort = port;
    }

    @SuppressWarnings("unused")
    private void setHost(final String host) {

        this.host = host;
    }

}
