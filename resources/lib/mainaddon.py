import requests
import re
from bs4 import BeautifulSoup

def get_soup1(URL1):
    page = requests.get(URL1)
    soup1 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup1))
    return soup1
def get_soup2(URL2):
    page = requests.get(URL2)
    soup2 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup2))
    return soup2
def get_soup3(URL3):
    page = requests.get(URL3)
    soup3 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup3))
    return soup3
def get_soup4(URL4):
    page = requests.get(URL4)
    soup4 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup4))
    return soup4
def get_soup5(URL5):
    page = requests.get(URL5)
    soup5 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup5))
    return soup5
def get_soup6(URL6):
    page = requests.get(URL6)
    soup6 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup6))
    return soup6
def get_soup7(URL7):
    page = requests.get(URL7)
    soup7 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup7))
    return soup7
def get_soup8(URL8):
    page = requests.get(URL8)
    soup8 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup8))
    return soup8
def get_soup9(URL9):
    page = requests.get(URL9)
    soup9 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup9))
    return soup9
def get_soup10(URL10):
    page = requests.get(URL10)
    soup10 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup10))
    return soup10
def get_soup11(URL11):
    page = requests.get(URL11)
    soup11 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup11))
    return soup11
def get_soup12(URL12):
    page = requests.get(URL12)
    soup12 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup12))
    return soup12
def get_soup13(URL13):
    page = requests.get(URL13)
    soup13 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup13))
    return soup13
def get_soup14(URL14):
    page = requests.get(URL14)
    soup14 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup14))
    return soup14
def get_soup15(URL15):
    page = requests.get(URL15)
    soup15 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup15))
    return soup15
def get_soup16(URL16):
    page = requests.get(URL16)
    soup16 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup16))
    return soup16
def get_soup17(URL17):
    page = requests.get(URL17)
    soup17 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup17))
    return soup17
def get_soup18(URL18):
    page = requests.get(URL18)
    soup18 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup18))
    return soup18
def get_soup19(URL19):
    page = requests.get(URL19)
    soup19 = BeautifulSoup(page.text, 'html.parser')
    print("type: ", type(soup19))
    return soup19

def get_playable_podcast1(soup1):
    subjects = []
    for content in soup1.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "http://www.alternativeradio.org/wp-content/uploads/2018/11/Alternative-Radio-logo-for-iTunes.png",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast1(playable_podcast1):
    items = []
    for podcast in playable_podcast1:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast2(soup2):
    subjects = []
    for content in soup2.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast2(playable_podcast2):
    items = []
    for podcast in playable_podcast2:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast3(soup3):
    subjects = []
    for content in soup3.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "http://assets.democracynow.org/assets/DN-Podcast-AUDIO-1d5df65d8936dcfd1387274443b3e0713c5f15dd3fa400331229f4ab39b5c19e.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast3(playable_podcast3):
    items = []
    for podcast in playable_podcast3:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast4(soup4):
    subjects = []
    for content in soup4.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://ssl-static.libsyn.com/p/assets/e/a/1/2/ea122a1b5bea2bf7/MID-iTunes.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast4(playable_podcast4):
    items = []
    for podcast in playable_podcast4:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast5(soup5):
    subjects = []
    for content in soup5.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast5(playable_podcast5):
    items = []
    for podcast in playable_podcast5:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast6(soup6):
    subjects = []
    for content in soup6.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "http://www.corbettreport.com/images/podcastlogoitunes.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast6(playable_podcast6):
    items = []
    for podcast in playable_podcast6:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast7(soup7):
    subjects = []
    for content in soup7.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast7(playable_podcast7):
    items = []
    for podcast in playable_podcast7:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast8(soup8):
    subjects = []
    for content in soup8.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "http://mediapub.it.ox.ac.uk/sites/fred/files/images/album-covers/critical-reasoning-beginners.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast8(playable_podcast8):
    items = []
    for podcast in playable_podcast8:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast9(soup9):
    subjects = []
    for content in soup9.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "http://www.merseysideskeptics.org.uk/podcast/swak.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast9(playable_podcast9):
    items = []
    for podcast in playable_podcast9:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast10(soup10):
    subjects = []
    for content in soup10.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/images/century-of-lies.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast10(playable_podcast10):
    items = []
    for podcast in playable_podcast10:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast11(soup11):
    subjects = []
    for content in soup11.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/media/k2/items/cache/500a44935c8320008f1c713a63e32b8e_XL.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast11(playable_podcast11):
    items = []
    for podcast in playable_podcast11:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast12(soup12):
    subjects = []
    for content in soup12.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/images/edge-effects-icon.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast12(playable_podcast12):
    items = []
    for podcast in playable_podcast12:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast13(soup13):
    subjects = []
    for content in soup13.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/images/For_The_Wild.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast13(playable_podcast13):
    items = []
    for podcast in playable_podcast13:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast14(soup14):
    subjects = []
    for content in soup14.find_all('item'):
        try:
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/images/shows/Law_And_Disorder_Radio.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast14(playable_podcast14):
    items = []
    for podcast in playable_podcast14:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast15(soup15):
    subjects = []
    for content in soup15.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
#            thumbnail = content.find('itunes:image')
#            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "https://www.deprogrammedradio.com/images/Shows-190/security-now.jpg",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast15(playable_podcast15):
    items = []
    for podcast in playable_podcast15:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast16(soup16):
    subjects = []
    for content in soup16.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast16(playable_podcast16):
    items = []
    for podcast in playable_podcast16:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast17(soup17):
    subjects = []
    for content in soup17.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast17(playable_podcast17):
    items = []
    for podcast in playable_podcast17:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast18(soup18):
    subjects = []
    for content in soup18.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast18(playable_podcast18):
    items = []
    for podcast in playable_podcast18:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast19(soup19):
    subjects = []
    for content in soup19.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast19(playable_podcast19):
    items = []
    for podcast in playable_podcast19:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast20(soup20):
    subjects = []
    for content in soup20.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 

    return subjects
def compile_playable_podcast20(playable_podcast20):
    items = []
    for podcast in playable_podcast20:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast21(soup21):
    subjects = []
    for content in soup21.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast21(playable_podcast21):
    items = []
    for podcast in playable_podcast21:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast22(soup22):
    subjects = []
    for content in soup22.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': thumbnail,
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast22(playable_podcast22):
    items = []
    for podcast in playable_podcast22:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast23(soup23):
    subjects = []
    for content in soup23.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast23(playable_podcast23):
    items = []
    for podcast in playable_podcast23:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items

def get_playable_podcast24(soup24):
    subjects = []
    for content in soup24.find_all('item'):
        try:        
            link = content.find('enclosure')
            link = link.get('url')
            print("\n\nLink: ", link)
            title = content.find('title')
            title = title.get_text()
            thumbnail = content.find('itunes:image')
            thumbnail = thumbnail.get('href')
        except AttributeError:
            continue
        item = {
                'url': link,
                'title': title,
                'thumbnail': "",
        }
        subjects.append(item) 
    return subjects
def compile_playable_podcast24(playable_podcast24):
    items = []
    for podcast in playable_podcast24:
        items.append({
            'label': podcast['title'],
            'thumbnail': podcast['thumbnail'],
            'path': podcast['url'],
            'is_playable': True,
    })
    return items
