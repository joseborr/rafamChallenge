from django.utils.deprecation import MiddlewareMixin
import logging
import re

logger = logging.getLogger(__name__)

class CustomHeaderMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.META['HTTP_MY_HEADER'] = "Hello"
        regex = re.compile('^HTTP_')
        log = dict((regex.sub('', header), value) for (header, value) 
            in request.META.items() if header.startswith('HTTP_'))
        logger.debug(log)
        


        
    
        