import time
import re
import json
import typing
from pprint import pprint
import datetime

from common.selenium_manager import SeleniumManager
from models.aliexpress_item import AliexpressItem
from common.logger import set_logger
from common.utility import *

logger = set_logger(__name__)

class AliexpressScraping():
    DOMAIN_URL = "https://ja.aliexpress.com"
    LOGIN_URL = "https://login.aliexpress.com/"

    