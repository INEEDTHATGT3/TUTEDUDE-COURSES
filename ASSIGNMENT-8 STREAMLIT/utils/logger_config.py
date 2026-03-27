import logging
import sys

def get_logger(name):
    logging.basicConfig(
        #Centralized logging configuration
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler("app_log.log"), logging.StreamHandler(sys.stdout)]
    )
    return logging.getLogger(name)

