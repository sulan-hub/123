#!/usr/bin/env python3
#! coding=utf-8
import json
import csv
from jsonpath import jsonpath
from typing import Dict,Tuple

def sort_xapp_func(name:str) -> None:
	# 读取文件,路径为name
	with open(name,'r') as f:
		data=json.load(f)
	# 设置输出csv表头
	head=['stat','length','url','title','tag','ip','fofa']
	list=[]
	# 输出文件路径
	path=f'./response_all.csv'
	with open(path,'a') as f:
		writer=csv.DictWriter(f,fieldnames=head)
		if not path:
			writer.writeheader()
		# 遍历每个请求数据
		for i in data:
			dict={}
			dict['url']=jsonpath(i,"$.value.url")[0]
			dict['title']=(jsonpath(i,"$.value.title") or [''])[0]
			dict['status']='->'.join(i[:3] for i in jsonpath(i,"$.value.httpFlow.exchanges[*].response.status"))
			dict['ip']=jsonpath(i,"$.value.httpFlow.exchanges[*].response.ip")[0]
			dict['tag'] = '\n'.join(i for i in (jsonpath(i, "$.value.fingerprints[*].product.name") or []) if i)
			dict['fofa']=(jsonpath(i,"$.value.fingerprints[*].extra.fofa") or [''])[0]
			dict['length']=(jsonpath(i,"$.value.httpFlow.exchanges[0].response.header.Content-Length.header[0]") or [''])[0]
			# 将数据提取添加进list
			list.append(dict)
		# 一口气将list写入csv文件中
		writer.writerows(list)

sort_xapp_func("./xapp.json")
