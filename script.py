import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import nltk
from nltk.corpus import stopwords
from nltk import sent_tokenize, word_tokenize
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from konlpy.tag import Okt
from nltk.tokenize import RegexpTokenizer
import re


df = pd.read_csv("./review.csv")

t = Okt()

sentences_tag = []
for sentence in list(df['Review']):
    morph = t.pos(sentence)
    sentences_tag.append(morph)

wordlists = []
wordlist = []
for sentence1 in sentences_tag:
    wordlist=[]
    for word, tag in sentence1:
            wordlist.append(word)
    wordlists.append(wordlist)

print(wordlists)
contents = wordlists

contents_for_vectorize = []
for content in contents:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word
    contents_for_vectorize.append(sentence)

def tfidf(t, d, D):
    tf = float(d.count(t)) / sum(d.count(w) for w in set(d))
    idf = sp.log( float(len(D))/(len([doc for doc in D if t in doc])) )
    return tf*idf

vectorizer = TfidfVectorizer(min_df=1, decode_error='ignore')
X = vectorizer.fit_transform(contents_for_vectorize)

#테스트 문장
test = ['재밌고 유익하고 교수님의 강의력이 좋은 강의']
test_tokens = [t.morphs(row) for row in test]

test_for_vectorize  = []

for content in test_tokens:
    sentence = ''
    for word in content:
        sentence = sentence + ' ' + word

    test_for_vectorize.append(sentence)
test_vec = vectorizer.transform(test_for_vectorize)

def dist_norm(v1, v2):
    v1_normalized = v1 / sp.linalg.norm(v1.toarray())
    v2_normalized = v2 / sp.linalg.norm(v2.toarray())
    
    delta = v1_normalized - v2_normalized
    
    return sp.linalg.norm(delta.toarray())

def dist_raw(v1, v2):
    delta = v1 - v2
    return sp.linalg.norm(delta.toarray())

dist = [dist_norm(each, test_vec) for each in  X]

import csv

def read_csv(filepath):
	elements = []
	with open(filepath, 'r', encoding='utf-8') as fp:
		reader = csv.reader(fp)
		for row in reader:
			element = (row[0], row[1], row[2], row[3], row[4])
			elements.append(element)
	return elements

elements = read_csv("./review.csv")
index = dist.index(min(dist))
print("Best lecture is ", elements[index + 1][1], " ", elements[index + 1] [2])
print("test -->", test)
print("best lecture review -->", elements[index + 1][4])