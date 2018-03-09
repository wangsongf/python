import requests as req 
import re 
  
def getHTMLText(url): 
 try: 
    r = req.get(url, timeout=30) 
    r.raise_for_status() 
    r.encoding = r.apparent_encoding 
    return r.text 
 except: 
    return "" 
  
def parasePage(ilt, html): 
 try: 
    plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html) 
    tlt = re.findall(r'\"raw_title\"\:\".*?\"', html) 
    for i in range(len(plt)): 
        price = eval(plt[i].split(':')[1]) 
        title = eval(tlt[i].split(':')[1]) 
        ilt.append([price, title]) 
 except: 
    print("") 
  
  
def printGoodsList(ilt): 
 tplt = "{:4}\t{:8}\t{:16}"
 print(tplt.format("序列号", "价格", "商品名称")) 
 count = 0
 for j in ilt: 
    count = count + 1
    print(tplt.format(count, j[0], j[1])) 
  
def main(): 
 goods = "python爬虫"
 depth = 3
 start_url = 'https://s.taobao.com/search?q=' + goods 
 infoList = [] 
 for i in range(depth): 
     try: 
         url = start_url + '&s=' + str(44*i) 
         html = getHTMLText(url) 
         parasePage(infoList, html) 
     except: 
         continue
 printGoodsList(infoList) 
  
main() 