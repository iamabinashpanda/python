# Write a program to fetch hyperlinks from any website entered by the user.

import requests
from bs4 import BeautifulSoup

website_url = input("Enter website url: ")
req = requests.get(website_url,headers={'User-Agent':'Mozilla/5.0'})
if req.status_code == 200:
    soup = BeautifulSoup(req.content,'html.parser')
    with open('books.txt', 'w') as file:
        for link in soup.find_all('a'):
            file.write(website_url + link['href'] + '\n')
else:
    print(req.status_code)
    print(req.text)
