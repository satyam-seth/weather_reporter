from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views import View
from .forms import SearchForm

# Create your views here.

def get_report(city):
    USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE="en-US,en;q=0.5"
    session=requests.Session()
    session.headers['User-Agent']=USER_AGENT
    session.headers['Accept-Language']=LANGUAGE
    session.headers['Content-Language']=LANGUAGE
    city=city.replace(' ','+')
    result=dict()
    try:
        html_content=session.get(f'https://www.google.com/search?q=weather+in+{city}').text
        soup=BeautifulSoup(html_content,'html.parser')
        result['region']=soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text
        result['temp_now']=soup.find("div",attrs={"class":"BNeawe iBp4i AP7Wnd"}).text
        result['day_hour'],result['weather_now']=soup.find("div",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text.split('\n')
    except:
        result['error']='invalid location'
    return result

# print(get_report(input()))

class HomeView(View):
    def get(self,request):
        fm=SearchForm()
        return render(request,'core/home.html',{'form':fm})

    def post(self,request):
        fm=SearchForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['loc'])
        return render(request,'core/home.html',{'form':fm})