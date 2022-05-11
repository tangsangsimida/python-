from concurrent.futures import ThreadPoolExecutor
import requests

'''每日一次，只能爬4，5000张，没有vip限量了'''


def askimg():
    proxy = {
        "http": "18.140.166.66:8000"
    }
    cookie = {
        # "Cookie": "Hm_lvt_7d2469592a25c577fe82de8e71a5ae60=1650630029,1650632573,1650762170,1650771418; Hm_lpvt_7d2469592a25c577fe82de8e71a5ae60=1650771423"}
        "Cookie": "Hm_lvt_7d2469592a25c577fe82de8e71a5ae60=1651630289; Hm_lpvt_7d2469592a25c577fe82de8e71a5ae60=1651630289"}
    head = {
        "Web-Agent": "web",
        # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
        # "User-Agent": "Firefox 4.0.1 – WindowsUser-Agent:Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32",
        "Accept": "application/json",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6"
    }
    '''header中有一条参数必须要，不确定，（懒得去试了，）不然会被屏蔽请求'''
    url = "http://www.dbbqb.com/api/search/json"
    url_img = "http://image.dbbqb.com/"  # 202204241523/04ba69bd460aaf922256711e5912b2ff/DGyoE
    '''图片的数据库加上请求到的100条path就直接能拿到100张jpg'''
    param = {"size": "100"}
    resp = requests.get(url, headers=head, params=param)  # .json()  # 拿到的是一个列表，列表里面的有100条字典转载数据
    print(resp)
    '''字典的名字从0-99'''
    '''Array[100]包含了Object{}*100'''
    '''开始只能拿到一条数据--》请求头不规范，被屏蔽了'''
    path = []
    j = 1
    for i in resp:
        path.append(i.get("path"))
        imgresp = requests.get(url_img + i.get("path")).content
        title = (i.get("id"))
        with open(r"E:\doubi\duoxc\{}.gif".format(title), "wb") as f:
            f.write(imgresp)
            print("保存成功" + str(j))
            j = j + 1
            f.close()
        imgresp.close()
    resp.close()
    print("download all ~")


if __name__ == '__main__':
    # with ThreadPoolExecutor(50) as t:
    #     for i in range(100):
    #         t.submit(askimg)
    askimg()
print("all over")  # 等待线程池完之后执行
