import ConfigParser as CP
import os

from shutil import copyfile, rmtree


def parserPath(dir):
	if len(dir) <= 1:
		dir = "ERROR"
	elif dir.find(":") is not -1:
		pass
	elif dir[0] is ".":
		currentDir = os.getcwd()
		if dir.find(".\\") is 0:
			dir = dir.replace('.\\', '')
			if dir is "":
				dir = currentDir
			else:
				dir = os.path.join(currentDir, dir)
		elif dir.find("..\\") is 0:
			count = dir.count("..\\")
			dir.replace('/', '\\')
			currentDir.replace('/', '\\')
			folders = currentDir.split('\\')
			if len(folders) <= count:
				dir = "ERROR"
			else:
				for idx in xrange(count):
					folders.pop()
				currentDir = '\\'.join(folders)
				dir = dir.replace('..\\'* count, '')
				dir = os.path.join(currentDir, dir)
	return dir

def createDir(folder):
	if -1 != folder.rfind('.'):
		if -1 == folder.rfind('\\'):
			folder = folder[:folder.rfind('/')]
		else:
			folder = folder[:folder.rfind('\\')]
	if not os.path.exists(folder):
		if -1 == folder.rfind('\\'):
			childfolder = folder[:folder.rfind('/')]
		else:
			childfolder = folder[:folder.rfind('\\')]
		createDir(childfolder)
		print '++++++++++++++++++\n', folder
		os.mkdir(folder)

def copyFileAuto(src, dst):
	if not os.path.exists(src):
		return
	if -1 != dst.rfind('.') and (-1 != dst.rfind('\\') or -1 != dst.rfind('/')):
		createDir(dst)
	copyfile(src, dst)

def walkDir(curdir, dstdir):
	dirinfo = os.walk(curdir)
	for root, dirs, files in dirinfo:
		if root is not curdir:
			continue
		for file in files:
			if checkIgnore(file):
				continue
			filePath = os.path.join(root, file)
			dstPath = filePath.replace(curdir, dstdir)
			copyFileAuto(filePath, dstPath)
		for dir in dirs:
			if checkIgnore(dir):
				continue
			dirPath = os.path.join(root, dir)
			walkDir(dirPath, os.path.join(dstdir, dir))
			
TYPES = []
IGNORE_FILES = []
def checkIgnore(filePath):
	if filePath in IGNORE_FILES:
		return True
	if "*" in TYPES:
		return False
	if len(filePath) < 2:
		return False
	prefixIdx = filePath.rfind('.')
	
	prefix = 'DIR'
	if prefixIdx is not -1:
		prefix = filePath[prefixIdx:]
	if prefix not in TYPES:
		return True
	return False
	

def runCopy(config_file):
	global TYPES, IGNORE_FILES
	print config_file
	if config_file.rfind('.ini') == -1:
		return
	print config_file
	cfg = CP.ConfigParser()
	cfg.readfp(open(config_file))
	SRC_DIR = os.getcwd()
	if cfg.has_option("SRC", "dir"):
		srcDir = cfg.get("SRC", "dir")
		if srcDir is not "" and srcDir is not None:
			SRC_DIR = srcDir;
	SRC_DIR = parserPath(SRC_DIR)
	DST_DIR = cfg.get("Target", "dir")
	DST_DIR = parserPath(DST_DIR)
	typesStr = cfg.get("SRC", "types")
	TYPES = typesStr.split('|')
	ignoreStr = cfg.get("SRC", "ignore")
	IGNORE_FILES = ignoreStr.split('|')
	OVERRIDE = cfg.get("Target", "override")
	REMOVE_ALL = cfg.get("Target", "removeAll")
	if REMOVE_ALL and os.path.exists(DST_DIR):
		try:
			rmtree(DST_DIR)
		except:
			print "IOError"
	if DST_DIR is not "ERROR":
		walkDir(SRC_DIR, DST_DIR)
		
		
		
if __name__ == "__main__":
	print '*' * 60
	print "Copy Desc"
	print "copy.py read and run copy.ini"
	print "copy.py xxx.ini			Run with config xxx.ini "
	print "copy.py dir .\\configDir 	Run with all config of dir configDir"
	print "copy.py dir .\\configDir R	Run with all config of dir configDir and recursion"
	print '*' * 60
	import sys
	config_file = 'copy.ini'
	if len(sys.argv) > 2 and sys.argv[1] == 'dir':
		dir = parserPath(sys.argv[2])
		if os.path.isdir(dir):
			loopRange = os.walk(dir)
			recursion = False
			if len(sys.argv) > 3 and (sys.argv[3] == 'r' or sys.argv[3] == 'R'): 
				recursion = True
			for _root, _dirs, _files in loopRange:
				if not recursion and _root != dir:
					continue
				for fileName in _files:
					runCopy(os.path.join(_root, fileName))
	else:
		if len(sys.argv) > 1:
			config_file = sys.argv[1]
		runCopy(config_file)
	