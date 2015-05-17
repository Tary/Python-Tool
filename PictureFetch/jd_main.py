# -*- coding:utf-8 -*-  

from downloader import *
from jdimage import *
import getpass
import os, sys

if __name__ == "__main__":
	serverGroup = 0
	if len(sys.argv) > 1 and sys.argv[1].isdigit():
		serverGroup = int(sys.argv[1])
	id = raw_input('Input ID(Number): ')
	str_id = str(id)
	while len(str_id) is 0 or not str_id.isdigit():
		id = raw_input('Input ID(Number): ')
		str_id = str(id)
	bs_rs = get_response(str_id)
	if bs_rs is None:
		print "ERROR"
	else:
		dns_prefetchs = parser_dns_prefetch(bs_rs)
		default = 0
		if len(dns_prefetchs) > 1:
			default = raw_input('Input Server IDX(1~%d): ' % len(dns_prefetchs))
			if default.isdigit():
				default = int(default)
			else:
				default = 1
			
		if dns_prefetchs is None:
			print "ERROR"
		else:
			images_sub = parser_urls(bs_rs)
			dl_dic = {}
			idx = 0
			for url in images_sub:
				print(url)
				dl_dic[str(idx)] = url#images_sub[url]
				idx = idx +1
			save_dir = os.path.join('C:\\Users', getpass.getuser(), 'Desktop', str_id)
			if not os.path.isdir(save_dir):
				os.makedirs(save_dir)
			download_img_bat(dns_prefetchs[default]+ '/popWaterMark', dl_dic, save_dir)#'/n%s'%serverGroup