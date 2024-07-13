import logging
import os

class ExperimentLogger:
    def __init__(self, log_dir, log_file_name):
        self.log_dir = log_dir
        self.log_file_name = log_file_name
        self.logger = self.setup_logger()

    def setup_logger(self):
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        log_file_path = os.path.join(self.log_dir, self.log_file_name)

        logger = logging.getLogger(log_file_path)
        logger.setLevel(logging.DEBUG)

        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        logger.addHandler(fh)
        logger.addHandler(ch)

        return logger

    def log_info(self, message):
        self.logger.info(message)

    def log_debug(self, message):
        self.logger.debug(message)

    def log_error(self, message):
        self.logger.error(message)
