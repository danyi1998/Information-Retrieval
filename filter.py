from nltk import word_tokenize
from nltk.stem.porter import PorterStemmer

#Tokenize the text
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
