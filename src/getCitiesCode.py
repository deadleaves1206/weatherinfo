#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		getCitiesCode.py	 ###
################################

#从中国天气网获取城市代码

import urllib2
import codecs

#获取省代码
def getProCode():
	url = 'http://m.weather.com.cn/data5/city.xml'
	try:
		content = urllib2.urlopen(url).read()
	except IOError:
		print '打开网页错误'
	else:
		provinces = content.split(',')
		if provinces == None:
			print '获取省代码失败'
			raise NameError()
		else:
			return provinces

#获取市代码
def getCityCode(proCode):
	url = 'http://m.weather.com.cn/data3/city%s.xml' %proCode
	try:
		content = urllib2.urlopen(url).read()
	except IOError:
		print '打开网页错误'
	else:
		cities = content.split(',')
		if cities == None:
			print '获取市代码失败'
			raise NameError()
		else:
			return cities

#获取地区代码
def getAreaCode(cityCode):
	url = 'http://m.weather.com.cn/data3/city%s.xml' %cityCode
	try:
		content = urllib2.urlopen(url).read()
	except IOError:
		print '打开网页错误'
	else:
		areas = content.split(',')
		if areas == None:
			print '获取市代码失败'
			raise NameError()
		else:
			return areas


if __name__ == '__main__':
	import sys
	provinces = getProCode()
	for pro in provinces[0:3]:
		type = sys.getfilesystemencoding()
		print pro.decode('utf-8').encode(type)
		cities = getCityCode(pro.split('|')[0])
		for city in cities:
			print city.decode('utf-8').encode(type)
			areas = getAreaCode(city.split('|')[0])
			for area in areas:
				print area.decode('utf-8').encode(type)