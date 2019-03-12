import requests
import xml
# from lxml import etree

url = 'https://movie.douban.com/subject/1292052/'

r = requests.get(url).text

s = etree.HTML(r)
movie = s.xpath('//*[@id="content"]/h1/span[1]/text()')
director = s.xpath('//*[@id="info"]/span[1]/span[2]/a/text()')
actor = s.xpath('//*[@id="info"]/span[3]/span[2]/a/text()')
time = s.xpath('//*[@id="info"]/span[13]/text()')

print('电影名称:', movie)
print('导演:', director)
print('主演:', actor)
print('片长:', time)