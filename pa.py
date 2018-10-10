from bs4 import BeautifulSoup
from pc import Img
import re

url = input('请输入一个网址：')#获得网页地址
path_d = input('请输入文件保存的地址（会创建一个以网页头同名的文件夹）:')
if url == '0' :#0结束
    pass
if not re.search('^http:.*',url) :#添加协议头
    url = 'http://' + url
print('你输入的URL为：'+url)
u = re.match('http.*com/',url)#获得网页跟地址，备用
u = u.group()#获得re匹配项
print('网站的跟地址为：'+u)
i = Img(url,path_d)#创建IMG类，url用来初始化现在文件夹
ht = i.get_content(url)#获取给页面代码
all_a = i.get_a(ht)#获取该页面的所有连接
#print(all_a)
if all_a != None :#如果连接不为空
    for a in all_a :#循环获得连接对象
        print(a['href'])#显示对象的地址
        if not re.search('.*java.*|/$|#',a['href']) :#当地址不为java代码，斜杠和#号时匹配下载
                a['href'] = u + '%s' %a['href']#连接获得的主地址
                print(u)#显示连接后的地址
                info = i.get_content(a['href'])#获取页面代码
                i.get_images(info)#下载图片
    
