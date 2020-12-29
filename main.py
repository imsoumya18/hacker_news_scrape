import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
res2 = requests.get("https://news.ycombinator.com/news?p=2")
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.storylink')
subtexts = soup.select('.subtext')
links2 = soup2.select('.storylink')
subtexts2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtexts = subtexts + subtexts2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtexts):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtexts[idx].select('.score')
        if len(vote):
            point = int(vote[0].getText().replace(' points', ''))
            if point > 99:
                hn.append({'title': title, 'link': href, 'votes': point})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtexts))
