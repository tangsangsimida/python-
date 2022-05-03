import requests
import os
# texttext
head = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50",
    "Web-Agent": "web"
}
url_img = "http://image.dbbqb.com/"
url_search = "http://www.dbbqb.com/api/search/json"
nock = 1
while nock:
    search_input = input("请输入要下载的表情包类型：")  # search_input 文件夹的名字，利用search_input创建一个文件夹
    if os.path.exists(r"E:\doubi\{}".format(search_input)):
        print("已经下载了该类型的表情包了，请重新输入类型：")
        nock = 1
    else:
        num = input("请输入要下载的数量：")
        # 直接再else中创建文件夹吧：
        os.makedirs(r"E:\doubi\{}".format(search_input))
        nock = 0
begin = 0
j = 0
for begin in range(0, 10000, 100):  # 应该还可以优化，emmm，循环可以再智能一点
    param = {
        "w": "{}".format(search_input),
        "start": "{}".format(str(begin))
    }
    resp = requests.get(url_search, headers=head, params=param)
    data = resp.json()
    for data_url in data:
        info = data_url.get("path")
        result_url = url_img + info
        if j >= int(num):
            exit()
        j += 1
        img_resp = requests.get(result_url, head).content
        '''访问图片url直接返回图片'''
        title = data_url.get("id")
        # 用imgID作为文件名防止重复
        with open(r"E:\doubi\{}\{}.gif".format(search_input, title), "wb") as f:
            f.write(img_resp)
            print("保存成功   ID=  {},  数量{}".format(str(title), str(j)))
            f.close()
if j < int(num):
    print("就这么点儿了，你爱要不要吧~~~")
resp.close()
