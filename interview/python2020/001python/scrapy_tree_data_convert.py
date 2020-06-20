# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 16:00:51 2020

@author: Charlot
"""

industry_list = [
  {
     "parent_ind" : "女装",
     "name" : "连衣裙"
  },
  {
     "name": "女装"
  },
  {
     "parent_ind" : "女装",
     "name" : "半身裙"
  },
  {
     "parent_ind" : "女装",
     "name" : "A字裙"
  },
  {
     "name": "数码"
  },
  {
    "parent_ind" : "数码",
     "name": "电脑配件"
  },
  {
    "parent_ind" : "电脑配件",
     "name": "内存"
  },
]

from collections import defaultdict

"""
爬虫数据格式转换，从字典列表转换为树形字典树
TODO 1. 处理数据有parent键值，但是在整个数据中找不到父级的情况，即树断裂情况
TODO 2. 处理重复键情况
"""
def convert_format(data):
    # 找到根节点
    # 列表推导式，筛选，也可以使用filter来筛选
    # 使用迭代器，如果数据量大，减少内存使用，但是效率会稍微差一点点
    roots = ( item for item in data if 'parent_ind' not in item)
    # 使用defaultdict, 方便初始键不存在数据
    treedata=defaultdict(dict)
    for root in roots:
        treedata[root['name']]=find_children(data,root['name'])
        
    return dict(treedata)

"""
通过递归的方式建立root子孙树结构
"""        
def find_children(data,parent_ind):
    children=defaultdict(dict)
    for item in ( i for i in data if 'parent_ind' in i and i['parent_ind']==parent_ind):
        children[item['name']]=find_children(data, item['name'])
    return dict(children)    
        
    
if __name__=='__main__':
   # 调用方法，并显示数据
   treedata =  convert_format(industry_list)    
   print(dict(treedata))