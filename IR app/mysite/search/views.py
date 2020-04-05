import nltk
from django.shortcuts import render, redirect 
import requests 
from nltk.corpus import stopwords 
import string
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize 
import time 


# home page 
def home(request):  
    # get user's query input
    query = request.POST.get("query_search") 
    start_time = time.time() 

    # get list of stopwords and punctuation 
    stoplist = stopwords.words("english") + list(string.punctuation) 
    # get lemmatizer
    lemma = WordNetLemmatizer() 

    results_list = [] 
    hard_list = []
    soft_list = []
    positive_list = []
    negative_list = []
    neutral_list = []

    # check if not empty 
    if type(query)==str:
        # language parsing on query 
        query = " ".join(lemma.lemmatize(word.lower()) for word in word_tokenize(query) if word not in stoplist and not word.isdigit())  

        # form solr query 
        # this is to make sure that solr searches on every field
        query = "author:" + query + " OR " + "url:" + query + " OR " + "processed_title:" + query 
        # make request 
        response = requests.get('http://localhost:8983/solr/irproject/select?q=' + query) 
        time_taken = time.time() - start_time 
        print(time_taken) 
        # parse response 
        response = response.json()  
        response = response["response"]["docs"]

        # get needed 
        for i in range(len(response)):
            results_list.append(response[i]) 

        for i in range(len(results_list)):
            # get hard news
            if results_list[i]["news_category"][0] == "hard":
                hard_list.append(results_list[i])
            # get soft news 
            else: 
                soft_list.append(results_list[i])

        for i in range(len(results_list)):
            # get positive sentiment
            if results_list[i]["sentiment"][0] == "positive":
                positive_list.append(results_list[i]) 
            # get neutral sentiment
            elif results_list[i]["sentiment"][0] == "neutral":
                neutral_list.append(results_list[i]) 
            # get negative sentiment
            else: 
                negative_list.append(results_list[i]) 
         
    return render(request=request, template_name="search/home.html", context={"all_results": results_list, "hard": hard_list, "soft": soft_list, "positive": positive_list, "neutral": neutral_list, "negative": negative_list})    



# results page 
def results(request):
    return render(request, "search/results.html") 
