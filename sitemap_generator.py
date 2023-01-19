from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
my_url = 'https://example.com'

def get_date(url):
    m_dict = {'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
              'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
              'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'}

    with urlopen(my_url) as response:
        date = response.headers.get('Last-Modified').split()

    return f'{date[3]}-{m_dict.get(date[2])}-{date[1]}T{date[4]}+01:00'

def get_urls(url):
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
     
    urls = []
    for link in soup.find_all('a'):
        l = link.get('href')
        if 'mailto' in l:
            continue
        elif '#' in l:
            continue
        elif url + l not in urls:
            urls.append(url + l)    
    return urls
    
def generate_map(url):
    urls = get_urls(url)
    date = get_date(url)

    tag_urls = f'''<url>
      <loc>{url}</loc>
      <lastmod>{date}</lastmod>
      <priority>1.0</priority>
    </url>
    '''
    for link in urls:
        tag_urls += f'''<url>
      <loc>{link}</loc>
      <lastmod>{date}</lastmod>
      <priority>0.6</priority>
    </url>
    '''

    xml = f'''<?xml version='1.0' encoding='UTF-8'?>
   <urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>
    {tag_urls}
   </urlset>
    '''

    with open('sitemap.xml', 'w') as f:
        f.write(xml)


if __name__ == '__main__':
    generate_map(my_url)

