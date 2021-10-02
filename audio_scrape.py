import requests
from bs4 import BeautifulSoup as bs4

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'https://fulllengthaudiobooks.com/michael-e-gerber-the-e-myth-revisited-audiobook/'

page = requests.get(url, headers=headers)
soup = bs4(page.content, 'lxml')

audio = soup.find_all("audio", class_="wp-audio-shortcode")
links = [i.find('a').text.strip() for i in audio]

for (i, link) in enumerate(links, start=1):
    data = requests.get(link)
    with open(f'The e myth revisited_0{i}.mp3', 'wb') as f:
        f.write(data.content)
    print(f'downloading file {i} of {len(links)} ...')

print('files downloaded!')


    # 
