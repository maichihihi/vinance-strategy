import json
from urllib.parse import urlencode
import requests
from requests import Response
import datetime as dt
from datetime import datetime
import pandas as pd


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

# you can read backtest from csv file, profit of equity strategies start with 100, for derivatives strategies, it starts with 0
backtest_profit = pd.read_csv("PE_PB_BackTest.csv")

json_result = backtest_profit.to_json(orient='records')
abc = json.loads(json_result)
data_array = []

strategy_id = 3
for record in abc:
    data = {
        "strategy": strategy_id,
        "date": str(record.get('date')),
        "accumulated_profit": round(record.get('profit'), 2)
    }
    data_array.append(data)
print(data_array)
# the format of data_array should be:
# [{'strategy': 10, 'date': '20141231', 'accumulated_profit': 1},
#  {'strategy': 10, 'date': '20150130', 'accumulated_profit': 1.01},
#  {'strategy': 10, 'date': '20150227', 'accumulated_profit': 1.02},
#  {'strategy': 10, 'date': '20150331', 'accumulated_profit': 1.05},
#  {'strategy': 10, 'date': '20150427', 'accumulated_profit': 1.15},
#  {'strategy': 10, 'date': '20150529', 'accumulated_profit': 1.23},
#  {'strategy': 10, 'date': '20150630', 'accumulated_profit': 1.26},
#  {'strategy': 10, 'date': '20150731', 'accumulated_profit': 1.26},
#  {'strategy': 10, 'date': '20150831', 'accumulated_profit': 1.26},
#  {'strategy': 10, 'date': '20150930', 'accumulated_profit': 1.31},
#  {'strategy': 10, 'date': '20151030', 'accumulated_profit': 1.51},
#  {'strategy': 10, 'date': '20151130', 'accumulated_profit': 1.39},
#  {'strategy': 10, 'date': '20151231', 'accumulated_profit': 1.58},
#  {'strategy': 10, 'date': '20160129', 'accumulated_profit': 1.51},
#  {'strategy': 10, 'date': '20160229', 'accumulated_profit': 1.59},
#  {'strategy': 10, 'date': '20160331', 'accumulated_profit': 1.84},
#  {'strategy': 10, 'date': '20160429', 'accumulated_profit': 2.12}]

# Uncomment below line to send backtest data: 
# import_response = post_rest(url='http://172.31.32.110/back-test-data/upload', body=data_array, headers={})
