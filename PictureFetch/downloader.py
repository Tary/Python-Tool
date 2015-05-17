# -*- coding:utf-8 -*-  

import os, urllib2, urllib


def download_img_bat(url_root, sub_urls, save_dir):
	if not os.path.isdir(save_dir):
		print("invalid save_path: %s" % save_dir)
		return
	save_dir = save_dir.replace('\\', '/')
	if save_dir[-1] is '/' and save_dir[-2] is not ':':
		save_dir = save_dir[:-1]
	if type(sub_urls) is list:
		for url in sub_urls:
			name = url
			if -1 is not url.rfind('/'):
				name = url[url.rfind('/')+1:]
			download_img('/'.join([url_root, url]), os.path.join(save_dir, name))
	elif type(sub_urls) is dict:
		for name in sub_urls:
			_url = sub_urls[name]
			if name.rfind('.') is -1 and _url.rfind('.') is not -1:
				name += _url[_url.rfind('.'):]
			dl_url = '/'.join([url_root, _url])
			download_img(dl_url, os.path.join(save_dir, name))

#save_path  c:\\d.png
def download_img(url, save_path):
	#print url, save_path
	urllib.urlretrieve(url, save_path)
