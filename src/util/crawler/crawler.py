import requests

from lxml import html

url = ''
page = requests.Session.get(url)
tree = html.fromstring(page.text)
result = tree.xpath('//')
