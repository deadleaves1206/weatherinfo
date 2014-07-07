#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		CitiesCode.py		 ###
################################

#模块功能：根据IP地址获取地理信息
#version：0.1

import socket
import urllib2
import json
import re

#获取本机IP地址(有局域网的情况下不能使用，废弃)
# def getLocalIP():
# 	localIP = socket.gethostbyname(socket.gethostname())
# 	return localIP

#获取本机外网IP地址（通过访问获取IP地址的网站）
class getMyIP():
	"""
	getMyIP：用于获取本机外网IP地址。
	获取方法：访问用于获取外网IP地址的网站
	"""
	def __init__(self):
		"""
		类的初始化
		"""
		self.myIP = None

	def visitUrl(self, apiurl):
		"""
		访问网站，获取IP地址
		"""
		opener = urllib2.urlopen(apiurl)
		if apiurl == opener.geturl():
			try:
				content = opener.read()
			except IOError:
				print "Can't get information from %s" %apiurl
				return None
			else:
				pattern = re.compile(r'\d+\.\d+\.\d+\.\d+')
				myIP = re.search(pattern, content)
				if myIP == None:
					print "Can't get IP"
					return None
				else:
					return myIP.group(0)
		else:
			print "Open the url error！"
			return None

	def getIP(self):
		"""
		尝试访问多个获取IP地址的网站，获取本机外网IP
		"""
		try:
			self.myIP = self.visitUrl("http://www.whereismyip.com")
		except:
			try:
				self.myIP = self.visitUrl("http://www.bliao.com/ip.phtml")
			except:
				try:
					self.myIP = self.visitUrl("http://www.ip138.com/ip2city.asp")
				except:
					print "Internet Error!"
					return None
		return self.myIP

		
#通过淘宝api获取地理信息
def getLocation(IP):
	apiurl = "http://ip.taobao.com/service/getIpInfo.php?ip=%s" %IP
	try:
		content = urllib2.urlopen(apiurl).read()
	except:
		print "Can't get the location information!"
		return None
	else:
		code = json.loads(content)['code']
		data = json.loads(content)['data']
		if code == 0:
			city = data['city']
			if city != None:
				return city[0:2]
			else:
				return None

if __name__ == '__main__':
	IP = getMyIP().getIP()
	if IP == None:
		print "Can't get the IP"
	else:
		cityname = getLocation(IP)
		print cityname