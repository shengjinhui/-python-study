import requests

base_url = 'http://pre.qapt.mogu-inc.com/api/query-users'

url = 'http://sunny.mogu-inc.com/jsonp/sellerSearch/1'

header = {
    'Cookie': 'MTGK.sig=PTw-h09aRDpiV2E-4IS6aZL279M; MTGK=TGK-260198-2FXKsLtWJAxSolAlyvrsyOzfPJxN9gGlTUG; tls=2NyCGA8ybVCCQ67N11m',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'content-type': 'application/json'
}


def callSunny(reqData):
    res = requests.get(url=url, json=reqData, headers=header)
    if res.status_code == 200:
        for v in res.text:
            print(v)
        print(res.json())

if __name__ == '__main__':
    reqData = {'userId':'24780516,104221666'}
    res = callSunny(reqData)
    print(res)