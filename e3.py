#爬取Discuz帖子内容及连接
from bs4 import BeautifulSoup
import requests
for i in range(200):
    html = requests.get('http://114.112.74.138/forum.php?mod=viewthread&tid='+str(i))
    soup = BeautifulSoup(html.text,"html.parser")
    url = soup.link['href']
    content = soup.find(attrs={"class":"t_fsz"})
    print(url)
    print(content)