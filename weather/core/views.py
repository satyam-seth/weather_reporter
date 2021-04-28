import requests
from bs4 import BeautifulSoup

# Create your views here.

def get_report(city):
    USER_AGENT="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE="en-US,en;q=0.5"
    session=requests.Session()
    session.headers['User-Agent']=USER_AGENT
    session.headers['Accept-Language']=LANGUAGE
    session.headers['Content-Language']=LANGUAGE
    city=city.replace(' ','+')
    html_content=session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    soup=BeautifulSoup(html_content,'html.parser')
    result = dict()
    result['region']=soup.find("span",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text
    result['temp_now']=soup.find("div",attrs={"class":"BNeawe iBp4i AP7Wnd"}).text
    result['dayhour'],result['weather_now']=soup.find("div",attrs={"class":"BNeawe tAd8D AP7Wnd"}).text.split('\n')
    return result

print(get_report(input()))