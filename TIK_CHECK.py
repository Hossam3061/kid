import requests , random
req = requests.session()
####################################################
#Rights:                                           #
#DEV:Filza_507                                     #
#CH:TweakPY                                        #
####################################################
print("---------------------------------------------")
print("Enter num for the user")
sos=int(input(">> "))
def start():
    while True:
        letters = 'qwertyuiopasdfghjklzxcvbnm1234567890._'
        amount = int(1)
        length = int(sos)
        for password in range(amount):
            password = ''
            for item in range(length):
                password = ''
            for item in range(length):
                password += random.choice(letters)
            hi = list(password)
            if hi[0] == '.':
                pass
            else:
                def tiktok():
                    x2 = '[🖤] @TweakPY - @Filza5'
                    j = '''
                    [☑️] TIKTOK USER:︎︎
                    '''
                    killout = open('id_token.txt', "r").read().splitlines()
                    idd = killout[0]
                    token = killout[1]
                    urltik = f'https://www.tiktok.com/@{password}?'
                    headertik = {
                        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        'accept-encoding': 'gzip, deflate, br',
                        'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
                        'cache-control': 'max - age = 0',
                        'sec-ch-ua': '"Google Chrome";v = "89", "Chromium";v = "89", ";Not A Brand";v = "99"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-fetch-dest': 'document',
                        'sec-fetch-mode': 'navigate',
                        'sec-fetch-site': 'none',
                        'sec-fetch-user': '?1',
                        'upgrade-insecure-requests': '1',
                        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
                    }
                    send = req.get(urltik, headers=headertik)
                    if send.status_code == 404:
                        global tik
                        tik = 'Available'
                        tele = (f'https://api.telegram.org/bot{token}/sendMessage?chat_id={idd}&text={j}\n𖡃 𝚄𝚂𝙴𝚁: {password}\n\n{x2}')
                        re = requests.post(tele)
                        with open('./Tiktok.txt', 'a') as Available:
                            Available.write(password +'\n')
                    else:
                        tik = 'Not Available'
                tiktok()
                soss = 'TweakPY'
                print(f'[{soss}]<>[{tik}] [{password}]')
start()
