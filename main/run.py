

import os
import sys
import fire
import pandas as pd

# プロジェクトルートをPATHに追加
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from common.utility import now_timestamp
from engine.aliexpress import AliexpressScraping
from engine.aliexpress_requests import AliexpressRequests

# ログ出力設定
from common.logger import set_logger
logger = set_logger(__name__)


def selenium(url :str, page_limit: int=5):
    pass

if __name__ == "__main__":
    fire.Fire(selenium)