from django.shortcuts import render

def home(request):
    query = request.POST.get("query_search") 
    print(query) 
    return render(request, "search/home.html")

def results(request):
    return render(request, "search/results.html") 


