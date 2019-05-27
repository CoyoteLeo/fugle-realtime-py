from pandas.io.json import json_normalize
from requests import get


def quote(
    apiToken="demo",
    apiVersion="v0",
    host="api.fugle.tw",
    output="pandas",
    symbolId="2884",
):
    url = "https://{}/realtime/{}/intraday/quote".format(host, apiVersion)
    params = dict(apiToken=apiToken, symbolId=symbolId)
    response = get(url=url, params=params)
    json = response.json()
    if response.status_code != 200:
        if output == "pandas":
            return json_normalize(json)
        else:
            return json
    quote = json["data"]["quote"]
    if output == "pandas":
        return json_normalize(quote)
    else:
        return quote