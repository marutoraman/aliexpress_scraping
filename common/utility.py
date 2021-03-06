# -*- coding: utf-8 -*-
from datetime import datetime as dt
from bs4 import BeautifulSoup as bs
import requests

def now_timestamp():
    return dt.now().strftime("%Y-%m-%d_%H_%M_%S")

def list_to_bool(l:list):
    bool_list=[]
    for item in l:
        bool_list.append(False if item == "0" or item == 0 else True)
    
    return bool_list

def create_proxy_dict(id,password,host,port,proxy_flg=True):
    if proxy_flg:
        proxy_url=f"http://{id}:{password}@{host}:{port}"
        return {
            "http": proxy_url,
            "https": proxy_url
        }
    else:
        return {}

def get_global_ip():
    #return socket.gethostbyname(socket.gethostname())
    try:
        res = requests.get("http://inet-ip.info/")
        soup = bs(res.text, "html.parser")
        return soup.select_one("table tbody tr td:nth-child(2)").text
    except Exception as e:
        print(e)
        return None
    
    
def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return: 
    """
    for idx in range(0, len(l), n):
        yield l[idx:idx + n]


def fetch_currency_rate(base: str, to: str):
    res = requests.get("http://fx.mybluemix.net/")
    res.raise_for_status()
    res_dict = res.json()
    try:
        return res_dict["result"]["rate"][base + to]
    except:
        raise Exception(f"exchange currency error: {base}->{to}")