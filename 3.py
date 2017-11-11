import os
import codecs
from bs4 import BeautifulSoup
import sys

directory_in_str = "archives/facebook-justinyan33/messages"
directory = os.fsencode(directory_in_str)

i = 1

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".html"): 
        f=codecs.open(os.path.join(directory_in_str, filename), 'r', 'utf-8')
        # print(f.read().encode('utf-8'))
        content = f.read().encode('utf-8')
        soup = BeautifulSoup(content, 'html.parser')
        print(i,": ", filename)
        sys.stdout.flush()
        i+=1
        # soup.find_all("a")
    #     soup.prettify()