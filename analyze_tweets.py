import json
import nltk
import re 
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
set(stopwords.words('english'))

tweets = []
stop_words=set(stopwords.words('english'))
for line in open('tweets.json', 'r'):
	no_links = re.sub(r'http\S+', '', line)
	no_unicode = re.sub(r"\\[a-z][a-z]?[0-9]+", '', no_links)
	no_special_characters = re.sub('[^A-Za-z ]+', '', no_unicode)
	words=no_special_characters.split('RT');
	for r in words:
		if not r in stop_words:
			r=r.strip()
			appendFile=open('filtered_tweets.txt','a')
			appendFile.write(" "+r)
			appendFile.close()
			
