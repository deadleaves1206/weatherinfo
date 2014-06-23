#-*- coding: utf-8 -*-
################################
###		author:ryli			 ###
###		date:2014-06-16		 ###
###		weatherinfo			 ###
###		CitiesCode.py		 ###
################################

#get cities' code from China weather


#import modules
from xml.dom import minidom

#read a dom tree form the xml named CitiesCode.xml
def read_XML(xmlurl):
	try:
		dom = minidom.parse(xmlurl)
	except IOError:
		print "Can't open the xml file!"
		return None
	else:
		print "Read the dom from the xml file successful!"
		return dom

#write the dom tree into the xml named CitiesCode.xml
def write_XML(dom, xmlurl):
	try:
		f = open(xmlurl, 'w')
	except IOError:
		print "Can't open the xml file!"
		return None
	else:
		print "Open the xml file successful!"
		try:
			dom.writexml(f, addindent='    ', newl='\n', encoding='utf-8')
		except IOError:
			print "Can't write the information into the xml file!"
			f.close()
			return None
		else:
			print "Write the information into the xml file successful!"
			f.close()

#search the node from dom tree by tag name
def search_childNode(parentNode, childName):
	childNodes=parentNode.getElementsByTagName(childName)
	if childNodes==None:
		print "There is no childnode of %s" %parentNode
		raise NameError
	else:
		return childNodes

#add a childnode
def add_childNode(dom, parentNode, childNode):
	node = dom.createElement(childNode['type'])
	node.setAttribute('id', childNode['id'])
	node.setAttribute('name', childNode['name'])
	parentNode.appendChild(node)

#delete a childnode
def del_childNode(dom, parentNode, childNode):
	node = 