from bs4 import BeautifulSoup
from urllib.request import urlopen

techmeme_url = 'http://techmeme.com'
techmeme_html = urlopen(techmeme_url)
soup = BeautifulSoup(techmeme_html)

story_links = [story.a for story in soup.find("div", {"id": "topcol1"}).
               findAll("strong")]

for story in story_links:
    print(story.contents[0], "\n", "\t==>", story.get('href'))
