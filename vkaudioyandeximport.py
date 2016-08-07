# -*- coding: utf-8 -*-
import time
import urllib.parse
import selenium
from selenium import webdriver
import webbrowser

import requests

def send_keys_to_input_by_xpath(webdriver, xpath, keys):
    inps = webdriver.find_elements_by_xpath(xpath)
    if not inps:
        return -1
    inp = inps[0]
    inp.send_keys(keys)
    return 0

reqParams = {'client_id': '2989747', 'display': 'page', 'response_type': 'token', 'redirect_uri': 'https://oauth.vk.com/blank.html', 'scope':'audio', 'v':'5.37'}
# r = requests.get('https://oauth.vk.com/authorize', params=pm)
# print(r.text)

# print(urllib.parse.urlencode(pm))


url = 'https://oauth.vk.com/authorize?' + urllib.parse.urlencode(reqParams)
browser = webdriver.Firefox()
browser.get(url)
while not url in browser.current_url:
    time.sleep(1)
print('HERE')

login = 'KarKarbI41000000@rambler.ru'
password = 'MephiMoscow533'
login_xpath = '/html/body/div/form/table/tbody/tr[2]/td/div[2]/div/div/input[6]'
if send_keys_to_input_by_xpath(browser, login_xpath, login):
    print('SHIT')
pass_xpath = '/html/body/div/form/table/tbody/tr[2]/td/div[2]/div/div/input[7]'
send_keys_to_input_by_xpath(browser, pass_xpath, password)
btn_xpath = '/html/body/div/form/table/tbody/tr[2]/td/div[2]/div/div/div[3]/button'
browser.find_elements_by_xpath(btn_xpath)[0].click()
while not 'https://oauth.vk.com/blank.html' in browser.current_url:
    time.sleep(1)
resParams = dict(urllib.parse.parse_qsl(urllib.parse.urlparse(browser.current_url).fragment))
user_id = resParams.get('user_id')
access_token = resParams.get('access_token')
print(access_token)

req_user_id = '120276236'
vk_api_audio_params = {'owner_id': req_user_id, 'access_token': access_token}
vk_api_audio_url = 'https://api.vk.com/method/audio.get'
# print(reqAudioUrl)
reqAudio = requests.get(vk_api_audio_url, params=vk_api_audio_params)
print(reqAudio.encoding)
with open('response.txt', 'wb') as f:
    f.write(reqAudio.text.encode('utf8'))

reqAudioJson = reqAudio.json()
# print(reqAudioJson)
trackList = []
resp = reqAudioJson.get('response')
trackAmount = resp[0]
tracks = resp[1:]
for track in tracks:
    trackList.append(track['artist'] + ' - ' + track['title'])

print(len(tracks))
print(len(trackList))
print(trackAmount)
with open('tracklist_{}.txt'.format(trackAmount), 'wb') as f:
    for track in trackList:
        f.write('{}\n'.format(track).encode('utf8'))


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