from lxml import html
import requests, random, time
links = []
num = 1
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
url = 'https://www.chaiandconversation.com/persian-dictionary?page=' + str(num)
for i in range(132):
    links.append(url)
    num += 1
    url = 'https://www.chaiandconversation.com/persian-dictionary?page=' + str(num)

for url in links:
    page = requests.get(url, headers=headers)
    tree = html.fromstring(page.content)
    pers = tree.xpath('.//td[1]/a/text()')
    tran = tree.xpath('.//td[2]/text()')
    for i in pers:
        if len(i) == 1 or 'Lesson' in i.split(' '):
            pers.remove(i)

    dic = dict(zip(pers, tran))
    for k, v in dic.items():
        with open('my_dictionary.txt', 'a', encoding='utf-8') as f:
            f.write(f'{k}: {v}' + "\n")    

    time.sleep(random.randint(5, 25))

