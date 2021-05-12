# vinance-strategy
# This is the manual for AI advisor

**1. Create strategy**
```
- To create strategy, we go to: https://vinance.vn/content-admin/strategy
- Fill out the form to create new strategy
- Strategy id is taken from the url after being created. 
Eg: vinance.vn/strategy/10 → strategy id = 10
```
**2. Upload backtest data**
```
- Api url: https://vinance.vn/back-test-data/upload (no need VPN)
- Alternative url: http://172.31.32.110/back-test-data/upload (need VPN)
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

```
**3. Send signals**
```
- Api url: https://vinance.vn/signals (no need VPN)
- Alternative url: http://172.31.32.110/signals (need VPN)
- Method : POST
- Header : {}
- data : {"strategyId": "10", "sellBuyType": "SELL", "code": "AMD"}

*Note : 
- each signal contains only 1 code
- signals have to send 1 day after creating new strategy, otherwise profit will be miscalculated
- If we use Winform C#, we should use .NET Framework 4.6
**Python code example is availabe for uploading backtest and signals**

```
**4. Subscribe and receive signals from Telegram**
```
- Step 1: Create a Telegram account and username in the app
- Step 2: Find username **VinanceSignalBot** in Telegram, start conversation
- Step 3: Log in to your account in vinance.vn
- Step 4: Go to profile settings, fill in your Telegram Username.
- Step 5: Click button **FOLLOW** to follow any strateies you want in AI Advisor. New signals will be sent to you via Telegram message
*Note: You can choose to unfollow a strategy to stop receiving new signals from that strategy

In Vietnamese:
- Bước 1: Tạo một tài khoản và username trên Telegram
- Bước 2: Tìm kiếm tài khoản **VinanceSignalBot** trên Telegram và bắt đầu cuộc trò chuyện
- Bước 3: Đăng nhập vào tài khoản của bạn trên vinance.vn
- Bước 4: Vào mục thông tin cá nhân và điền username Telegram của bạn
- Bước 5: Bấm nút **Theo dõi** những chiến thuật bạn muốn và bạn có thể nhận được tín hiệu đầu tư qua Telegram
*Chú ý: Bạn có thể bỏ theo dõi chiến thuật nếu muốn ngừng nhận tín hiệu
```
