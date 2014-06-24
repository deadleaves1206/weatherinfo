#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		CitiesCode.py		 ###
################################

#模块功能：将城市代码写入xml中
#version：1.0
#使用dom模块对xml文件进行操作
#模块导入
from xml.dom import minidom				#dom模块，用于读写xml文件
import getCitiesCode					#获取城市代码
#import codecs							#文件、字符编码

def readXML(in_path):
	'读取xml文件，返回dom树'
	dom = minidom.parse(in_path)
	return dom

def writeXML(dom, out_path):
	'将dom树写入xml文件中'
#	f = codecs.open(out_path, 'w', encoding='utf-8')
#	dom.writexml(f, addindent='    ',\
#				newl='\n', encoding='utf-8'	)
#	f.close()
	f = open(out_path, 'w')
	dom.writexml(f, addindent='    ',\
				newl='\n', encoding='utf-8'	)
	f.close()

def citiesCode():
	impl = minidom.getDOMImplementation()
	dom = impl.createDocument(None, 'CitiesCode', None)
	rootNode = dom.documentElement

	provinces = getCitiesCode.getProCode()	#获取省编号
	for pro in provinces:
		province = dom.createElement('province')
		province.setAttribute('id', pro.split('|')[0])
		province.setAttribute('name', pro.split('|')[1])
		cities = getCitiesCode.getCityCode(pro.split('|')[0])	#获取市编号
		for ci in cities:
			city = dom.createElement('city')
			city.setAttribute('id', ci.split('|')[0])
			city.setAttribute('name', ci.split('|')[1])
			areas = getCitiesCode.getAreaCode(ci.split('|')[0])
			for ar in areas:
				area = dom.createElement('area')
				area.setAttribute('id', ar.split('|')[0])
				area.setAttribute('name', ar.split('|')[1])
				city.appendChild(area)
			province.appendChild(city)
		rootNode.appendChild(province)

	writeXML(dom, '../xml/CitiesCode.xml')

#测试代码，用于测试该模块所有功能是否正常
if __name__ == '__main__':
	citiesCode()

