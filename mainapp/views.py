from django.shortcuts import render
from django.http import HttpResponse
import sys, os

# Create your views here.


def test(request):
    return HttpResponse("test api ....")


import logging
logger = logging.getLogger(__name__)
logger = logging.getLogger('django')
logger_demo = logging.getLogger('demo_log')
logger_city = logging.getLogger('city_log')


# def home_page(request):
#     logger.info("I print on the console and also on info.log upper")
#     logger.error("I print on the console and also on info.log upper")
#     logger_demo.info("I print on demo.log upper")
#     logger_demo.error("I print on demo.log upper")
#     logger_city.info("I print on city.log upper")
#     logger_city.error("I print on city.log upper")
#     return render(request,"login.html")


def home_page(request):
    try:
        raise Exception('Error')   
    except Exception as e: 
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        logger_city.error(exc_type , fname , exc_tb.tb_lineno)
        logger_city.error('hi')
    return render(request,"login.html")

