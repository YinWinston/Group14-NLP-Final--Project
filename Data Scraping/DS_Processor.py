import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
import re
from time import sleep
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from num2words import num2words
import csv

closed_class_stop_words = ['a','the','an','and','or','but','about','above','after','along','amid','among', \
                           'as','at','by','for','from','in','into','like','minus','near','of','off','on', \
                           'onto','out','over','past','per','plus','since','till','to','under','until','up', \
                           'via','vs','with','that','can','cannot','could','may','might','must', \
                           'need','ought','shall','should','will','would','have','had','has','having','be', \
                           'is','am','are','was','were','being','been','get','gets','got','gotten', \
                           'getting','seem','seeming','seems','seemed', \
                           'enough', 'both', 'all', 'your' 'those', 'this', 'these', \
                           'their', 'the', 'that', 'some', 'our', 'no', 'neither', 'my', \
                           'its', 'his' 'her', 'every', 'either', 'each', 'any', 'another', \
                           'an', 'a', 'just', 'mere', 'such', 'merely' 'right', 'no', 'not', \
                           'only', 'sheer', 'even', 'especially', 'namely', 'as', 'more', \
                           'most', 'less' 'least', 'so', 'enough', 'too', 'pretty', 'quite', \
                           'rather', 'somewhat', 'sufficiently' 'same', 'different', 'such', \
                           'when', 'why', 'where', 'how', 'what', 'who', 'whom', 'which', \
                           'whether', 'why', 'whose', 'if', 'anybody', 'anyone', 'anyplace', \
                           'anything', 'anytime' 'anywhere', 'everybody', 'everyday', \
                           'everyone', 'everyplace', 'everything' 'everywhere', 'whatever', \
                           'whenever', 'whereever', 'whichever', 'whoever', 'whomever' 'he', \
                           'him', 'his', 'her', 'she', 'it', 'they', 'them', 'its', 'their','theirs', \
                           'you','your','yours','me','my','mine','I','we','us','much','and/or'
                           ]
# cur_prod_listings = pd.DataFrame(product_desc_data)
files_to_parse = ["PowerAdapters_DS.csv", "StripLights_DS.csv", "LightSabers_DS.csv", "mixed_DS.csv"]
reducer = PorterStemmer()
for a in files_to_parse:
    g = open(a.replace(".csv","") + "_Processed.csv", encoding='utf-8', mode = 'w')
    with open (a, mode = 'r',encoding = 'utf-8') as file:
        cur_file = csv.reader(file)
        for line in cur_file:
            unmodified_field = ""
            # print(row[l])
            for s in line[1]:
                if s.isalpha() or s.isspace():
                    unmodified_field += s
                elif s in "1234567890":
                    unmodified_field += num2words(int(s)) + " "
            # print(unmodified_field)
            tokenized_field = word_tokenize(unmodified_field) #tokenizes word
            modified_field = [reducer.stem(w) for w in tokenized_field if w not in closed_class_stop_words] #remove stop words
            # print(unmodified_field)
            for word in modified_field:
                print(word + " ")
                g.write(word + " ")
            g.write("\n")
    g.close()
