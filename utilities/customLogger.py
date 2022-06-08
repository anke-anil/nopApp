import logging, logging.handlers

class LogGen:

    @staticmethod
    def loggen():

        # logging.basicConfig(filename=".\\logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        formatter = logging.Formatter('%(asctime)s:%(levelname)s : %(name)s : %(message)s')
        file_handler = logging.FileHandler('.//logs/automation.log')
        file_handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        if (logger.hasHandlers()):
            logger.handlers.clear()
        logger.addHandler(file_handler)
        return logger

