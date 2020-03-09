import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk import word_tokenize
import string


class lemmatization(object):
    def __init__(self):
        self.lmtzr = WordNetLemmatizer()
        self.stop_words = set(stopwords.words("english"))

    def removeStopWords(self, words):
        line = []
        for w in words:
            if w not in self.stop_words:
                line.append(w)
        return line

    def getBiwords(self, words):
        bigrams_val = nltk.bigrams(words)
        biwords = []
        for word in bigrams_val:
            biwords.append(word)
        return biwords

    def lemmatizeWord(self, lst):
        lemmatized_list = []
        for item in lst:
            lemmatized_list.append(self.lmtzr.lemmatize(item))
        return lemmatized_list
    
    def tokenize(text):

        #Create Stemmer
        stemmer = PorterStemmer()

        #Remove irrelevant character
        text = re.sub(r"http\S+", '', text)
        text = re.sub(r"[^a-zA-Z]", ' ', text)

        #Tokenization
        tokens = word_tokenize(text)
        tokens = [i for i in tokens if i not in string.punctuation]

        #Stemming
        stems = stem_tokens(tokens, stemmer)
        return stems

    #Stemming Function
    def stem_tokens(t,s):
        stemmed=[]
        for item in t:
            stemmed.append(s.stem(item))
        return stemmed

