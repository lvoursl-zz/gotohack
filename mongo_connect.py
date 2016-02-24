import pymongo
import json
import nltk
import re
import pymongo
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
from nltk.tokenize import wordpunct_tokenize
from collections import Counter


def killshit(text):
    temp = text.split(' ')
    ans = ""
    for i in range (len(temp)):
        if len(temp[i]) > 4 and len(temp[i]) < 21:
            ans += temp[i]
            ans += ' '
    return ans

delete = re.compile(u'\W+?', re.UNICODE)
tokenizer = RegexpTokenizer(r'\w+')

def get_bag_of_the_words(text):
    tokens = tokenizer.tokenize(text)
    tokens_stemmed = [stemmer.stem(token) for token in tokens]
    return Counter(tokens_stemmed)

stemmer = RussianStemmer()
d = {}

users_ids_file = tuple(open('ScienceAndTech', 'r+'))
users_ids = [ ]

#print(users_ids_file)

for user_id in users_ids_file:
    try:
        users_ids.append(int(user_id.replace('\n', '')))
    except:
        pass

#print(users_ids)
# users_ids 

data = ""

client = pymongo.MongoClient('goto.reproducible.work')
db = client['vk_bukin']
users = db.users

data_file1 = open('last_stats_for_science_and_tech', 'w+')

for user_id in users_ids:
    p = users.find_one({'_id' : user_id})
    t = str(p['status']) 
    #t = t + ' '
    if 'about' in p.keys():
        t += p['about'] + ' '
    if 'interests' in p.keys():
        t += p['interests'] + ' ' 
    if 'books' in p.keys():
        t += p['books'] + ' '
    if 'tv' in p.keys():
        t += p['tv'] + ' '
    if 'movies' in p.keys():
        t += p['movies'] + ' '
    if 'games' in p.keys():
        t += p['games'] + ' '
    if 'quotes' in p.keys():
        t += p['quotes'] + ' '

    t = delete.sub(' ', t).strip()

    freq = get_bag_of_the_words(killshit(t))

    for token, freq in freq.most_common()[:1]:
        #token = token.encode('ascii')
        if token in d.keys():
            d[token] += int(freq)
        else:
            d[token] = int(freq)

    print(user_id)


for w in sorted(d, key = d.get, reverse = True)[:40]:
    print(w, d[w], file = data_file1)

