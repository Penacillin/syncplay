from syncplay.ui.ConfigurationGetter import ConfigurationGetter
from syncplay import ui
from syncplay.messages import getMessage

class SyncplayClientManager(object):
    def run(self):
        config = ConfigurationGetter().getConfiguration()
        from syncplay.client import SyncplayClient #Imported later, so the proper reactor is installed
        #interface = ui.getUi(graphical=not config["noGui"])
        interface = ui.getUi(graphical=not config["noGui"])
        self.syncplayClient = SyncplayClient(config["playerClass"], interface, config)
        if self.syncplayClient:
            interface.addClient(self.syncplayClient)
            self.syncplayClient.start(config['host'], config['port'])
        else:
            interface.showErrorMessage(getMessage("unable-to-start-client-error"), True)

