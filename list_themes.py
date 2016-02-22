import json
import nltk
import re
import pymongo
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
from nltk.tokenize import wordpunct_tokenize
from collections import Counter

client = pymongo.MongoClient('goto.reproducible.work')
db = client['vk_bukin']
users = db.['users']

users.find({'id' : '1'})

stemmer = RussianStemmer()
people_goal = db['users'].find({'sex': 1}).limit(50000)


def killshit(text):
    temp = text.split(' ')
    ans = ""
    for i in range (len(temp)):
        if len(temp[i]) > 4 and len(temp[i]) < 21:
            ans += temp[i]
            ans += ' '
    return ans

delete = re.compile(u'\W+?', re.UNICODE)

def get_bag_of_the_words(text):
    tokens = tokenizer.tokenize(text)
    tokens_stemmed = [stemmer.stem(token) for token in tokens]
    return Counter(tokens_stemmed)

d = {}

for p in people_goal:
        t = p['status']
        t += ' '
        if 'about' in p.keys():
            t += p['about']
        t += ' '
        if 'interests' in p.keys():
            t += p['interests']
        if 'books' in p.keys():
            t += p['books']
        t += ' '
        if 'tv' in p.keys():
            t += p['tv']
        t += ' '
        if 'movies' in p.keys():
            t += p['movies']
        t += ' '
        if 'games' in p.keys():
            t += p['games']
        t += ' '
        if 'quotes' in p.keys():
            t += p['quotes']
        t += ' '

        t = delete.sub(' ', t).strip()

        freq = get_bag_of_the_words(killshit(t))

        for token, freq in freq.most_common()[:1]:
            #token = token.encode('ascii')
            if token in d.keys():
                d[token] += int(freq)
            else:
                d[token] = int(freq)
print max(d, key = d.get)

for w in sorted(d, key = d.get, reverse = True)[:40]:
    print w, d[w]