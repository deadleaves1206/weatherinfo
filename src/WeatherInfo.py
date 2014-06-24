#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		WeatherInfo.py		 ###
################################

#version:0.1


import urllib2
import json

cityCode = '010102'
if cityCode:
	try:
		url = ('http://www.weather.com.cn/data/cityinfo/1%s00.html' %cityCode)
		content = urllib2.urlopen(url).read()
		data = json.loads(content)
		result = data['weatherinfo']
		str_temp = ('%s\n%s ~ %s') % (	result['weather'],
										result['temp1'],
										result['temp2'])
		print str_temp
	except:
		print '查询失败'
