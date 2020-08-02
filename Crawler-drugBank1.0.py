# -*- coding: utf-8 -*-
"""
@Time ： 2020/7/20 23:39
@Auth ： LuZheng
@E-mail: 466824111@qq.com
@IDE ：PyCharm
"""
import requests        #导入requests包
from lxml import etree
from bs4 import BeautifulSoup

#url = 'https://pubchem.ncbi.nlm.nih.gov/#query=BRD-K49328571'
#url = 'https://pubchem.ncbi.nlm.nih.gov/compound/3062316#section=CAS'
url='https://www.drugbank.ca/drugs/DB00598'
strhtml = requests.get(url)
# etree_html = etree.HTML(strhtml)
#print(strhtml.text)
bs=BeautifulSoup(strhtml.text,'lxml')
# print(bs)
print(bs.select('#targets'))
# etree_html = etree.HTML(strhtml)  # 自动补全网页格式，并解析为xpath能解析的命令
# result = etree.tostring(etree_html)  # 查看自动补全后的网页
# print(etree_html)
# print(result)
#Get方式获取网页数据
# print(strhtml.text)