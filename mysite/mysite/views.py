from django.http import HttpResponse
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def root(request):
    logger.info("this is test info")
    logger.debug('this is debug log')
    logger.error('this is error log')
    return HttpResponse("hello world")