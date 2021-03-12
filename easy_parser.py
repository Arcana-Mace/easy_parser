import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text

def get_data(html):
    soup = BeautifulSoup (html, 'lxml')
    h1 = soup.find('nav', class_='navbar navbar-expand-lg navbar-dark bg-sc-dark').find('div', class_='container nav-container').find('span', class_='d-none d-xl-inline-block').text
    return h1

def main():
    url = 'https://snowcrows.com'
    print(get_data(get_html(url)))



if __name__ == "__main__":
    main()