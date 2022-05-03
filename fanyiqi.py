import requests

url = "https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"  # 翻译的url，参数未确定  js反爬，，，，
'''去掉url中的_o只能英译中，，，，'''
'''翻译有道js反爬'''
param = {
    "smartresult": "dict",
    "smartresult": "rule"  # ?smartresult=dict&smartresult=rule
}
input_ = input("请输入要翻译的词汇")
data = {
    "i": "{}".format(input_),  # important
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": "16508843055804",
    "sign": "8ae9c25f3f4008452c0997c7f5851f87",
    "lts": "1650884305580",
    "bv": "2d1c69266bc998ad23a582ba1c751727",
    "doctype": "json",  # important
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_REALTlME"
}
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}
cookie = {
    "Cookie": 'OUTFOX_SEARCH_USER_ID_NCOO=1556203491.380786; OUTFOX_SEARCH_USER_ID="-277281382@10.169.0.81"; fanyi-ad-closed=0; JSESSIONID=aaaq1cZcWWLsFe5QrxGby; fanyi-ad-id=305676; ___rl__test__cookies=1650884305576'
}
resp = requests.post(url, data=data, headers=head, cookies=cookie)
data = resp.json().get("translateResult")  # reult一个列表
# result = data[0]
data = data[0]
data = data[0]
# print(data)  # 字典tgt -》key
result = data.get("tgt")
print(result)
