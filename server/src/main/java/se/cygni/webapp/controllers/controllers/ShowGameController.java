package se.cygni.webapp.controllers.controllers;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import se.cygni.texasholdem.game.Player;
import se.cygni.texasholdem.server.session.SessionManager;
import se.cygni.texasholdem.server.statistics.StatisticsCollector;
import se.cygni.texasholdem.util.PlayerTypeConverter;

import java.util.List;
import java.util.Locale;

@Controller
public class ShowGameController {

    private static Logger log = LoggerFactory
            .getLogger(ShowGameController.class);

    @Autowired
    SessionManager sessionManager;

    @Autowired
    StatisticsCollector statisticsCollector;


    @RequestMapping(value = "/showgame", method = RequestMethod.GET)
    public String home(Locale locale, Model model) {

        model.addAttribute("gamelog", statisticsCollector.getLastGameLog());

        return "showgame";
    }
}
