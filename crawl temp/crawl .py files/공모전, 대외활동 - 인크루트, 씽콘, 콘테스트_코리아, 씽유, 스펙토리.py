#!/usr/bin/env python
# coding: utf-8

<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[7]:
=======
# In[34]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


import pandas as pd
from pandas import json_normalize
import numpy as np
from bs4 import BeautifulSoup
import re
import urllib.request
from urllib.request import urlopen
import ssl
from dateutil.parser import parse
import json
import requests
context=ssl._create_unverified_context()


<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[8]:
=======
# In[35]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


# 공모전 인크루트
inc_title=[]
inc_host=[]
inc_terms=[]
inc_start_bef=[]
inc_end_bef=[]
inc_qualification=[]
inc_links=[]
inc_real_links=[]
base_url='https://gongmo.incruit.com/list/gongmolist.asp?ct=1&category=11'
webpage = urlopen(base_url,context=context)
soup = BeautifulSoup(webpage, 'html.parser')
for i in range(1,13):
    try:
<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
        inc_title.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.gmtitle > ul > a')[0].get_text())
        inc_host.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.company')[0].get_text().lstrip('\r\n\t\t\t\t\t\t\t').strip('\r\n\t\t\t\t\t\t\t'))
        inc_terms.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.due')[0].get_text())
        inc_links.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.gmtitle > ul > a')[0].get('href'))
=======
=======
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
        inc_host.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.company')[0].get_text().lstrip('\r\n\t\t\t\t\t\t\t').strip('\r\n\t\t\t\t\t\t\t'))
        inc_terms.append(soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.due')[0].get_text())
        inc_link_tmp = soup.select('#tbdyGmScrap > tr:nth-child('+str(i)+') > td.gmtitle > ul > a')[0].get('href')
        inc_links.append(inc_link_tmp)
        inc_link_tmp = urlopen(inc_link_tmp,context=context)
        tmp_soup = BeautifulSoup(inc_link_tmp, 'html.parser')
        inc_title.append(tmp_soup.select('h3.job_new_top_title')[0].get_text().rstrip().lstrip())
        
<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
    except:
        break


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[9]:
=======
# In[36]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[3]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


inc_start_bef=[]
inc_end_bef=[]
for inc_term in inc_terms:
    inc_start_day,inc_end_day=inc_term.split("~")
    inc_start_bef.append('20'+inc_start_day.replace('.','. '))
    inc_end_bef.append('20'+inc_end_day.replace('.','. '))


<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[10]:
=======
# In[37]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


# 공모전 콘테스트 코리아
ck_title = []
ck_date = []
ck_link = []
ck_tag = []
ck_target = ['대학생', '일반인', '누구나']

for n in range(1, 6):
    url = ('https://www.contestkorea.com/sub/list.php?displayrow=12&int_gbn=1&Txt_sGn=1&Txt_key=all&Txt_word=&Txt_bcode=030210001&Txt_code1=&Txt_aarea=&Txt_area=&Txt_sortkey=a.int_sort&Txt_sortword=desc&Txt_host=&Txt_tipyn=&Txt_actcode=&page='+str(n))
    headers = {'User-Agent': 'Mozilla/5.0'} 
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')

   
    list_crawl = soup.select('#frm > div > div.list_style_2 > ul')

    for li in list_crawl:        
        for num in range(0, 12):
            tmp = []
            try:
                li_target = li.select('li > ul > li.icon_2')[num].get_text().replace('\t', '').replace('\n', '')
                if any(word in li_target for word in ck_target):
                    li_title = li.select('li > div.title > a > span.txt')[num].get_text()
                    li_date_tmp = li.select('li > div.date > div > span.step-1')[num].text
                    li_date = li_date_tmp.replace("\n", "").replace("\t", "").split('~')[-1]
                    li_date1, lidate2 = li_date.split('.')
                    li_date = '2022. '+li_date1+'. '+lidate2
                    link_tmp = li.select('li > div.title > a')[num]
                    link_tmp = link_tmp['href']               
                    ck_title.append(li_title)
                    ck_date.append(li_date)
                    ck_link.append("https://www.contestkorea.com/sub/" + link_tmp)
                else:            
                    continue         
            except IndexError:
                break
            
            try:
                li_tmp = li.select('li')[3*num]
            except IndexError:
                break          
            for i in range(0, 5):
                try:
                    cat = li_tmp.select('div.title > a > span.category')[i].get_text()
                    tmp.append(cat)
                except IndexError:
                    break    
            ck_tag.append(tmp)


<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[11]:
=======
# In[38]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


# 공모전 씽콘
url_base = 'https://www.thinkcontest.com/Contest/CateField.html?page=1&c=11'
headers = {'User-Agent': 'Mozilla/5.0'}
res = requests.get(url_base, headers=headers)
soup = BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')
key = ['과학/공학', '게임/소프트웨어']
tc_links = []
tc_titles = []
tc_dday = []
tc_inst = []
tc_dates = []
k = 1
    
while k <= 10:
    url = 'https://www.thinkcontest.com/Contest/CateField.html?page=' + str(k) + '&c=11'
    base_url = 'https://www.thinkcontest.com/'
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')
    len_link = len(soup.select(' .txt-left > .contest-title > a'))
    for i in range(len_link):
        if soup.select(' td > span ')[i].text.replace('\n', '') == '마감':
            break
        else:
            tc_titles.append(soup.select(' .txt-left > .contest-title > a')[i].text)
            tc_links.append(base_url + soup.select('.txt-left > .contest-title > a ')[i]['href'])
            tc_dday.append(soup.select(' td > p ')[i].text.split('-')[1])
    k=k+1
                            
str_date = []
end_date = []
participate = []
for i in range(len(tc_links)):
    headers = {'User-Agent': 'Mozilla/5.0'}
    res = requests.get(tc_links[i], headers=headers)
    soup = BeautifulSoup(res.content.decode('utf-8', 'replace'), 'html.parser')
    html = soup.select(' tr')
    text = str(html).replace('\n', '')
    certi = re.compile('참가자격' + '.{200}')
    test = certi.findall(text)[0]
    partis = []
    if '제한없음' in test:
        partis.append('대학(원)생')
        pass
    elif '일반인' in test:
        partis.append('대학(원)생')
        pass
    elif '국내외 석학과 연구진' in test:
        partis.append('대학원생')
        pass
    elif '대학생' in test:
        if '대학원생' in test:
            partis.append('대학(원)생')
            pass
        else :
            partis.append('대학생')
            pass
    elif '대학원생' in test:
        partis.append('대학원생')
    else : 
        pass
            

    participant = str(partis).replace('[', '').replace(']', '').replace("'", "")
    start = re.compile('접수기간' + '.{19}')
    strdate = start.findall(text)[0].split('<td>')[1]
    end = re.compile('접수기간' + '.{32}')
    enddate = end.findall(text)[0].split('~')[1].replace(' ', '')
    enddate1, enddate2, enddate3 = enddate.split('-')
    enddate = enddate1+'. '+enddate2+'. '+enddate3
    participate.append(participant)
    str_date.append(strdate)
    end_date.append(enddate)
    tc_inst.append(soup.select(' tbody > tr > td ')[0].text)


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[12]:
=======
# In[39]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[6]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


gongmo = []

for i in range(len(inc_title)):
    li_tmp = {"title": inc_title[i], "dday": inc_end_bef[i], "link": inc_links[i], "tag": inc_host[i], "분류": "공모전"}
    gongmo.append(li_tmp)

for i in range(len(ck_title)):
    li_tmp = {"title": ck_title[i], "dday": ck_date[i], "link": ck_link[i], "tag": ck_tag[i], "분류": "공모전"}
    gongmo.append(li_tmp)

for i in range(len(tc_links)):
    li_tmp = {"title": tc_titles[i], "dday": end_date[i], "link": tc_links[i], "tag": participate[i], "분류": "공모전"}
    gongmo.append(li_tmp)


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[13]:
=======
# In[40]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[7]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


d_title = []
title = []
d_link = []
link = []
d_date = []
date = []

<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py

<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[14]:
=======
# In[41]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


=======
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
# 씽유: 마감임박
for i in range (1, 3):
    cookies = {
        '_ga': 'GA1.3.435304916.1651484551',
        'ASPSESSIONIDSQDQCSCD': 'ADPANDLCOBGKHDGDNLALNONC',
        '_gid': 'GA1.3.1060530810.1652413738',
        '_gac_UA-163306206-1': '1.1652413738.Cj0KCQjw4PKTBhD8ARIsAHChzRJK1_Tf7OMLmorQhnztqqRBAgrge2dkQDsxtH0O7wbI3pKZgkkRg0QaAlDQEALw_wcB',
        'wcs_bt': 'fff9f7a878b278:1652413738',
    }

    headers = {
        'authority': 'thinkyou.co.kr',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.3.435304916.1651484551; ASPSESSIONIDSQDQCSCD=ADPANDLCOBGKHDGDNLALNONC; _gid=GA1.3.1060530810.1652413738; _gac_UA-163306206-1=1.1652413738.Cj0KCQjw4PKTBhD8ARIsAHChzRJK1_Tf7OMLmorQhnztqqRBAgrge2dkQDsxtH0O7wbI3pKZgkkRg0QaAlDQEALw_wcB; wcs_bt=fff9f7a878b278:1652413738',
        'origin': 'https://thinkyou.co.kr',
        'referer': 'https://thinkyou.co.kr/contest/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'pageSize': '35',
        'page': str(i),
        'serstatus': '0',
        'serfield': '5,6',
        'sertarget': '0',
        'serprizeMoney': '',
        'serdivision': '',
        'seritem': '',
        'searchstr': '',
    }
    response = requests.post('https://thinkyou.co.kr/contest/ajax_contestList.asp', cookies=cookies, headers=headers, data=data)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    length = soup.select('.title > a')
    for n in range(0, len(length)):
        name, host= soup.select('.title > a')[n].text.replace('\n', '').split('주최 :')
        end_date = soup.select('.etc')[2*n].text.split('~')[-1]
        year, month, day = end_date.split('-')
        end_date = '2022. '+month+'. '+day
        links = length[n]['href']
        end_date = end_date.lstrip()
        d_date.append(end_date)
        d_title.append(name)
        d_link.append('https://thinkyou.co.kr/' + links)
    


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[15]:
=======
# In[42]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[8]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


for i in range(len(d_title)):
    li_tmp = {"title": d_title[i], "dday": d_date[i], "link": d_link[i], "분류": "대외활동"}
    gongmo.append(li_tmp)


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[16]:
=======
# In[43]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[9]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


# 씽유: 접수중
for i in range (1, 3):
    cookies = {
        '_ga': 'GA1.3.435304916.1651484551',
        'ASPSESSIONIDSQDQCSCD': 'ADPANDLCOBGKHDGDNLALNONC',
        '_gid': 'GA1.3.1060530810.1652413738',
        '_gac_UA-163306206-1': '1.1652413738.Cj0KCQjw4PKTBhD8ARIsAHChzRJK1_Tf7OMLmorQhnztqqRBAgrge2dkQDsxtH0O7wbI3pKZgkkRg0QaAlDQEALw_wcB',
        'wcs_bt': 'fff9f7a878b278:1652413738',
    }

    headers = {
        'authority': 'thinkyou.co.kr',
        'accept': 'text/html, */*; q=0.01',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_ga=GA1.3.435304916.1651484551; ASPSESSIONIDSQDQCSCD=ADPANDLCOBGKHDGDNLALNONC; _gid=GA1.3.1060530810.1652413738; _gac_UA-163306206-1=1.1652413738.Cj0KCQjw4PKTBhD8ARIsAHChzRJK1_Tf7OMLmorQhnztqqRBAgrge2dkQDsxtH0O7wbI3pKZgkkRg0QaAlDQEALw_wcB; wcs_bt=fff9f7a878b278:1652413738',
        'origin': 'https://thinkyou.co.kr',
        'referer': 'https://thinkyou.co.kr/contest/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'pageSize': '35',
        'page': str(i),
        'serstatus': '1',
        'serfield': '5,6',
        'sertarget': '0',
        'serprizeMoney': '',
        'serdivision': '',
        'seritem': '',
        'searchstr': '',
    }

    response = requests.post('https://thinkyou.co.kr/contest/ajax_contestList.asp', cookies=cookies, headers=headers, data=data)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    length = soup.select('.title > a')
    for n in range(0, len(length)):
        name, host= soup.select('.title > a')[n].text.replace('\n', '').split('주최 :')
        end_date = soup.select('.etc')[2*n].text.split('~')[-1]
        year, month, day = end_date.split('-')
        end_date = '2022. '+month+'. '+day
        links = length[n]['href']
        end_date = end_date.lstrip()
        date.append(end_date)
        title.append(name)
        link.append('https://thinkyou.co.kr/' + links)

for i in range(len(title)):
    li_tmp = {"title": title[i], "dday": date[i], "link": link[i], "분류": "대외활동"}
<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
    gongmo.append(li_tmp)


<<<<<<< HEAD:app/crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유.py
# In[17]:
=======
# In[44]:


# 대외활동 스펙토리
sp_dates = []
sp_titles = []
sp_links = []

for i in range(1, 10):
    cookies = {
        '_gid': 'GA1.2.2040960810.1652348896',
        'JSESSIONID': 'D908A4298CE46A3AFBB269C8B62299C5',
        '_gat_gtag_UA_151252983_1': '1',
        '_ga': 'GA1.2.1649544576.1651112511',
        '_ga_E0BZXCDS6N': 'GS1.1.1652515880.7.1.1652517017.0',
        '_ga_K9LXWP7RN9': 'GS1.1.1652515880.7.1.1652517017.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_gid=GA1.2.2040960810.1652348896; JSESSIONID=D908A4298CE46A3AFBB269C8B62299C5; _gat_gtag_UA_151252983_1=1; _ga=GA1.2.1649544576.1651112511; _ga_E0BZXCDS6N=GS1.1.1652515880.7.1.1652517017.0; _ga_K9LXWP7RN9=GS1.1.1652515880.7.1.1652517017.0',
        'Referer': 'http://www.spectory.net/activities?page=1&cat=%EB%8C%80%ED%95%99%EC%83%9D&prefix=info-target&searchDate=latest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        '__n': '1652517017745',
        'siteType': '대외활동',
        'categoryPrefix': 'info-target',
        'categoryName': '대학생',
        'searchDate': 'latest',
        'page': '1',
        'rows': '10',
    }

    response = requests.get('http://www.spectory.net/api/portal/contest', params=params, cookies=cookies, headers=headers, verify=False)

    html = response.text
    dict = json.loads(html)
    df = json_normalize(dict['data'])
    df = df.drop(['premium', 'created', 'modified', 'startDate', 'siteType', 'bannerImage', 'level', 'bannerEndDate', 'scrapCount', 'infoAttachementPoster'], axis=1)
    df = df[['name', 'endDate', 'contestId', 'sponsorName', 'category']]

    for i in range(0, 10):
        title = df.iloc[i][0]
        date = df.iloc[i][1]
        date = date.replace('00:00', '')
        link = df.iloc[i][2]
        link = 'http://www.spectory.net/activities/detail?pid='+str(link)+'&cat=%EB%8C%80%ED%95%99%EC%83%9D&prefix=info-target&searchDate=latest'
        sp_titles.append(title)
        sp_dates.append(date)
        sp_links.append(link)

for i in range(len(sp_titles)):
    li_tmp = {"title": sp_titles[i], "dday": sp_dates[i], "link": sp_links[i], "분류": "대외활동"}
    gongmo.append(li_tmp)


# In[66]:
=======
    gongmo.append(li_tmp)


# In[10]:


# 대외활동 스펙토리
sp_dates = []
sp_titles = []
sp_links = []

for i in range(1, 10):
    cookies = {
        '_gid': 'GA1.2.2040960810.1652348896',
        'JSESSIONID': 'D908A4298CE46A3AFBB269C8B62299C5',
        '_gat_gtag_UA_151252983_1': '1',
        '_ga': 'GA1.2.1649544576.1651112511',
        '_ga_E0BZXCDS6N': 'GS1.1.1652515880.7.1.1652517017.0',
        '_ga_K9LXWP7RN9': 'GS1.1.1652515880.7.1.1652517017.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_gid=GA1.2.2040960810.1652348896; JSESSIONID=D908A4298CE46A3AFBB269C8B62299C5; _gat_gtag_UA_151252983_1=1; _ga=GA1.2.1649544576.1651112511; _ga_E0BZXCDS6N=GS1.1.1652515880.7.1.1652517017.0; _ga_K9LXWP7RN9=GS1.1.1652515880.7.1.1652517017.0',
        'Referer': 'http://www.spectory.net/activities?page=1&cat=%EB%8C%80%ED%95%99%EC%83%9D&prefix=info-target&searchDate=latest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    params = {
        '__n': '1652517017745',
        'siteType': '대외활동',
        'categoryPrefix': 'info-target',
        'categoryName': '대학생',
        'searchDate': 'latest',
        'page': '1',
        'rows': '10',
    }

    response = requests.get('http://www.spectory.net/api/portal/contest', params=params, cookies=cookies, headers=headers, verify=False)

    html = response.text
    dict = json.loads(html)
    df = json_normalize(dict['data'])
    df = df.drop(['premium', 'created', 'modified', 'startDate', 'siteType', 'bannerImage', 'level', 'bannerEndDate', 'scrapCount', 'infoAttachementPoster'], axis=1)
    df = df[['name', 'endDate', 'contestId', 'sponsorName', 'category']]

    for i in range(0, 10):
        title = df.iloc[i][0]
        date = df.iloc[i][1]
        date = date.replace('00:00', '')
        date = str(date)
        year, month, day = date.split('-')
        date = year+'. '+month+'. '+day
        link = df.iloc[i][2]
        link = 'http://www.spectory.net/activities/detail?pid='+str(link)+'&cat=%EB%8C%80%ED%95%99%EC%83%9D&prefix=info-target&searchDate=latest'
        sp_titles.append(title)
        sp_dates.append(date)
        sp_links.append(link)

for i in range(len(sp_titles)):
    li_tmp = {"title": sp_titles[i], "dday": sp_dates[i], "link": sp_links[i], "분류": "대외활동"}
    gongmo.append(li_tmp)


# In[11]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


df = pd.DataFrame(gongmo)
df = df.drop(['tag'], axis=1)
df = df.drop_duplicates(['title'], keep='first')
# 294 -> 212 중복제거


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
# In[69]:
=======
# In[12]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


titles = []
dday = []
links = []
sort= []
gongmo_final = []

for i in range(len(df)):
        gongmo_title = df.iloc[i][0]
        gongmo_dday = df.iloc[i][1]
        gongmo_link = df.iloc[i][2]
        gongmo_sort = df.iloc[i][3]
        titles.append(gongmo_title)
        dday.append(gongmo_dday)
        links.append(gongmo_link)
        sort.append(gongmo_sort)

for i in range(len(titles)):
    li_tmp = {"title": titles[i], "dday": dday[i], "link": links[i], "분류": sort[i]}
    gongmo_final.append(li_tmp)


<<<<<<< HEAD:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
# In[70]:
>>>>>>> 437e7449bf80d877a14593fed9f8d21266e43856:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py
=======
# In[13]:
>>>>>>> upstream/test:crawl temp/crawl .py files/공모전, 대외활동 - 인크루트, 씽콘, 콘테스트_코리아, 씽유, 스펙토리.py


with open('공모전.json', 'w', encoding='UTF-8') as file:
     file.write(json.dumps(gongmo_final, ensure_ascii=False, indent="\t"))

