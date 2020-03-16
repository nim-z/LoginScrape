from bs4 import BeautifulSoup
import requests
from lxml import html

session = requests.Session()
result = session.get('https://student.amizone.net/Home')
token = result.cookies['__RequestVerificationToken']
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='__RequestVerificationToken']/@value")))[0]
token = session.cookies['__RequestVerificationToken']
print(f"AUTH TOKEN {authenticity_token}")
payload = f"__RequestVerificationToken" \
          "=" + authenticity_token + "&_UserName=7671389&_Password=ecc3f4 "
headerpayload = {'Host': 'student.amizone.net',
                 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,/;q=0.8',
                 'Accept-Language': 'en-US,en;q=0.5',
                 'Accept-Encoding': 'gzip, deflate, br',
                 'Content-Type': 'application/x-www-form-urlencoded',
                 'Content-Length': '170',
                 'Origin': 'https://student.amizone.net',
                 'Connection': 'keep-alive',
                 'Referer': 'https://student.amizone.net/login/',
                 'Cookie': '__RequestVerificationToken=' + token,
                 'Upgrade-Insecure-Requests': '1'
                 }
getpayload = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__RequestVerificationToken=' + token,
    'Host': 'student.amizone.net',
    'Referer': 'https://student.amizone.net/',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36'
}
result = session.post('https://student.amizone.net/Login/Login', data=payload, headers=headerpayload)
# print(result.content)
print(result.status_code)
soup = BeautifulSoup(result.content, 'html.parser')
# print(soup.prettify())
span = soup.find('span', class_='user-info')
number = span.small.get_text()
name = span.contents[0]
course_list = soup.find('ul', class_='item-list', id='tasks').find_all('li')
final_course_list = []
attendance_list = []
for a in course_list:
    children = a.find_all('div', class_='pull-right easy-pie-chart percentage')
    children1 = a.find_all('div', class_='pull-right class-count')
    print(children[0].attrs['data-percent'])
    print(children1[0].span.text)
    final_course_list.append(a.label.span.text)
#print(span)
#for i in final_course_list:
    #print(i)
for i in attendance_list:
    print(i)
print(name.strip())
print(number)
# print(soup.prettify())
