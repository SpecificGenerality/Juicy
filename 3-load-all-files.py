import os
import codecs
from bs4 import BeautifulSoup

directory_in_str = "archives/facebook-justinyan33/messages"
directory = os.fsencode(directory_in_str)


for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".html"): 
        f=codecs.open(os.path.join(directory_in_str, filename), 'r', encoding='utf-8')
        soup = BeautifulSoup(f.read(), 'html.parser')
        print(soup.prettify()) #replace with parsing
        continue
    else:
        continue