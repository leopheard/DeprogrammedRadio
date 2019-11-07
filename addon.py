from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon
plugin = Plugin()
url1 = "https://www.alternativeradio.org/arpodcast.xml" #ALTERNATIVERADIO
url2 = "https://podcasts.apple.com/us/podcast/between-the-lines-radio-newsmagazine-podcast/id387215195" #BETWEENTHELINES
url3 = "https://www.democracynow.org/podcast.xml" #DN
url4 = "https://www.middletheory.com/feed/podcast/" #MIDDLETHEORY
url5 = "https://www.bradblog.com/podcastgen/bradcast/feed.xml" #BRADCAST
url6 = "http://feeds.feedburner.com/CorbettreportcomPodcast" #CORBETT
url7 = "http://feeds.soundcloud.com/users/soundcloud:users:550574712/sounds.rss" #WINDOWSONTHEWORLD
url8 = "http://mediapub.it.ox.ac.uk/feeds/129128/audio.xml" #CRITICALREASONINGFORBEGINNERS
url9 = "https://feeds.feedburner.com/swak" #SKEPTICS-WITH-A-K
url10 = "http://drugtruth.net/century_of_lies/itunes" #CENTURY-OF-LIES
url11 = "https://www.ecoshock.org/feed/cdquality" #ECOSHOCK
url12 = "https://edgeeffects.net/feed/podcast/" #EDGEEFFECTS
url13 = "http://feeds.feedburner.com/unlearnandrewild" #FORTHEWILD
url14 = "http://feeds.feedburner.com/lawanddisorder" #LAWANDDISORDER
url15 = ""
url16 = ""
url17 = ""
url18 = ""
url19 = ""
url20 = ""
url21 = ""
url22 = ""
url23 = ""
url24 = ""
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30000),
            'path': "https://www.deprogrammedradio.com//mobile-mono.mp3?nocache=15730729?nocache=850587",
            'thumbnail': "https://cdn-profiles.tunein.com/s218630/images/logoq.jpg",
            'is_playable': True},
        {
            'label': plugin.get_string(30001),
            'path': plugin.url_for('episodes1'),
            'thumbnail': "http://www.alternativeradio.org/wp-content/uploads/2018/12/arlogo-podcast.jpg"},
        {
            'label': plugin.get_string(30002),
            'path': plugin.url_for('episodes2'),
            'thumbnail': "https://is5-ssl.mzstatic.com/image/thumb/Podcasts123/v4/ae/eb/f9/aeebf97a-8005-0635-668b-4ac0bf8e6d14/mza_1535653222288662846.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30003),
            'path': plugin.url_for('episodes3'),
            'thumbnail': "http://assets.democracynow.org/assets/DN-Podcast-AUDIO-1d5df65d8936dcfd1387274443b3e0713c5f15dd3fa400331229f4ab39b5c19e.jpg"},
        {
            'label': plugin.get_string(30004),
            'path': plugin.url_for('episodes4'),
            'thumbnail': "https://is1-ssl.mzstatic.com/image/thumb/Podcasts123/v4/61/32/70/61327000-fa31-c5e1-948a-2f4a7c737ad5/mza_9144477857832551567.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30005),
            'path': plugin.url_for('episodes5'),
            'thumbnail': "https://www.deprogrammedradio.com/images/Shows-190/Bradcast_Radio.jpg"},
        {
            'label': plugin.get_string(30006),
            'path': plugin.url_for('episodes6'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/83/79/fb/8379fb81-8d60-bfb2-059d-449d97866ecf/mza_7067909342739060738.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30007),
            'path': plugin.url_for('episodes7'),
            'thumbnail': "https://i1.sndcdn.com/avatars-000545806026-ev4smr-large.jpg"},
        {
            'label': plugin.get_string(30008),
            'path': plugin.url_for('episodes8'),
            'thumbnail': "http://podcasts.ox.ac.uk/sites/default/files/styles/large/public/images/album-covers/critical-reasoning-beginners.jpg?itok=PyM9do5o"},
        {
            'label': plugin.get_string(30009),
            'path': plugin.url_for('episodes9'),
            'thumbnail': "https://www.deprogrammedradio.com/images/Skeptics-With-A-K-2.jpg"},
        {
            'label': plugin.get_string(30010),
            'path': plugin.url_for('episodes10'),
            'thumbnail': "https://www.deprogrammedradio.com/images/century-of-lies.jpg"},
        {
            'label': plugin.get_string(30011),
            'path': plugin.url_for('episodes11'),
            'thumbnail': "https://www.deprogrammedradio.com/media/k2/items/cache/500a44935c8320008f1c713a63e32b8e_XL.jpg"},
        {
            'label': plugin.get_string(30012),
            'path': plugin.url_for('episodes12'),
            'thumbnail': "https://www.deprogrammedradio.com/images/edge-effects-icon.jpg"},
        {
            'label': plugin.get_string(30013),
            'path': plugin.url_for('episodes13'),
            'thumbnail': "https://www.deprogrammedradio.com/images/For_The_Wild.jpg"},
        {
            'label': plugin.get_string(30014),
            'path': plugin.url_for('episodes14'),
            'thumbnail': "https://www.deprogrammedradio.com/images/shows/Law_And_Disorder_Radio.jpg"},
        {
            'label': plugin.get_string(30015),
            'path': plugin.url_for('episodes15'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30016),
            'path': plugin.url_for('episodes16'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30017),
            'path': plugin.url_for('episodes17'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30018),
            'path': plugin.url_for('episodes18'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30019),
            'path': plugin.url_for('episodes19'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30020),
            'path': plugin.url_for('episodes20'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30021),
            'path': plugin.url_for('episodes21'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30022),
            'path': plugin.url_for('episodes22'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30023),
            'path': plugin.url_for('episodes23'),
            'thumbnail': ""},
        {
            'label': plugin.get_string(30024),
            'path': plugin.url_for('episodes24'),
            'thumbnail': ""},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items
@plugin.route('/episodes2/')
def episodes2():
    soup2 = mainaddon.get_soup2(url2)
    playable_podcast2 = mainaddon.get_playable_podcast2(soup2)
    items = mainaddon.compile_playable_podcast2(playable_podcast2)
    return items
@plugin.route('/episodes3/')
def episodes3():
    soup3 = mainaddon.get_soup3(url3)
    playable_podcast3 = mainaddon.get_playable_podcast3(soup3)
    items = mainaddon.compile_playable_podcast3(playable_podcast3)
    return items
@plugin.route('/episodes4/')
def episodes4():
    soup4 = mainaddon.get_soup4(url4)   
    playable_podcast4 = mainaddon.get_playable_podcast4(soup4)
    items = mainaddon.compile_playable_podcast4(playable_podcast4)
    return items
@plugin.route('/episodes5/')
def episodes5():
    soup5 = mainaddon.get_soup5(url5)
    playable_podcast5 = mainaddon.get_playable_podcast5(soup5)
    items = mainaddon.compile_playable_podcast5(playable_podcast5)
    return items
@plugin.route('/episodes6/')
def episodes6():
    soup6 = mainaddon.get_soup6(url6)
    playable_podcast6 = mainaddon.get_playable_podcast6(soup6)
    items = mainaddon.compile_playable_podcast6(playable_podcast6)
    return items
@plugin.route('/episodes7/')
def episodes7():
    soup7 = mainaddon.get_soup7(url7)
    playable_podcast7 = mainaddon.get_playable_podcast7(soup7) 
    items = mainaddon.compile_playable_podcast7(playable_podcast7)
    return items
@plugin.route('/episodes8/')
def episodes8():
    soup8 = mainaddon.get_soup8(url8)
    playable_podcast8 = mainaddon.get_playable_podcast8(soup8)
    items = mainaddon.compile_playable_podcast8(playable_podcast8)
    return items
@plugin.route('/episodes9/')
def episodes9():
    soup9 = mainaddon.get_soup9(url9)
    playable_podcast9 = mainaddon.get_playable_podcast9(soup9)
    items = mainaddon.compile_playable_podcast9(playable_podcast9)
    return items
@plugin.route('/episodes10/')
def episodes10():
    soup10 = mainaddon.get_soup10(url10)
    playable_podcast10 = mainaddon.get_playable_podcast10(soup10)
    items = mainaddon.compile_playable_podcast10(playable_podcast10)
    return items
@plugin.route('/episodes11/')
def episodes11():
    soup11 = mainaddon.get_soup11(url11)
    playable_podcast11 = mainaddon.get_playable_podcast11(soup11)
    items = mainaddon.compile_playable_podcast11(playable_podcast11)
    return items
@plugin.route('/episodes12/')
def episodes12():
    soup12 = mainaddon.get_soup12(url12) 
    playable_podcast12 = mainaddon.get_playable_podcast12(soup12)
    items = mainaddon.compile_playable_podcast12(playable_podcast12)
    return items
@plugin.route('/episodes13/')
def episodes13():
    soup13 = mainaddon.get_soup13(url13)
    playable_podcast13 = mainaddon.get_playable_podcast13(soup13)
    items = mainaddon.compile_playable_podcast13(playable_podcast13)
    return items
@plugin.route('/episodes14/')
def episodes14():
    soup14 = mainaddon.get_soup14(url14)
    playable_podcast14 = mainaddon.get_playable_podcast14(soup14)
    items = mainaddon.compile_playable_podcast14(playable_podcast14)
    return items
@plugin.route('/episodes15/')
def episodes15():
    soup15 = mainaddon.get_soup15(url15)
    playable_podcast15 = mainaddon.get_playable_podcast15(soup15)
    items = mainaddon.compile_playable_podcast15(playable_podcast15)
    return items
@plugin.route('/episodes16/')
def episodes16():
    soup16 = mainaddon.get_soup16(url16)
    playable_podcast16 = mainaddon.get_playable_podcast16(soup16)
    items = mainaddon.compile_playable_podcast16(playable_podcast16)
    return items
@plugin.route('/episodes17/')
def episodes17():
    soup17 = mainaddon.get_soup17(url17)
    playable_podcast17 = mainaddon.get_playable_podcast17(soup17)
    items = mainaddon.compile_playable_podcast17(playable_podcast17)
    return items
@plugin.route('/episodes18/')
def episodes18():
    soup18 = mainaddon.get_soup18(url18)
    playable_podcast18 = mainaddon.get_playable_podcast18(soup18)
    items = mainaddon.compile_playable_podcast18(playable_podcast18)
    return items
@plugin.route('/episodes19/')
def episodes19():
    soup19 = mainaddon.get_soup19(url19)
    playable_podcast19 = mainaddon.get_playable_podcast19(soup19)
    items = mainaddon.compile_playable_podcast19(playable_podcast19)
    return items
@plugin.route('/episodes20/')
def episodes20():
    soup20 = mainaddon.get_soup20(url20)
    playable_podcast20 = mainaddon.get_playable_podcast20(soup20)
    items = mainaddon.compile_playable_podcast20(playable_podcast20)
    return items
@plugin.route('/episodes21/')
def episodes21():
    soup21 = mainaddon.get_soup21(url21)
    playable_podcast21 = mainaddon.get_playable_podcast21(soup21)
    items = mainaddon.compile_playable_podcast21(playable_podcast21)
    return items
@plugin.route('/episodes22/')
def episodes22():
    soup22 = mainaddon.get_soup22(url22)
    playable_podcast22 = mainaddon.get_playable_podcast22(soup22)
    items = mainaddon.compile_playable_podcast22(playable_podcast22)
    return items
@plugin.route('/episodes23/')
def episodes23():
    soup23 = mainaddon.get_soup23(url23)
    playable_podcast23 = mainaddon.get_playable_podcast23(soup23)
    items = mainaddon.compile_playable_podcast23(playable_podcast23)
    return items
@plugin.route('/episodes24/')
def episodes24():
    soup24 = mainaddon.get_soup24(url24)
    playable_podcast24 = mainaddon.get_playable_podcast24(soup24)
    items = mainaddon.compile_playable_podcast24(playable_podcast24)
    return items
if __name__ == '__main__':
    plugin.run()