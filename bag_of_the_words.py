import json
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import RussianStemmer
from nltk.tokenize import wordpunct_tokenize
from collections import Counter

stemmer = RussianStemmer()
tokenizer = RegexpTokenizer(ur"[^\\ ,\\.\!\\?\\:\\)\(\\-\\0\\1\\\2\\3\\4\\5\\6\\7\\8\\9\\_\\?\\-\\?\\?]+")
people_goal = db['users'].find({'first_name': 'Ваня'}).limit(50)


def killshit(text):
    temp = text.split(' ')
    ans = ""
    for i in range (len(temp)):
        if len(temp[i]) > 3 and len(temp[i]) < 21:
            ans += temp[i]
            ans += ' '
    return ans
            

def get_bag_of_the_words(text):
    tokens = tokenizer.tokenize(text)
    tokens_stemmed = [stemmer.stem(token) for token in tokens]
    return Counter(tokens_stemmed)
for p in people_goal:
        #print (token)
        t = p['status']
        t += ' '
        if 'about' in p:
            t += p['about']
        t += ' '
        if 'interests' in p:
            t += p['interests']
        if 'books' in p:
            t += p['books']
        t += ' '
        if 'tv' in p:
            t += p['tv']
        t += ' '
        if 'movies' in p:
            t += p['movies']
        t += ' '
        if 'games' in p:
            t += p['games']
        t += ' '
        if 'quotes' in p:
            t += p['quotes']
        t += ' '
        freq = get_bag_of_the_words(killshit(t))
        for token, freq in freq.most_common():
            print (token + "\t" + str(freq))
        #print (stemmer.stem(token))
        print '------------'

#print json.dumps(user[1345], indent=4, encoding='utf8', ensure_ascii=False)[:]