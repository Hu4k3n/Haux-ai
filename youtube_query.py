import urllib.request
from bs4 import BeautifulSoup

def youtube_search(search):
    textToSearch = str(search)
    query = textToSearch.replace(' ','+').replace('-','+')
    url = "https://www.youtube.com/results?search_query=" + query
    response = urllib.request.urlopen(url)
    html = response.read()
    i=str(html).find("\"/watch?v=")
    html=str(html)
    final=html[i+1:i+21]
    print('https://www.youtube.com'+str(final))