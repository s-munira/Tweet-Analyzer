
"""
Created on Sat Nov  2 20:26:35 2019

@author: sirajummunira
"""

from wordcloud import WordCloud
from collections import Counter

wc = WordCloud()

counts_all = Counter()

with open('filtered_tweets.txt', 'r') as f:
    for line in f:  
        counts_line = wc.process_text(line)
        counts_all.update(counts_line)

wc.generate_from_frequencies(counts_all)
wc.to_file('wc.png')
