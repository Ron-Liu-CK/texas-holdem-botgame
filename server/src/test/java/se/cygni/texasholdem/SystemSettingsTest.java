package se.cygni.texasholdem;

import org.junit.Assert;
import org.junit.Test;

public class SystemSettingsTest {

    @Test
    public void testSystemProperties() {

        System.setProperty(SystemSettings.PREFIX_PROPERTY + "defaultPort", "666");
        System.setProperty(SystemSettings.PREFIX_PROPERTY + "host", "doot.se");

        final SystemSettings sp = new SystemSettings();
        Assert.assertEquals(666, sp.getPort());
        Assert.assertEquals("doot.se", sp.getHost());
    }
}
