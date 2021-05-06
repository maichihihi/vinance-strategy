# vinance-strategy
# This is the manual for AI advisor

1. Create strategy
To create strategy, we go to: https://vinance.vn/content-admin/strategy
Fill out the form to create new strategy
Strategy id is taken from the url after being created. 

Eg: vinance.vn/strategy/10 → strategy id = 10

2. Upload backtest data
- Api url: http://172.31.32.110/back-test-data/upload (need VPN)
- Alternative url: https://vinance.vn/back-test-data/upload (no need VPN)
- Method : POST
- Headers: {}
- json (the data upload is in this form): 
 [{'strategy': 10, 'date': '20141231', 'accumulated_profit': 1},
 {'strategy': 10, 'date': '20150130', 'accumulated_profit': 1.01},
 {'strategy': 10, 'date': '20150227', 'accumulated_profit': 1.02},
 {'strategy': 10, 'date': '20150331', 'accumulated_profit': 1.05},
 {'strategy': 10, 'date': '20150427', 'accumulated_profit': 1.15},
 {'strategy': 10, 'date': '20150529', 'accumulated_profit': 1.23},
 {'strategy': 10, 'date': '20150630', 'accumulated_profit': 1.26},
 {'strategy': 10, 'date': '20150731', 'accumulated_profit': 1.26}]



3. Send signals
- Api url: http://172.31.32.110/signals (need VPN)
- Alternative url: https://vinance.vn/signals (no need VPN)
- Method : POST
- Header : {}
- data : {"strategyId": "10", "sellBuyType": "SELL", "code": "AMD"}

*Note : each signal contains only 1 code

Python code example is availabe for uploading backtest and signals
 
4. Subscribe and receive signals from telegram
- Step 1: Create your Telegram username in the app
- Step 2: Find username **VinanceSignalBot** in Telegram, start conversation
- Step 3: Log in to your account in vinance.vn
- Step 4: Go to profile settings, fill in your Telegram Username.
- Step 5: Click button **FOLLOW** to follow any strateies you want in AI Advisor. New signals will be sent to you via Telegram message
*Note: You can choose to unfollow a strategy to stop receiving new signals from that strategy

