import requests,random,threading,time
import sys as n
import time as mm
from instabot import Bot
b = Bot
r=requests.session()
print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 15)
print("""
██╗   ██╗██╗███████╗██╗    ██╗███████╗ 
██║   ██║██║██╔════╝██║    ██║██╔════╝  V3
██║   ██║██║█████╗  ██║ █╗ ██║███████╗
╚██╗ ██╔╝██║██╔══╝  ██║███╗██║╚════██║
 ╚████╔╝ ██║███████╗╚███╔███╔╝███████║
  ╚═══╝  ╚═╝╚══════╝ ╚══╝╚══╝ ╚══════╝""")
slow('        By JOKER AND Mustafa ')
slow('Mode:\n  [1] Get proxy   |  [2] Increase views')
print(' ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n')
joker = input('Enter mode : ')
time.sleep(1)


def vv1ck():
	global POST
	proxy =  open("proxy.txt",'r').read().splitlines()
	url = 'https://sifresiz.instahile.co/c/views.php'
	while True:
		proxylist = []
		for pro in proxy:
			proxylist.append(pro)
			run = str(random.choice(proxylist))
		try:
			PROXY = {"https":run,"http":run}
			headers = {
				'Accept': 'application/json, text/javascript, */*; q=0.01',
				'Accept-Encoding': 'gzip, deflate, br',
				'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
				'Connection': 'keep-alive',
				'Content-Length': '51',
				'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
				'Cookie': '_ga=GA1.2.271938960.1616745818; fpestid=gqkv1zcX8UGM99qMA2oo8i07PS52924eUQ0fwurHjbnm3NiZ02QYsjTZ3hg1rCSzaEtM-Q; _gid=GA1.2.168553159.1617169241; _gat_gtag_UA_129054916_2=1',
				'Host': 'sifresiz.instahile.co',
				'Origin': 'https://sifresiz.instahile.co',
				'Referer': 'https://sifresiz.instahile.co/views',
				'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
				'sec-ch-ua-mobile': '?0',
				'Sec-Fetch-Dest': 'empty',
				'Sec-Fetch-Mode': 'cors',
				'Sec-Fetch-Site': 'same-origin',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
				'X-Requested-With': 'XMLHttpRequest'}
			data={
				'media_id': f'{POST}_2872859990',
				'quantity': '10'}
			j=r.post(url,headers=headers,data=data,proxies=PROXY).text
			if '"sent":5' in j:
				print('[$]>> 5 views posted ')
			
			elif '"sent":4' in j:
				print('[$]>> 4 views posted ')
			
			elif '"sent":3' in j:
				print('[$]>> 3 views posted ') 
			
			elif '"sent":2' in j:
				print('[$]>> 2 views posted ')
			
			elif '"sent":1' in j:
				print('[$]>> 1 views posted ')
			
			else:
				print('Error 404 { bad proxy } !')
			
		except requests.exceptions.ConnectionError:
			pass
		except KeyboardInterrupt:
			exit()

def tret():
	global POST
	POSe = input(' [+] Enter url post : ')
	POST = b.get_media_id_from_link(self='',link=POSe)
	theards =[]
	for i in range(320):
		th1 = threading.Thread(target=vv1ck)
		th1.start()
		theards.append(th1)
	for th2 in theards:
		th2.join()

def Proxy():
	url = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt'
	headers = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'if-none-match': 'W/"11cd2e7c01d9ff7aa4333364a5b0e80aeb825b0641fa17e4e5980b32bdf7be6d"',
		'referer': 'https://github.com/ShiftyTR/Proxy-List/blob/master/https.txt',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'cross-site',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
	re = requests.get(url,headers=headers).text
	
	url_2 = 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt'
	headers_2 = {
		'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
		'accept-encoding': 'gzip, deflate, br',
		'accept-language': 'en-US,en;q=0.9',
		'referer': 'https://github.com/ShiftyTR/Proxy-List/blob/master/http.txt',
		'sec-ch-ua': '"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"',
		'sec-ch-ua-mobile': '?0',
		'sec-fetch-dest': 'document',
		'sec-fetch-mode': 'navigate',
		'sec-fetch-site': 'cross-site',
		'sec-fetch-user': '?1',
		'upgrade-insecure-requests': '1',
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'}
	re_2 = requests.get(url_2,headers=headers_2).text
	with open('proxy.txt','w') as file:
		file.write(re + re_2)
		print('[+] Done...✅')
		print('[+] Proxy list added to file : proxy.txt')
		print('By @EDISONpy')
		exit()

if joker=='1':
	Proxy()
elif joker=='2':
	tret()
else:
	print('\n good bye By @vv1ck and @tweakjailbreak')
	exit()
