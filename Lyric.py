from bs4 import BeautifulSoup
import requests

# Requires Cifra Club music URL.
url = input('Insert song link on cifraclub.com.br: ')
result = requests.get(url)
content = result.text

soup = BeautifulSoup(content, 'lxml')

# Searching for div containing music title and lyrics.
box = soup.find('div', attrs={'class': 'g-1 g-fix cifra'})

title = box.find('h1').get_text()
artist = box.find('h2').get_text()
music = box.find('div', attrs={'class': 'letra'})

# Keeping spacing.
for br in music.find_all('br'):
    br.replace_with('\n')

print(title)
print(artist)
print(music.get_text())

# Exporting .txt file.
with open(f'{title} ({artist}).txt', 'w', encoding="utf-8") as file:
    file.write(music.get_text())