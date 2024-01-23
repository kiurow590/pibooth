from pibooth.utils import LOGGER
import pibooth


class QuestionaryPlugin(object) :
    name = 'pibooth-core:question'
    
    def __init__(self, plugin_manager):
        self._pm = plugin_manager
        LOGGER.info("Questionary plugin loaded")
        
    @pibooth.hookimpl
    def state_previewQuestion_enter(cfg, app):
        app.leds.blink(on_time=0.5, off_time=0.5)
        
    @pibooth.hookimpl
    def state_previewQuestion_exit(self, app):
        app.leds.off()
        
    @pibooth.hookimpl
    def state_previewQuestion_do(cfg, app, win, events):
        LOGGER.info("Question state")
        
        
    @pibooth.hookimpl
    def state_previewQuestion_validate(self, app, events):
        LOGGER.info("Question state")