import os.path
import requests
import pytest
from routes.Routes import Routes
from utils.ConfigReader import ReadConfig
import logging

#Created path for log file
Log_File= os.path.abspath(os.path.join(os.path.dirname(__file__), "../logs/test_logging.log"))
#Create log folder if it does not exist
os.makedirs(os.path.dirname(Log_File), exist_ok=True)
#create logger object
logger= logging.getLogger("api_logger")
#set logging level (DEBUG= log everything)
logger.setLevel(logging.DEBUG)

#prevent adding multiple handlers again and again
if not logger.handlers:
    #filehandler -> logs will be saved in a file
    file_handler = logging.FileHandler(Log_File, mode="a")
    #set log format
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
    #apply format to file handler
    file_handler.setFormatter(formatter)
    #attach file handller to logger
    logger.addHandler(file_handler)

def log_request_response(response: requests.Response):
    req= response.request

    logger.info(f"Request: {req.method} {req.url}")

    logger.info(f"Request Heades: {req.headers}")

    if req.body:
        logger.info(f"Request Body: {req.body}")

    logger.info(f"Response status: {response.status_code}")

    logger.info(f"Response Headers: {response.headers}")

    try:
        logger.info(f"Response body: {response.json()}")
    except Exception:
        logger.info(f"Response body: {response.text}")

@pytest.fixture(scope="class")
def setup():

    orginal_request= requests.Session.request

    def custom_request(self, method, url, **kwargs):
        #Call original request
        response= orginal_request(self, method,url, **kwargs)
        #log request and response
        log_request_response(response)
        return response

    #Override requests.session.request with custom funtion
    requests.Session.request=custom_request

    yield {"base_url": Routes.Base_Url, "config_reader": ReadConfig}
