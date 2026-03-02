import re

import nltk
import spacy
from pprint import pprint
from unidecode import unidecode
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

f = open('Bible.txt', 'r')
#corpus = f.read()
#print(corpus[:1000])

lines = f.readlines()
# for line in lines:
#     print(unidecode(line))

text = "".join(lines[0:10])
#text = "".join(lines)

word_tokenizer = WordPunctTokenizer()
x = unidecode(lines[0])
tokens = list(x)
print(x)
print(tokens)
print(word_tokenizer.tokenize(x))


sentence_tokenizer = PunktSentenceTokenizer()
sentence_tokens = sentence_tokenizer.tokenize(text)
print(sentence_tokens)

#spacy.cli.download('en_core_web_sm')
# pipe = spacy.load('en_core_web_sm')
# doc = pipe(x)
# for token in doc:
#     print(token)
#
# for sent in doc.sents:
#     print(sent)
#nltk.download("stopwords")
sw = stopwords.words('english')
print(sw)
tokens = word_tokenizer.tokenize(text)
filtered_text = list(filter(
    lambda token: token not in sw,
    tokens
))
pprint(" ".join(filtered_text))

#nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()
word = lemmatizer.lemmatize("ate", pos="v")
print(word)
f.close()
