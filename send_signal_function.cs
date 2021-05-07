// NET FRAMEWORK USED: 4.6

private void send_Signal(string id, string code, string buy_sell)
{
    var dict = new Dictionary<string, string>();
    dict.Add("strategyId", id);
    dict.Add("code", code);
    dict.Add("sellBuyType", buy_sell);

    HttpRequestMessage request = new HttpRequestMessage();
    request.Method = HttpMethod.Post;
    request.Content = new FormUrlEncodedContent(dict);
    request.RequestUri = new Uri("https://vinance.vn/signals");

    HttpResponseMessage response = client.SendAsync(request).Result;
    String responseMsg = response.Content.ReadAsStringAsync().Result;

}
