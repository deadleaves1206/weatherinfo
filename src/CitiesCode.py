#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		CitiesCode.py		 ###
################################

#模块功能：将城市代码写入xml中
#version：1.0
#将原本使用的dom模块改为ElementTree模块
#dom模块需要将dom树存入内存中，比较消耗内存，效率比较低
#ElementTree是一种更友好的API，可以提供“在空中”的方式处理xml，内存占用较小，效率较高
#注：ElementTree对于恶意数据结构数据不能较好的处理

#模块导入
