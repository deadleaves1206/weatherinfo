#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		WeatherInfo.py		 ###
################################

#version:1.0


import urllib2
import json
import codecs
import sys
import re
import CitiesCode
import getIPInfo

# cityname = raw_input(u"请输入所要查询地区：")
# type = sys.getfilesystemencoding()
# cityname = cityname.decode(type)
IP = getIPInfo.getMyIP().getIP()
if IP == None:
	print "Can't get the IP"
else:
	cityname = getIPInfo.getLocation(IP)
dom = CitiesCode.readXML('..\\xml\\CitiesCode.xml')
cityCode = CitiesCode.searchXML(cityname, dom)
pattern = re.compile(r'^0[0-4]')
match = pattern.match(cityCode)
if match:
	str1 = cityCode[0:2]
	str2 = cityCode[4:6]
	cityCode = str1 + str2 + '00'
	
if cityCode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/101%s.html' %cityCode)
		content = urllib2.urlopen(url).read()
		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (	result['weather'],
										result['temp2'],
										result['temp1'])
		print str_temp
	except:
		print '查询失败'
