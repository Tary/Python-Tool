# -*- coding:utf-8 -*-  

import requests, bs4

ROOT_URL = "http://item.jd.com/%s.html"

def get_response(id):#str
	rs = requests.get(ROOT_URL%id)
	if rs.ok:
		return bs4.BeautifulSoup(rs.text)
	return None

def parser_dns_prefetch(bs):#BeautifulSoup
	all_dns = bs.find_all('link', rel = 'dns-prefetch')
	if len(all_dns) is 0:
		return None
	rs = []
	for dns_tag in all_dns:
		if not dns_tag.attrs.has_key('href'):
			continue
		rs.append('http:' + dns_tag.get('href'))
	return rs
	
def parser_urls(bs):#BeautifulSoup
	rs_spec_items = bs.find_all('div', 'spec-items')
	if len(rs_spec_items) is 0:
		return {}
	spec_items = rs_spec_items[0]
	rs_ele = spec_items.find_all('img')
	images = {}
	for ele in rs_ele:
		if ele.attrs.has_key('data-url') and ele.attrs.has_key('data-img'):
			images[ele.attrs.get('data-url')] = ele.attrs.get('data-img')
	return images
