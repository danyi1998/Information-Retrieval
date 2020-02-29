from django.shortcuts import render
import requests 

def home(request):
    query = request.POST.get("query_search") 
    if type(query)==str:
        response = requests.get('http://localhost:8983/solr/techproducts/select?q=' + query)
        response = response.json() 
        for i in range(0):
            print(response["response"]["docs"][i]["name"]) 
    
    return render(request, "search/home.html")

def results(request):
    return render(request, "search/results.html") 


