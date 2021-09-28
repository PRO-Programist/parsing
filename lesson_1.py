import requests
from bs4 import BeautifulSoup

def get_url(url):
    result = requests.get(url)
    return result.text

def get_data(html, title):
    soup = BeautifulSoup(html, 'lxml')
    datas = soup.find_all('p')
    for data in datas:
        print('=---asd-sdasdasjkdhsauidfgsuyf')
        print(title)
        print('+++++++++++++++++++++++')
        print(data)
        print('===============')
        
def get_urls(url,title):
    urls = 'https:' + url
    result = requests.get(urls)
    get_data(result.text,title)

def get_datas(html):
    soup = BeautifulSoup(html, 'lxml')
    items = soup.find_all('a', attrs={'class':'newslink'})
    for item in items:
        item_href = item.get('href')
        if 'turmush' in item_href:
            get_urls(item_href,item.get_text())

def main():
    url = 'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
    total = get_url(url)
    get_datas(total)

main()