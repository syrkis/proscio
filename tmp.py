import requests

page = requests.get('https://stopwords.syrkis.com')
content = page.text.split('\n')
content = [word for word in content]
print(content)