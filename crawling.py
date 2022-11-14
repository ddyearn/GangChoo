from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3) 

time.sleep(3)

driver.get("https://everytime.kr/lecture")
time.sleep(2)
                          

id_bar = driver.find_element("name", "userid")
id_bar.clear()
id_bar.send_keys('userid')
time.sleep(2)



pw_bar = driver.find_element("name", "password")
pw_bar.clear()
pw_bar.send_keys('password')

pw_bar.send_keys(Keys.RETURN)
time.sleep(3)



bs = BeautifulSoup(driver.page_source, 'html.parser')

a = 0 
while a < 1000:
    a = a + 1
    driver.execute_script("window.scrollTo(0, 100100100100100100100100);")
    




bs = BeautifulSoup(driver.page_source, 'html.parser')

lec_names = bs.select('#container > div:nth-child(4) > div > a > h3')


lec_rates = bs.select('#container > div:nth-child(4) > div > a > p.rate > span > span')

lec_reviews = bs.select('#container > div:nth-child(4) > div > a > p.text')

ProfList = [] 
LecList = [] 
StarList = [] 
ReviewList =[] 
TotalList = []

for lec_name in lec_names:

    LecName_Prof = lec_name.text.replace(' ','').split(':')
    
    if len(LecName_Prof) == 2:
        
    
        LecList.append(LecName_Prof[0])
        ProfList.append(LecName_Prof[1])
    
    else:
        LecList.append(LecName_Prof[0])
        ProfList.append('?')


for lec_rate in lec_rates:
    
    rate_width = lec_rate['style'].replace(' ', '').replace(';','').split(':')[1]
#     print(rate_width)
    
    if rate_width == '0%':
        LecStar = 0
    
    elif rate_width == '20%':
        LecStar = 1
    
    elif rate_width == '40%':
        LecStar = 2
    
    
    elif rate_width == '60%':
        LecStar = 3
        
    elif rate_width == '80%':
        LecStar = 4
        
    elif rate_width == '100%':
        LecStar = 5
        
    StarList.append(LecStar)
    
    

    
    LecReview = lec_review.text
    ReviewList.append(LecReview)
    

TempList = [] 
for i in range(0, len(ProfList)):
    
    TempList.append(ProfList[i])
    TempList.append(LecList[i])
    TempList.append(StarList[i])
    TempList.append(ReviewList[i])
    
    TempList = []
    
    TotalList.append(TempList)
    

    
TotalList.pop() 

import pandas as pd
pd.set_option('display.max_row', 500)
df = pd.DataFrame(TotalList)
df.to_csv("review.csv", mode='w')
df.columns = ['Professor', 'Lecture', 'Star', 'Review']

DicList = [] 
for pr in SetProf:
    
    d = {'교수명': pr,'평균별점':round(ProfStarMean[pr],1)}
    d['강의목록'] = str(df[df['Prof'] == pr]['Lec'].unique()).replace("'", '').replace('[', '').replace(']', '').split(' ')
    
    DicList.append(d)



#------wordcloud
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import numpy  as np
from PIL import Image
from wordcloud import ImageColorGenerator
import re
from konlpy.tag import Kkma
from konlpy.tag import Twitter
import nltk
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

t = Twitter()


wordcloud = WordCloud(font_path='./arial-unicode-ms.ttf', background_color="white", max_font_size=50).generate(text)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

tokens = t.nouns(text)
ko =  nltk.Text(tokens)
dic = dict(ko.vocab().most_common(700))

wordcloud = WordCloud(font_path='./arial-unicode-ms.ttf', background_color="white", max_font_size=1000).generate_from_frequencies(dic)
plt.figure(figsize=(12,12))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()