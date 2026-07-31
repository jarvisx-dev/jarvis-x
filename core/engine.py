from core.logger import Logger
from config.settings import *

class JarvisEngine:

    def __init__(self):

        self.logger = Logger()

    def start(self):

        self.logger.log(f"Starting {APP_NAME} Version {VERSION}")

        self.logger.log("Brain Module Loaded")

        self.logger.log("Voice Module Loaded")

        self.logger.log("Vision Module Loaded")

        self.logger.log("Automation Module Loaded")

        self.logger.log("Memory Module Loaded")

        self.logger.log(f"{APP_NAME} is Ready.")