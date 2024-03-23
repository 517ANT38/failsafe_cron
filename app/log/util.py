
import logging

FORMAT = '%(asctime)s %(levelname)s: %(message)s'

def get_file_handler(filename:str):
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(FORMAT))
    return file_handler



def get_logger(filename:str,name:str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler(filename))  
    return logger
