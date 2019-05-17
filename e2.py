#爬取Discuz帖子标题
from bs4 import BeautifulSoup
import requests
for i in range(200):
        #使用for循环更改url中的tid
    html = requests.get('http://114.112.74.138/forum.php?mod=viewthread&tid='+str(i))
    #创建BeautifulSoup对象
    soup = BeautifulSoup(html.text,"html.parser")
    #第一中爬取标题方法
    title1 = soup.title.string
        #第二种爬取标题的方法
    title2=soup.find(attrs={"id":"thread_subject"})
    print(title1)
    print(title2)