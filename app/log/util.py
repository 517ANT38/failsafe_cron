
import logging

FORMAT = '%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s'


class CustomAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        my_context = kwargs.pop('pid', self.extra['pid'])
        return 'process [%s] %s' % (my_context, msg), kwargs

def get_file_handler(filename:str):
    file_handler = logging.FileHandler(filename)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(logging.Formatter(FORMAT))
    return file_handler

def get_logger(filename:str,name:str=None):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler(filename))  
    return CustomAdapter(logger, {"pid": None})
