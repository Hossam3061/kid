try:
    import time,requests,random,os
    from colorama import Fore
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install colorama')
global x2,j
x2='[🖤] @TweakPY'
j='''
[☑️] NEW USER:︎︎
'''
def insta_checker_without_list():
    done=0
    error=0
    count=0
    user=""
    lena=input('[?] طول اليوزر: ')
    length=(int(lena))
    chars="qwertyuiopasdfghjklzxcvbnm1234567890_"
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID=use_checkers[0]
        token=use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    while True:
        time.sleep(0.9)
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        headerinsta = {
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max-age=0',
            'sec-ch-ua':'"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        send=requests.get(f'https://www.instagram.com/{user}', headers=headerinsta)
        if send.status_code==404:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
            done+=1
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            count+=1
            error+=1
def insta_checker_with_list():
    done=0
    error=0
    count=0
    file=open('user.txt', 'r')
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID = use_checkers[0]
        token = use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    while True:
        time.sleep(0.9)
        user = file.readline().split('\n')[0]
        headerinsta = {
                'accept-encoding': 'gzip, deflate, br',
                'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                'cache-control': 'max-age=0',
                'sec-ch-ua': '"Google Chrome";v="89","Chromium";v="89", ";Not A Brand";v="99"',
                'sec-ch-ua-mobile': '?0',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
            }
        send=requests.get(f'https://www.instagram.com/{user}', headers=headerinsta)
        if send.status_code == 404:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            count+=1
            done+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            count+=1
            error+=1
def telegram_with_list():
    error=0
    count=0
    done=0
    file=open('user.txt', 'r')
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID = use_checkers[0]
        token = use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    while True:
        user=file.readline().split('\n')[0]
        req=requests.get(f"https://t.me/{user}")
        if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
def telegram_without_list():
    count=0
    user=""
    done=0
    error=0
    lena=input('[?] طول اليوزر: ')
    length=(int(lena))
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID = use_checkers[0]
        token = use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    while True:
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        send=requests.get(f"https://t.me/{user}")
        if send.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"') >= 0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
def tik_checker():
    error=0
    count=0
    done=0
    lena=input('[?] طول اليوزر: ')
    length=(int(lena))
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID = use_checkers[0]
        token = use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    while True:
        time.sleep(0.9)
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        head = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'cache-control': 'max - age = 0',
            'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
            'sec-ch-ua-mobile': '?0',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
        fl=requests.get(f'https://www.tiktok.com/@{user}?', headers=head)
        if fl.status_code==404:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
def tik_checker_s():
    sess=input('[?] Type your session id :\n')
    count=0
    user=""
    ban=0
    done=0
    error=0
    lena=input('[?] طول اليوزر: ')
    length=(int(lena))
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID=use_checkers[0]
        token=use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    while True:
        time.sleep(0.9)
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        head={
            'Host': 'www.tiktok.com',
            'Cookie': f'tt_webid_v2=6965670367281858049; tt_webid=6965670367281858049; MONITOR_WEB_ID=6965670367281858049; _abck=DF7A347900A8D8FED81AFD5EE12008C7~-1~YAAQxzNWsgEVpRp6AQAAuqx6YgbdL0VIUYQFrf8WLz002DvSJRnQFKotG7hsVLkDIeQGWbs9awUK/5HLgPIbRKL7+BDefAeSzhSYx4Oaqm7EgkrAJj3nLbPWHNJ/2TNCaAoZN7KFbZgEaC0Uz5g09lsyURkNNjc811jqD0ppyZsRVY+qwcMavhooax84SMCO2aXDUbnPhrZKqCGTDvdGwoHzKXalMkOYWH+1YQAE5HNEy6AYyNT2lZ8oj1uwT8vFv0cw7jLZr6bGoX5PLe0Cl9PPTUtyTTEUrKXHenzP6GAIikG9aoeX9AX5ZB3uaZIrL5t4gshsCYlv0g9yyigqZzLq3DciTckQnxsIHMje5bbjEPGBqZWwNMMadAZmPNT34sqVkBkVBYErXRg=~-1~-1~-1; ttwid=1%7CGgSBNxhEX3SRZ-8gRwj6trJuRqBn9FTPhb-bLV09ikY%7C1625161283%7C1e8f918cc1183c04a604eee4ca979e01b09db98eb664635c2b27ffbd27e7f064; passport_csrf_token=f04fc476081a3d063b607f520e64780c; passport_csrf_token_default=f04fc476081a3d063b607f520e64780c; store-idc=alisg; store-country-code=kw; sid_guard={sess}%7C1625161275%7C21600%7CThu%2C+01-Jul-2021+23%3A41%3A15+GMT; uid_tt=8bccf5677c39c14cd37903624db85ead; uid_tt_ss=8bccf5677c39c14cd37903624db85ead; sid_tt={sess}; sessionid={sess}; sessionid_ss={sess}; odin_tt=4a561b401ba1a9af141ccfc984c3341dfef257c624d34a3255314923136ec468; R6kq3TV7=AIB1emJ6AQAAqA2c4vw_0g1Lyj9buwAoINT1GhAo7qTTopAbHG1U7J7-ofxl|1|0|48f2621a0f4379ba4258de92fd40c8b07b655c06; bm_sz=E161F9826C1159756C705283680D7689~YAAQxzNWsgAVpRp6AQAAuqx6YgznurulZT6IO07a9xHVGGYosiED9aPRNkvusXuHc2hEbYo80m5qvrh+rbt22ssX68K0cXXt0q3DjuUtFsXNR7THyFEEP2lGwZ8UV7mNm58YGrqyNYKGnbGW0mxzlG7qaotnMvFQra62p8tyPL6uUBoiwdllCfy2ojhMGv3j; tt_csrf_token=jgt9mOlWOPCOkVpJDvRHG5On; ak_bmsc=DD9CE8CF9C4F57DEBA976C40AFC52E22~000000000000000000000000000000~YAAQ3TNWskNNRw16AQAA+6wKYwwZ+E94uvHCNbWdsUwoNmX7RPgY8sstUWQdfnUozzlugFUM3SzvQ5QOLOKyF7HDtXhqv5WFZ4Pa0VhEnelbbKmzC/AtjeA58Xx5NQOIVtP7ltPSr6Ys8QWCKS1DeAl07wR9CiSyquIMIfDFtIZYgtpEBHVrYjtM22SNV+WSwhKlufzbBCGjpBvVrTcRqWopfpdnQD7csv5+rv9RV9S4Hns6mqudICKeJPANxC7WuBZlTjkW79cd9o5T7ynwqPrsmAlezu11KvXLbxB0Fmx2SNYYvCBW6ZDvENGyWPZoX4FOHpycwUZ9swvxvhOdAzMm74IDEUp7U96GcDzK0cOCt0L+pWPDCyYaD8k5Bhs2Rfnrkosy9jtD; csrf_session_id=9b74fae109614222b77b680a1d9a3b08; bm_sv=B2B3DBA971AE48D618ED54B82DB2B809~AN62layAxJK/Y32hmwfFPuZLXj6+AckUsWVAkCoH7mmp2pPbfLJRrONoTD9wwcwSJd4RAOUiJ33iMsLxIXUh8ddHyX6MQyQq8mHeBNG0dIAdHnd8A0eEUg3n0DxB5WqXjC1haBlvb/ilahGYPieZV0Hhjyp41m8ck7MPcVL0CTI=; csrf_session_id=9b74fae109614222b77b680a1d9a3b08; s_v_web_id=verify_kql72dl5_iIpBKz5B_ZP5g_40oV_8MvL_hE4c6TTp0S5R',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Upgrade-Insecure-Requests': '1',
            'Te': 'trailers',
            'Connection': 'close', }
        req=requests.get(f'https://www.tiktok.com/@{user}?lang=ar', headers=head)
        if req.text.find('<p class="jsx-3565499374 title">تعذر العثور على هذا الحساب</p>') >= 0:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}حظر <{ban}> | تم فحص <{count}> {Fore.RESET} ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        elif req.text.find('<span class="jsx-714557759">تم الإعجاب</span>') >= 2:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}حظر <{ban}> | تم فحص <{count}> {Fore.RESET} ',end='')
            error+=1
            count+=1
        elif req.text=='':
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}حظر <{ban}> | تم فحص <{count}> {Fore.RESET} ',end='')
            ban+=1
            count+=1
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}حظر <{ban}> | تم فحص <{count}> {Fore.RESET} ',end='')
            error+=1
            count+=1
def snap_with_list():
    error=0
    count=0
    done=0
    file=open("user.txt", 'r')
    try:
        use_checkers = open('id_token.txt', "r").read().splitlines()
        ID = use_checkers[0]
        token = use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    while True:
        user=file.readline().split('\n')[0]
        head={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '57',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
            'origin': 'https://accounts.snapchat.com',
            'referer': 'https://accounts.snapchat.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
        data={
            'requested_username': user,
            'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
        req = requests.post(f'https://accounts.snapchat.com/accounts/get_username_suggestions',data=data,headers=head).text
        if '"status_code":"OK"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        elif '"status_code":"TAKEN"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_BEGIN"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_END"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"DELETED"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_SEPARATED"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
def snap_without_list():
    error=0
    count=0
    done=0
    lena=input('[?] طول اليوزر: ')
    length=(int(lena))
    try:
        use_checkers=open('id_token.txt', "r").read().splitlines()
        ID=use_checkers[0]
        token=use_checkers[1]
    except:
        pass
        print('[!] شغل رقم 5 لو تبي ينرسل لك صيد علبوت لو ماتبي ترا تومتيك الان بتشتغل الاداه')
    chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
    while True:
        time.sleep(0.9)
        for user in range(1):
            user = ""
            for item in range(length):
                user += random.choice(chars)
        head={
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US,en;q=0.9',
            'content-length': '57',
            'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
            'cookie': 'xsrf_token=qguFhKiP7FrimtibnGvopQ; web_client_id=6dee3ce3-db42-4fd0-b538-682cdb294f9a; _scid=482919d7-1390-46c8-8951-d3031e352b63; _sca={%22cid%22:%22e22c1577-7f73-4b69-85ff-79b72444951a%22%2C%22token%22:%22v1.key.2020-03-05_UKiB4eNE.iv.MeUzIJboKx7l+nZu.zf9r/dgUl/1vg1iBp4fz27qapzxGL1VJowr9Clna1AvHYCTUocABFHpeSMdPC2BGmfDmAfrA8eEqFPnV5qNP/QJCPISHEUpj7aGeYGpoggjapYZZ%22}; sc-cookies-accepted=true; Preferences=true; Performance=true; Marketing=true; _ga=GA1.2.148694331.1613677502; _gid=GA1.2.1609447525.1613677502; _gat_UA-41740027-4=1',
            'origin': 'https://accounts.snapchat.com',
            'referer': 'https://accounts.snapchat.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'same-origin',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36'}
        data={
            'requested_username': user,
            'xsrf_token': 'qguFhKiP7FrimtibnGvopQ'}
        req=requests.post(f'https://accounts.snapchat.com/accounts/get_username_suggestions', data=data, headers=head).text
        if '"status_code":"OK"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            done+=1
            count+=1
            try:
                requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {user}\n\n{x2}')
            except:
                pass
            with open('Available.txt', 'a') as x:
                tl = '[] NEW USER -->  '
                x.write(tl + user + '\n')
        elif '"status_code":"TAKEN"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_BEGIN"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_END"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"DELETED"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        elif '"status_code":"INVALID_SEPARATED"' in req:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
        else:
            print(f'\r[{Fore.MAGENTA}${Fore.RESET}] {Fore.GREEN}متاح  <{done}>{Fore.RESET} | {Fore.RED}غير متاح <{error}>{Fore.RESET} | {Fore.LIGHTYELLOW_EX}تم فحص <{count}> {Fore.RESET}  ',end='')
            error+=1
            count+=1
#############################
print(f"{Fore.RED}author:@Filza2\tchannel:@TweakPY Free Tool Not for sell{Fore.RESET}")
choose=int(input(f"""
1) - تشيكرات تيك توك
2) - تشيكرات تلقرام
3) - تشيكرات انستقرام
4) - تشيكرات سناب شات
5) - حفظ الايدي والتوكن
----------------------------------------------------------------------------
\n> """))
if choose==1:
    tiktokchoose=int(input("""
    1-تشيكر تيك بدون سيشن
    2-تشيكر تيك بسيشن
    """))
    if tiktokchoose==1:
        tik_checker()
    elif tiktokchoose==2:
        tik_checker_s()
elif choose==2:
    choose6 = int(input(f"""
        1) تشيكر تلقرام انت تجيب ملف اليوزرات
        2) تشيكر تلقرام الاداه تسوي يوزرات
        """))
    if choose6 == 1:
        telegram_with_list()
    elif choose6 == 2:
        telegram_without_list()
    else:
        exit('@TweakPY')
elif choose==3:
    choose7 = int(input(f"""
        1) تشيكر انستا انت تجيب ملف اليوزرات
        2) تشيكر سناب الاداه تسوي يوزرات
        """))
    if choose7 == 1:
        insta_checker_with_list()
    elif choose7 == 2:
        insta_checker_without_list()
    else:
        exit('@TweakPY')
elif choose==4:
    choose0 = int(input(f"""
        1) تشيكر سناب انت تجيب ملف اليوزرات
        2) تشيكر سناب الاداه تسوي يوزرات
        """))
    if choose0==1:
        snap_with_list()
    elif choose0==2:
        snap_without_list()
elif choose==5:
    ID = input("ايديك على تلقرام ->: ")
    token = input("توكن بوتك ->: ")
    with open('id_token.txt', 'a') as x:
        x.write(ID + "\n" + token)
    print(f"ID: {ID}\nTOKEN: {token}")
else:
    exit("@TweakPY")
