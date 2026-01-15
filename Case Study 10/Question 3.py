# 3. Perform Web Scrapping on the following page:
from bs4 import BeautifulSoup
import re
html_content = '<html><head><title>Page title</title></head><body><p id="firstpara" align="center">This is paragraph<b>one</b></p><p id="secondpara" align="blah">This is paragraph<b>two</b></p></body></html>'
soup = BeautifulSoup(html_content, 'html.parser')

# 1. Read the page using Beautiful Soup and show it in a well-formatted,indented manner

with open('q3i.html','w') as html_file:
    html_file.write(soup.prettify())

# 2. Print the b tag from the page
print("start b tag")
for bold in soup.find_all('b'):
    print(bold.text)

# 3. Print all the tags that start from b
print("starts from b")
for bold in soup.find_all(re.compile('^b')):
    print(bold.text)

# 4. Print text from the tags having title and p by using lists
print("Tags from title and paragraph")
tags = soup.find_all(['title','p'])
print("\n".join([tag.text for tag in tags]))

# 5. Print text from the tags having title and p by using dictionaries

keys = ['title','p']
data = {key: [] for key in keys}
for key in keys:
    for tag in soup.find_all(key):
        data[key].append(tag.text)
print(data)

# 6. Print all the tag names present in the page
print("Tag present in the page :")
tags = [tag.name for tag in soup.find_all()]
print(",".join(set(tags)))

# 7. Print the complete tag that has two, and only two, attributes
for tag in soup.find_all():
    if len(tag.attrs)==2:
        print(tag)

# 8.