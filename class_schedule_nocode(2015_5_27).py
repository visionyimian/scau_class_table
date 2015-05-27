# --*-- coding:utf-8 --*-
#---------------------------------------
#   程序：华农大学爬虫
#   版本：测试版2.0
#   作者：back-lighting
#   日期：2015-05-28
#   语言：Python 2.7
#   功能：抓取课表
#---------------------------------------
import os
import urllib  
import urllib2
import cookielib
from PIL import Image
import webbrowser

from bs4 import BeautifulSoup as bs



class personal_schedule:
	def __init__(self):
		self.loginUrl = 'http://202.116.160.170/default_ysdx.aspx'
		#self.CodeUrl = 'http://202.116.160.170/CheckCode.aspx?'
		self.cookiejar = cookielib.CookieJar()
		self.cookieSupport = urllib2.HTTPCookieProcessor(self.cookiejar)
		self.opener = urllib2.build_opener(self.cookieSupport)
		self.installer = urllib2.install_opener(self.opener)
	"""
	def code(self):
		img_req = urllib2.Request(self.CodeUrl)
		img_response = self.opener.open(img_req)
		out = open('code','wb')
		out.write(img_response.read())
		out.flush()
		out.close()
		print 'get code success'
		im = Image.open('code')
		#print im.format, im.size, im.mode
		im.show()
	"""
	def pc_login(self,xh='',xm='',xqd='',xnd=''):
		soup = bs(urllib.urlopen(self.loginUrl).read(),from_encoding='utf-8')
		self.viewstate = soup.find("input", {"name":"__VIEWSTATE"})['value']
		self.viewstategenerator = soup.find("input", {"name":"__VIEWSTATEGENERATOR"})['value']
		self.headers  = {  'Referer': 'http://202.116.160.170/default_ysdx.aspx','User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
		self.postdata = urllib.urlencode({  
			'__VIEWSTATE':self.viewstate,
			'__VIEWSTATEGENERATOR':self.viewstategenerator,
			'TextBox1':xh,
			'TextBox2':xm,
			#'txtSecretCode':img_code,  #验证码
			'RadioButtonList1':'Ñ§Éú',
			'Button1':'  µÇÂ¼  '
			})
		req = urllib2.Request(
			url = self.loginUrl,
			data = self.postdata,
			headers = self.headers
			)
		res = urllib2.urlopen(req)
		html = res.read()
		
		html = unicode(html, "gb2312").encode("utf8")
		print req
		print html
		res.close()

	def p_c(self,xh='',xm='',xqd='',xnd='',VIEWSTATE=''):
		self.headers2 = {
			'Referer': 'http://202.116.160.170/xs_main.aspx?xh='+xh,
			'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
		}
		self.postdata2 = urllib.urlencode({
			'__EVENTTARGET':xnd,
			'__EVENTARGUMENT':'',
			'__VIEWSTATE':VIEWSTATE,
			'__VIEWSTATEGENERATOR':'55530A43',
			'xnd':xnd,
			'xqd':xqd
			})

		req2 = urllib2.Request(
			url = 'http://202.116.160.170/xskbcx.aspx?xh='+xh+'&xm='+xm+'&gnmkdm=N121603',
			data = self.postdata2,
			headers = self.headers2
			)
		result = urllib2.urlopen(req2)
		html = result.read()
		result.close()
		html = unicode(html, "gb2312").encode("utf8")
		soup = bs(html, from_encoding='utf-8')
		table = soup.find("table",{"id":"Table1"})
		table = str(table)
		
		fo = open('personalclass.html','wb+')
		fo.write('<meta charset="utf-8"><meta http-equiv="Content-Type" content="text/html; charset=utf-8" />')
		fo.write(table)
		fo.close()
		webbrowser.open('guess.html')

if __name__ == '__main__':
	person = personal_schedule()
	"""
	xh = raw_input('please enter your student ID: ')
	xm = raw_input('please enter your password: ')
	xnd = raw_input('please enter your xue nian(xxxx-xxxx,such like 2014-2015): ')
	xqd = raw_input('please enter your xue qi(1 ,2 or 3):')
	"""
	import who

	if who.xnd == '2014-2015' and who.xqd == '2':
		VIEWSTATE = 'dDwzOTI4ODU2MjU7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwyPjtpPDQ+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDI0PjtpPDI2PjtpPDI4PjtpPDMwPjtpPDMyPjtpPDM0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4bjt4bjs+Pjs+O3Q8aTwzPjtAPDIwMTQtMjAxNTsyMDEzLTIwMTQ7MjAxMi0yMDEzOz47QDwyMDE0LTIwMTU7MjAxMy0yMDE0OzIwMTItMjAxMzs+PjtsPGk8MD47Pj47Oz47dDx0PDs7bDxpPDA+Oz4+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m5Y+377yaMjAxMjMwMjMwNDI4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrpg5HlrZDlgaU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8mui1hOa6kOeOr+Wig+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77ya546v5aKD5bel56iLOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJoxMueOr+Wig+W3peeoizQ7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDI+O2k8Mj47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8546v5aKD5bel56iL57u85ZCI5a6e5LmgMjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85Luy5rW35rabOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE2LTE3Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuI3mjpLor747Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8546v5aKD5bel56iL57u85ZCI5a6e5LmgMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86buE6I2jOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDE1LTE2Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuI3mjpLor747Pj47Pjs7Pjs+Pjs+Pjs+Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwwPjtpPDA+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47Oz47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8Mz47aTwzPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+O2w8aTwwPjs+O2w8dDw7bDxpPDE+O2k8Mj47aTwzPjs+O2w8dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNC0yMDE1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlvaLlir/kuI7mlL/nrZbihaI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOS4veWGsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MC41Oz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNC0yMDE1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwxOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznjq/looPlt6XnqIvnu7zlkIjlrp7kuaAyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzku7Lmtbfmtps7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDIuMDs+Pjs+Ozs+Oz4+O3Q8O2w8aTwwPjtpPDE+O2k8Mj47aTwzPjtpPDQ+Oz47bDx0PHA8cDxsPFRleHQ7PjtsPDIwMTQtMjAxNTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8546v5aKD5bel56iL57u85ZCI5a6e5LmgMTs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w86buE6I2jOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjs+Pjs+Pjs+Pjs+Pjs+Pjs+ZCPIoUqBUl3xdrGYI49A9XyE9LE='
	else:
		VIEWSTATE = 'dDwzOTI4ODU2MjU7dDw7bDxpPDE+Oz47bDx0PDtsPGk8MT47aTwyPjtpPDQ+O2k8Nz47aTw5PjtpPDExPjtpPDEzPjtpPDE1PjtpPDI0PjtpPDI2PjtpPDI4PjtpPDMwPjtpPDMyPjtpPDM0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDxcZTs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4bjt4bjs+Pjs+O3Q8aTwzPjtAPDIwMTQtMjAxNTsyMDEzLTIwMTQ7MjAxMi0yMDEzOz47QDwyMDE0LTIwMTU7MjAxMy0yMDE0OzIwMTItMjAxMzs+PjtsPGk8MD47Pj47Oz47dDx0PDs7bDxpPDE+Oz4+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85a2m5Y+377yaMjAxMjMwMjMwNDI4Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzlp5PlkI3vvJrpg5HlrZDlgaU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOWtpumZou+8mui1hOa6kOeOr+Wig+WtpumZojs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85LiT5Lia77ya546v5aKD5bel56iLOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzooYzmlL/nj63vvJoxMueOr+Wig+W3peeoizQ7Pj47Pjs7Pjt0PDtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxwPGw8VmlzaWJsZTs+O2w8bzxmPjs+PjtsPGk8MT47PjtsPHQ8QDA8Ozs7Ozs7Ozs7Oz47Oz47Pj47dDxAMDxwPHA8bDxQYWdlQ291bnQ7XyFJdGVtQ291bnQ7XyFEYXRhU291cmNlSXRlbUNvdW50O0RhdGFLZXlzOz47bDxpPDE+O2k8MD47aTwwPjtsPD47Pj47Pjs7Ozs7Ozs7Ozs+Ozs+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDI+O2k8Mj47bDw+Oz4+Oz47Ozs7Ozs7Ozs7PjtsPGk8MD47PjtsPHQ8O2w8aTwxPjtpPDI+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8546v5aKD5bel56iL57u85ZCI5a6e5LmgMzs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w85p6X5LqR55C0Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyLjA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDEyLTEzOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwmbmJzcFw7Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzkuI3mjpLor747Pj47Pjs7Pjs+Pjt0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0PjtpPDU+O2k8Nj47PjtsPHQ8cDxwPGw8VGV4dDs+O2w85Yib5paw5Yib5Lia5a6e6Le1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzpmYjkuL3lhrA7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDMuMDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8MDEtMTY7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPCZuYnNwXDs7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOS4jeaOkuivvjs+Pjs+Ozs+Oz4+Oz4+Oz4+O3Q8QDA8cDxwPGw8UGFnZUNvdW50O18hSXRlbUNvdW50O18hRGF0YVNvdXJjZUl0ZW1Db3VudDtEYXRhS2V5czs+O2w8aTwxPjtpPDA+O2k8MD47bDw+Oz4+Oz47Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPHA8cDxsPFBhZ2VDb3VudDtfIUl0ZW1Db3VudDtfIURhdGFTb3VyY2VJdGVtQ291bnQ7RGF0YUtleXM7PjtsPGk8MT47aTwzPjtpPDM+O2w8Pjs+Pjs+Ozs7Ozs7Ozs7Oz47bDxpPDA+Oz47bDx0PDtsPGk8MT47aTwyPjtpPDM+Oz47bDx0PDtsPGk8MD47aTwxPjtpPDI+O2k8Mz47aTw0Pjs+O2w8dDxwPHA8bDxUZXh0Oz47bDwyMDE0LTIwMTU7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPDI7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOeOr+Wig+W3peeoi+e7vOWQiOWunuS5oDM7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOael+S6keeQtDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi4wOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNC0yMDE1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDzliJvmlrDliJvkuJrlrp7ot7U7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOmZiOS4veWGsDs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8My4wOz4+Oz47Oz47Pj47dDw7bDxpPDA+O2k8MT47aTwyPjtpPDM+O2k8ND47PjtsPHQ8cDxwPGw8VGV4dDs+O2w8MjAxNC0yMDE1Oz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDwyOz4+Oz47Oz47dDxwPHA8bDxUZXh0Oz47bDznjq/looPlt6XnqIvnu7zlkIjlrp7pqow7Pj47Pjs7Pjt0PHA8cDxsPFRleHQ7PjtsPOm7hOafseWdmjs+Pjs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8Mi4wOz4+Oz47Oz47Pj47Pj47Pj47Pj47Pj47PlbPRrg9GYiFfcd7rDeSB3BFNkY5'

	#person.code()
	#img_code = raw_input('please input code: ')
	#print 'your code is %s'%img_code
	person.pc_login(xh=who.xh,xm=who.xm,xqd=who.xqd,xnd=who.xnd)
	person.p_c(xh=who.xh,xm=who.xm,xqd=who.xqd,xnd=who.xnd,VIEWSTATE=VIEWSTATE)




