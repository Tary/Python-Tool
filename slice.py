

def loadconfig(path2file):
	import xml.etree.ElementTree as ET
	tree = ET.ElementTree(file=path2file)
	root = tree.getroot()
	bitmapdata = root.find("BitmapData")
	width, height = 0, 0
	if bitmapdata is not None:
		width, height = bitmapdata.attrib.values()
	
	items = []
	for node in root.getchildren():
		if "SubTexture" == node.tag:
			attrib = node.attrib
			item = [attrib['name'], attrib['x'], attrib['y'], attrib['width'], attrib['height']]
			items.append(item)
			
	return items, width, height

import os
	
def sliceimg(imgname, configs, dir):
	import Image
	img = Image.open(imgname)
	if img is None:
		return	
	for item in configs:
		name, x, y, wid, hei = item
		x, y, wid, hei = int(x), int(y), int(wid), int(hei)
		img.crop((x, y, x+wid, y+hei)).save(os.path.join(dir, str.join('', [name,'.png'])))

		
	


def slicebyconfig(namewithprefix):
	dir = os.getcwd()
	if -1 != namewithprefix.find('.'):
		name = namewithprefix[:namewithprefix.find('.')]
	else:
		name = namewithprefix
	configitems, width, height = loadconfig(name + ".xml")	
	targetdir = os.path.join(dir, name)
	if not os.path.isdir(targetdir):
		os.makedirs(targetdir)
	sliceimg(name + '.png', configitems, targetdir)


slicebyconfig('TextureResource_0')
slicebyconfig('TextureResource_1')
slicebyconfig('TextureResource_2')
slicebyconfig('shopSeed_0')
slicebyconfig('shopSeed_1')
slicebyconfig('shopSeed_2')

	
