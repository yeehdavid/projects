import json
import time
import requests
from abnormal.settings import proxies, coins, headers


def get_amplitude():
    result = []
    for coin_name in coins.values():
        time.sleep(1)
        params = {'symbol': coin_name + '_usd', 'type': '1min', 'contract_type': 'quarter', 'size': '120'}
        resp = requests.get('https://www.okex.com/api/v1/future_kline.do', params=params, proxies=proxies, headers=headers)
        data_ = json.loads(resp.text)
        amplitude = ((data_[-1][4] - data_[0][1]) / data_[0][1]) * 100

        result.append(amplitude)
    return result


if __name__ == '__main__':
    print(get_amplitude())
