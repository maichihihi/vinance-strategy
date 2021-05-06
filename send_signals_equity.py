import json
from urllib.parse import urlencode
import requests
from requests import Response
import datetime as dt
from datetime import datetime
import pandas as pd
import time


def post_rest(url, body, headers, print_log=True, encode_require=False):
    if print_log:
        print("POST REQUEST - url={}, body={}".format(url, body))
    if encode_require:
        response: Response = requests.post(url, data=urlencode(body), headers=headers)
    else:
        response: Response = requests.post(url, json=body, headers=headers)
    if response.status_code != 200:
        print(response.text)
        content = None
    else:
        try:
            content = response.json()
        except BaseException as e:
            print(response.text)
            content = None
            raise e
    if print_log:
        print("{} - POST RESPONSE - url={}, data={}".format(response.status_code, url, content))
    return content


strategy_id = "10"
buy_sell = "BUY"
code_list = ["DGW", "HAX", 'NKG', 'PET', 'SHI', 'SMC', 'TDG']
# code = "AMD"
for code in code_list:
    data_sent = {"strategyId": strategy_id, "sellBuyType": buy_sell, "code": code}

    import_response = post_rest(url='http://172.31.32.110/signals', body=data_sent, headers={})
    time.sleep(5)
    print("DONE : {}".format(code))
