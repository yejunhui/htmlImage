import urllib ,ssl
from urllib import request
from bs4 import BeautifulSoup
import os
import re

class Img():
	"""docstring for """
	def __init__(self,urls,path_d):
		local=path_d + '/'
		#headers = {'User-Agent':"Mozilla/5.0 (Windows NT 5.1; rv:52.0) Gecko/20100101 Firefox/52.0"
                #          }

		self.url = urls
		if self.url == '0' :
			pass
		info = self.get_content(self.url)
		he = re.sub(',*，*','',BeautifulSoup(info,'lxml').title.string)
		Path = local+he+'/'
		if not os.path.exists(Path) :
			os.mkdir(local+he+'/')
			print('创建%s成功' %he)
			print('文件将保存在%s下' %Path)
		self.he = he
		self.Path = Path
		
	def get_content(self,url):
	    """doc."""
	    context = ssl._create_unverified_context()
	    res = request.Request(url)
	    html=request.urlopen(res,context=context)
	    content=html.read()
	    content=content.decode('UTF-8')
	    html.close()
	    return content
	def get_images(self,info):
		u = re.match('http.*com/',self.url)
		u = u.group()
		soup=BeautifulSoup(info,'lxml')
		t = soup.title.string
		all_img=soup.find_all('img')
                #print(all_img)
		print('成功获取所有图片链接！')
		x=1
		for img in all_img:
			imgurl = re.sub('^/.*[jpg,png,jpeg]$',u + img['src'],img['src'])
			if re.search('.*jpg',imgurl) :
				name = self.he + '.jpg'
			if re.search('.*.jpeg',imgurl) :
				name = self.he + 'jpeg'
			if re.search('.*png',imgurl) :
				name = self.he + '.png'
			print(t)
			if re.search('^http.*',imgurl) :
				print('成功找到匹配')
				print('即将下载第%s张图片' %x+'共%s张'%len(all_img))
				print('即将下载:'+imgurl)
				imgname = re.sub(r'/','',imgurl)
				imgname = re.sub(r':','',imgname)
                                #print(imgname)
				request.urlretrieve(imgurl, self.Path+t+'%s'%x+name)
				print('下载成功！\n')
				x+=1
                        os.system('cls')

	def get_a(self,info):

		soup = BeautifulSoup(info,'lxml')
		all_a = soup.find_all('a')
		return all_a
