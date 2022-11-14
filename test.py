import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from collections import Counter
from nltk.tokenize import RegexpTokenizer
import re

df = pd.read_csv("./review.csv")

from collections import Counter


from konlpy.tag import Twitter
twitter = Twitter()


sentences_tag = []
for sentence in list(df['Review']):
    morph = twitter.pos(sentence)
    sentences_tag.append(morph)

#명사, 형용사인 품사만 선별해 리스트에 담기
noun_adj_list = []
for sentence1 in sentences_tag:
    for word, tag in sentence1:
        if tag in ['Noun','Adjective']:
            noun_adj_list.append(word)

print(noun_adj_list)