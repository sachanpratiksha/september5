import requests
from bs4 import BeautifulSoup

base_url = 'http://nytimes.com'
r = requests.get(base_url)
htmlcontent=r.content
soup = BeautifulSoup(htmlcontent,"html5lib")
anchors=soup.find_all('a')
alllinks=set()

filename=input('Enter filename to save')
with open(filename, 'w') as f:
    for all in anchors:
        if (all.get("href") != '#'):
            linktext = "https://nytimes.com" + all.get("href")
            alllinks.add(all)
            # print(linktext)
            f.write(linktext.strip())


# open_file = open('file_to_save.txt', 'w')
#   open_file.write('A string to write')
#   open_file.close()

