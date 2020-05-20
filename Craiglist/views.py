from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.compat import quote_plus
from bs4 import BeautifulSoup

BASE_CRAIGLIST_URL = 'https://delhi.craigslist.org/search/bbb?query={}'

def home(request):
    return render(request,"base.html")

def new_search(request):
    search = request.POST.get("search")
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup =BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a', {'class':'result-title'})
    print(post_titles)
    context = {
        'search' : search ,
    }
    return render(request,"Craiglist/new_search.html" ,context)