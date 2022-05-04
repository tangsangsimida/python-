import requests
import os
'''
裹被子图片表情包

'''
baseurl = "http://image.dbbqb.com/"
baseunc = "E:\doubi\套图"


def getimg(url):
    num_data = 198  # 一次性请求的套图数量默认是8
    param = {
        "size": '{}'.format(num_data)
    }
    resp = requests.get(url, params=param).json()
    count = 0
    j = 1
    for i in range(0, num_data):
        all_img = resp[i]["details"]  # resp 是一个列表
        title = resp[i]["title"]
        if os.path.exists(r"{}\{}".format(baseunc, title)):
            print("{}存在，已经跳过".format(title))
            continue
        else:
            os.makedirs(r"{}\{}".format(baseunc, title))  # 分类创建套图文件夹
            for j in all_img:
                path = j[u"path"]
                img_content = requests.get(baseurl + path).content
                with open(r"{}\{}\{}.gif".format(baseunc, title, count), "wb") as f:
                    f.write(img_content)
                    print("success" + str(count))
                    count += 1  # 总共下载图片个数
            print("{}类型已经下载完毕".format(title))
            print("{}类型已经下载完毕".format(title))
            print("{}类型已经下载完毕".format(title))


if __name__ == '__main__':
    url = "http://www.dbbqb.com/api/group"
    getimg(url)
    os.system("pause")

