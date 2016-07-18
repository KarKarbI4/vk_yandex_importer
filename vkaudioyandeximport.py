__author__ = 'Виктор'
import time
import urllib.parse
import selenium
from selenium import webdriver
import webbrowser

import requests
reqParams = {'client_id': '2989747', 'display': 'page', 'response_type': 'token', 'redirect_uri': 'https://oauth.vk.com/blank.html', 'scope':'audio', 'v':'5.37'}
# r = requests.get('https://oauth.vk.com/authorize', params=pm)
# print(r.text)

# print(urllib.parse.urlencode(pm))


url = 'https://oauth.vk.com/authorize?' + urllib.parse.urlencode(reqParams)
browser = webdriver.Firefox()
browser.get(url)
while not 'https://oauth.vk.com/blank.html' in browser.current_url:
    time.sleep(1)
resParams = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(browser.current_url).fragment))
user_id = resParams.get('user_id')
access_token = resParams.get('access_token')
print(access_token)

reqAudioParams = {'owner_id': user_id, 'access_token': access_token}
reqAudioUrl = 'https://api.vk.com/method/audio.get?' + urllib.parse.urlencode(reqAudioParams)
print(reqAudioUrl)
reqAudio = requests.get(reqAudioUrl)
reqAudioJson = reqAudio.json()
print(reqAudioJson)
trackList = []
trackAmount = reqAudioJson.get('response')[0]
for track in reqAudioJson.get('response')[1:]:
    trackList.append(track['artist'] + ' - ' + track['title'])

print(trackAmount)
for track in trackList:
    print(track)


browser.get('https://music.yandex.ru/import')
textform = browser.find_elements_by_class_name("page-import__freetext")
for track in trackList:
    textform[0].send_keys(track)
# reqImportUrl = 'https://music.yandex.ru/import'
# reqImport = requests.get(reqImportUrl)
# print (reqImport.text)


# vkaudio = open('vkaudio', encoding="utf8")
# audiolist = vkaudio.readlines()
# vkaudio.close()
#
# print(audiolist)
#
# vkaudio = open('vkaudio', 'w', encoding="utf8")
# for line in audiolist:
#     if '–' in line:
#         vkaudio.write(line)
# vkaudio.close()