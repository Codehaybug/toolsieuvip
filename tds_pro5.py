
do = "\033[1;91m"
xanhbien = "\033[1;36m"
vang = "\033[0;33m"
hong = "\033[1;35m"
xanhduong = "\033[1;34m"
xanhla = "\033[1;32m"
xanh="\033[1;32m"
cam="\033[1;33m"
blue="\033[1;34m"
lam="\033[1;34m"
tim="\033[1;34m"
syan="\033[1;36m"
xnhac= "\033[1;96m"
den="\033[1;90m"
luc="\033[1;92m"
xduong="\033[1;94m"
trang="\033[1;97m"
xanhnhat = "\033[1;36m"
trang1 = "\033[1;37m"
#####################
den = "\033[0;30m"
trang = "\033[0;37m"
do = "\033[0;31m"
xanh_la = "\033[0;32m"
nau = "\033[0;33m"
xanh_duong = "\033[0;34m"
tim = "\033[0;35m"
xanh_ngoc = "\033[0;36m"
xam_nhat = "\033[0;37m"
xam_dam = "\033[1;30m"
do_nhat = "\033[1;31m"
xanh_la_nhat = "\033[1;32m"
vang = "\033[1;33m"
xanh_duong_nhat = "\033[1;34m"
tim_nhat = "\033[1;35m"
hong  = "\033[95m"
xanh_ngoc_nhat = "\033[1;36m"
trang_nhat = "\033[1;37m"
#####[THƯ VIỆN]#######
import os, sys
try:
	import requests, json, re, random
except:
	os.system("pip install requests")
	import requests, json, re, random
from random import randint
from time import sleep
from pystyle import Colors, Colorate
from pystyle import *
import base64
from datetime import datetime
import requests,os,sys, time
import uuid, binascii, codecs
###################################
try:
    apiServer = requests.get("https://ducthinhexe.github.io/")
    if "admin" in apiServer.text:
        __ADMIN__   = apiServer.json()["admin"]
        verison = apiServer.json()["verison"]
        fullName = apiServer.json()['data']['fullName']
        facebook = apiServer.json()['data']['Facebook']
        zalo     = apiServer.json()['data']['Zalo']
        boxzalo  = apiServer.json()['data']['BoxZalo']
        thuekey  = apiServer.json()['data']['thuekey']
    else:
        msg = apiServer.text.upper().replace('\n','')
        print(f"{do}Server Đang {vang}{msg} {do}!")
        exit()
except Exception as e:
    print(f"{do}Đã Có Lỗi Xảy Ra, Vui Lòng Inbox Zalo : {xanh_duong_nhat}0923.932.075{do} - LỖI : {vang}{e}")
    exit()
####[LOGO]#####
import binascii, codecs, base64
class KeyTool:
	def __init__(self):
		dateTime = datetime.now().strftime("%d%m%Y")
		getIP = requests.get("https://ipinfo.io/json").json()
		self.ipGoc = getIP['ip']
		self.region = getIP['region']
		self.ip = self.ipGoc.replace('.', '')
		Realkey1 = f"Jiray-{self.region}-{dateTime}-{int(self.ip) + 262482006}"
		Realkey = Realkey1[::-1]
		self.key = base64.b64encode(Realkey.encode()).decode('utf-8')[:8]
		self.notification = '\n'.join([f"{vang}[{trang}<{xanh_la}/{trang}>{vang}] {xanh_la}{line}" for line in requests.get("https://jirayshop.xyz/keytool/notification.php").text.splitlines()])

	
	@property
	def BannerKey(self):
		self.Clear
		urlKey = requests.get(f'https://jirayshop.xyz/keytool/tao.php?ip={self.ip}&region={self.region}').json()['url']
		logo = f"""             {xanh_la_nhat}██╗██╗██████╗  █████╗ ██╗   ██╗
             {xanh_duong_nhat}██║██║██╔══██╗██╔══██╗ ██╗ ██╔╝
             {xanh_la_nhat}██║██║██████╔╝███████║ ╚████╔╝ 
        {xanh_duong_nhat}██╗  ██║██║██╔══██╗██╔══██║  ╚██╔╝  
        {xanh_la_nhat}╚█████╔╝██║██║  ██║██║  ██║   ██║   
         {xanh_duong_nhat}╚════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
{trang} Copyright {xanh_la}@DucThinhEXE - Jiray {trang}| Verirson : {xanh_la}{verison}
{trang_nhat}═════════════════════════════════════════════════════
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Facebook        {do_nhat}: {vang}{facebook}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Youtube         {do_nhat}: {tim_nhat}https://youtube.com/@JirayIsMe{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Thuê Key        {do_nhat}: {xanh_duong_nhat}{thuekey}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Zalo            {do_nhat}: {xanh_la_nhat}{zalo}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Box Telegram    {do_nhat}: {do_nhat}{boxzalo}{trang_nhat}
{trang_nhat}═════════════════════════════════════════════════════
{trang_nhat}{self.notification}{trang_nhat}
{trang_nhat}════════════════════ \033[95mLINK KEY {trang_nhat}═══════════════════════
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Link Lấy Key {do_nhat}: \033[1;33m{urlKey}{trang_nhat}
═════════════════════════════════════════════════════
"""
		for _ in logo:
			sys.stdout.write(_)
			sys.stdout.flush()
			time.sleep(random.uniform(0.00125, 0.00025))
	
	@property
	def InputKey(self):
		keyTool = input(f"{xanh_ngoc_nhat}Nhập Key Ngày Hôm Nay ( Nếu Key Phí Thì Không Cần Vượt ) : {trang_nhat}")
		return keyTool
	
	def Convert2Check(self, key):
		if len(key) > 3:
			encKey = key[::-1]
			decoded_hex_bytes = binascii.unhexlify(encKey)
			decoded_rot13 = codecs.decode(decoded_hex_bytes.decode('utf-8'), 'rot_13')
			return decoded_rot13
		else:
			return False
	def Logo(self, key, date):
		self.Clear
		logo = f"""             {xanh_la_nhat}██╗██╗██████╗  █████╗ ██╗   ██╗
             {xanh_duong_nhat}██║██║██╔══██╗██╔══██╗ ██╗ ██╔╝
             {xanh_la_nhat}██║██║██████╔╝███████║ ╚████╔╝ 
        {xanh_duong_nhat}██╗  ██║██║██╔══██╗██╔══██║  ╚██╔╝  
        {xanh_la_nhat}╚█████╔╝██║██║  ██║██║  ██║   ██║   
         {xanh_duong_nhat}╚════╝ ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝
{trang} Copyright {xanh_la}@DucThinhEXE - Jiray {trang}| Verirson : {xanh_la}{verison}
{trang_nhat}═════════════════════════════════════════════════════
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Facebook        {do_nhat}: {vang}{facebook}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Youtube         {do_nhat}: {tim_nhat}https://youtube.com/@JirayIsMe{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Thuê Key        {do_nhat}: {xanh_duong_nhat}{thuekey}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Zalo            {do_nhat}: {xanh_la_nhat}{zalo}{vang}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Box Telegram    {do_nhat}: {do_nhat}{boxzalo}{trang_nhat}
{trang_nhat}═════════════════════════════════════════════════════
{trang_nhat}{self.notification}{trang_nhat}
{trang_nhat}════════════════════ \033[95mINFO MEMBER {trang_nhat}══════════════════════
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}IP  : {vang}{self.ipGoc}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Key : {vang}{'*' * int(len(key) - 2)+ key[int(len(key) - 2):]}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Expiration date : {vang}{date}{trang_nhat}
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Trao Đổi Sub Facebook Pro5{trang_nhat}
══════════════════════════════════════════════════════
"""
		for _ in logo:
			sys.stdout.write(_)
			sys.stdout.flush()
			time.sleep(random.uniform(0.00125, 0.00025))

	@property
	def Clear(self):
		os.system('cls' if os.name == "nt" else "clear")
	
	@property
	def CheckKey(self):
		try:
			file = open("JirayKeyTool.txt", 'r')
			file.close()
		except:
			file = open("JirayKeyTool.txt", "w")
			file.write(self.ipGoc)
			file.close()
		with open("JirayKeyTool.txt", "r") as fKey:
			keyOld = fKey.read().strip()
		checkVip = requests.post(f"https://jirayshop.xyz/api/check_key.php", json={'key':keyOld})
		if 'true' in checkVip.text:
			key		  	  = keyOld
			Encdate 	  = checkVip.headers['Id-Requests']
			thinhvip      = self.Convert2Check(Encdate)
			if thinhvip == False:
				return False, f"{do}Key Không Tồn Tại Hoặc Đã Hết Hạn!"
			else:
				keyRS, date = thinhvip.split('-')[0], thinhvip.split('-')[1]
				if keyRS != key:return False, f"{do}Key Không Tồn Tại Hoặc Đã Hết Hạn!"
				else:return True, keyRS, date
		else:
			if keyOld != self.key:
				return False, f"{do}Key Không Tồn Tại Hoặc Đã Hết Hạn!"
			else:
				with open("JirayKeyTool.txt", "w") as fKey:
					fKey.write(self.key)
					return True, self.key, str(datetime.now().strftime("%d/%m/%Y"))
t = KeyTool()
t.Clear
checkKey = t.CheckKey
if checkKey[0] == False:
	t.BannerKey
	while True:
		keyInput = t.InputKey
		with open("JirayKeyTool.txt", "w") as fKey:
			fKey.write(keyInput)
		check = t.CheckKey
		if check[0] == False:
			msg = check[1]
			print(msg)
			time.sleep(1.2)
		else:
			key = check[1]
			date = check[2]
			print(f'{trang_nhat}Chào Mừng Bạn Đến Với {vang}JIRAYTOOL {trang_nhat}!')
			break
else:
	key = checkKey[1]
	date = checkKey[2]

############## FUNCTION #################
def banner():
    t.Logo(key, date)
banner()
######[DEF AUTO]########
def echo(text):
	for i in range(len(text)):
		sys.stdout.write(text[i])
		sys.stdout.flush()
		sleep(0)
	print()
def khang(khang):
   echo('═══════════════════════════════════════════════════════')
def clear():
	if os.name=='nt':os.system('cls')
	else:os.system('clear')
def idelay(delaymin, delaymax):
    delay = randint(delaymin, delaymax)
    while delay > 0:
        print(f"{vang}[{xanh_la}<{xanh_duong_nhat}DUCTHINHEXE{xanh_la}>{vang}]{vang}[{trang}{delay}{vang}]                                                                      ", end='\r')
        sleep(1)
        delay-=1
def idelayblock(delay):
    while delay > 0:
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [.....]														", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [•....]														", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [••...]														", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [•••..]														", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [••••.]														", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {xanh_la}{delay} [•••••]														", end='\r')
        print(' '*50,end='\r')
        sleep(1/6)
        delay -= 1
def LoadJob(delay):
	for demtg in range(int(delay), -1, -1):
		print(trang+"Làm Nhiệm Vụ Tiếp Theo Sau: "+str(demtg), end="     										\r")
		sleep(0.8)
def jsoncookie(cookies):
    result = {}
    try:
        for i in cookies.split(';'):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result
    except(Exception,):
        for i in cookies.split('; '):
            result.update({i.split('=')[0]: i.split('=')[1]})
        return result
def GETID(cookie):
	try:
		head = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1366',}
		url = requests.get("https://www.facebook.com/me", headers=head, cookies=cookie).url
		get = requests.get(url, headers=head, cookies=cookie).text
		fb = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
		jazoest = get.split('jazoest=')[1].split('"')[0]
		data = {
		'fb_dtsg' :fb,
		'jazoest' :jazoest,
		'variables' : '{"showUpdatedLaunchpointRedesign":true,"useAdminedPagesForActingAccount":false,"useNewPagesYouManage":true}',
		'doc_id' : '5300338636681652'
		}
		get = requests.post("https://www.facebook.com/api/graphql/", headers=head, cookies=cookie, data=data).json()
		return get['data']['viewer']['actor']['profile_switcher_eligible_profiles']['nodes']
	except:
		exit(f"{do}Cookie Die!")
class Facebook:
	def __init__ (self, cookie) -> None:
		self.cookie = jsoncookie(cookie)
		self.head = {'authority': 'www.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','accept-language': 'vi','sec-ch-prefers-color-scheme': 'light','sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'none','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36','viewport-width': '1366',}
		self.user_id = cookie.split("i_user=")[1].split(";")[0]
		url = requests.get("https://www.facebook.com/me", headers=self.head, cookies=self.cookie).url
		get = requests.get(url, headers=self.head, cookies=self.cookie).text
		self.fb = get.split('["DTSGInitialData",[],{"token":"')[1].split('"')[0]
		self.jazoest = get.split('jazoest=')[1].split('"')[0]
		self.lsd = get.split('["LSD",[],{"token":"')[1].split('"')[0]
	def infocookie(self):
		get = requests.get(f"https://www.facebook.com/{self.user_id}").text
		try:
			name = get.split('<title>')[1].split('</title>')[0]
			return {"success":200,"name":name, "id":self.user_id}
		except:
			return {"error":200}
	def CamXuc(self, id, type):
		url = requests.get("https://www.facebook.com/"+id, headers=self.head, cookies=self.cookie).url
		get = requests.get(url, headers=self.head, cookies=self.cookie).text
		feedback = base64.b64encode(f"feedback:{id}".encode('utf-8')).decode('utf-8')
		trackingdata = "AZUWSff9IbOm7WYclNQ8Rdp3OiHQE93bPuGbIeTR-oR1dbegBG8_sAyrLAGv-lgtY5fJC2-VkDf3ET6NmkBl2ei3nAQfEtQb_Q-EWXdqExUrA4BwTdTja6w0IPHUbxfaakMAnDkPuc_d4-wxEGvRR4yYcw-AxqgxSCgyy76QJEjmMe8TtO-wLkbErMHEfWIlOEBEXX032c_5DMP5jLUoF-raGeDOZjSfNFqDPjiHOLCIF44pMODEmPwymgh40ypXG549DZslL_8NBXk-GNJDk-ozcClD4DfwyldPBYia1nv416ZD1EOM3cXeSgCQxZw5iATdTAlyxdX4CohdPNTf0Tl4XlREHJ7wFa8Q3HWwJstV4lLO3NMthPCQD6WA2aMvzh7XqVU42HOWhaoZWOmTu8XKjrcFTwimPHwuSJSaaSompUxYVEF8wwKBE5f0Wxhznp2gqXM_ff5kLmlBMpl4ZKJ7V5krGl37ToKFjBROyv0IXN7DQ1nRaa3uSLGMd1dPAi8fMjeBLUcuJKIgWulqx-J_H1foC8bFNxYqYA802aqGdhauF1CPLlO1fKWCayresorODNgLx_VolhhjfK34oiW2O1fgVqZCtYH8YaGeUY5_MvrCosOVyaNwDa0jrswco8tW0hNA_7q7HdqC6CoPS3RWJExFJr4O7NShfL5asubUpdkwncHHCJH4jGwCDfaWMhuYOHKt-ozn9NOllhj5bzYS4vPuctZddFTnRnUZXEV6TuGhP97B4fBoSsF3din7G8ix7GyF-OGs9KqxzH0gVHGb34m_yoV09a7E7a3BEhTZ3tCzan1qc_b25VFQy5uAjQLwuRvjA3n12AvhSF_QnRGeiPO6ixTQr58fV3irNNl692WWpK10FKkH18nZzyRfDPFKEbjuVD2443GxrLKrAvfaWKYqHvrb72dAkyndzms10x79Z723DE6olaGQD_Ck5DBnhDZvGE0AwmI22GWXrv1Fv1ukoubed0_fe3Du7eQXxL9CJXgWdu0hy-ycqeHXW5jnuyKBvtLp8JnOGrWJF_FBnwkAC2sBECkSN2Rx8F8f0BtHMLn1aQcYW5Ji7EyGS2WXAf86ejs5XI5TX5_7KBf8qDg2Ys5cCKjv90H66_9pUGcWI9cbvFAt6Y_VlksehEkJHJSX3hJVnTsxQNIukfQomAFQhDYpxVvl6XcWpN68--v5Oq2j25hSX_EEnORiUHFlYf6dzs5ZYzKXkEj7Rpsii3_ZT5MoOu53Pz2ubzFGr6fG4OmxfXI1qnjzVBTofiQFBJjZ7YTUDK6MF9v-wTf0"
		if type == "LIKE":id = "1635855486666999"
		if type == "LOVE":id = "1678524932434102"
		if type == "CARE":id = "613557422527858"
		if type == "HAHA":id = "115940658764963"
		if type == "WOW":id = "478547315650144"
		if type == "SAD":id = "908563459236466"
		if type == "ANGRY":id = "444813342392137"
		data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wFwhUngS3q32360CEboG4E762S1DwUx60GE3Qwb-q7oc81xoswMwto88422y11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61axe3S7Udo5qfK0zEkxe2GewGwkUtxGm2SUbElxm3y11xfxmu3W3y261eBx_y88E3VBwJCwLyES0Io88cA0z8c84qifxe3u364UrwFg662S269wkoqw","__csr" : "g9Q9OOhthsIBFPQYFzQyOtvFsy4TFsyRozTsGGHN9k8W8ObECQD4QParJ4Iz8yp6A_AKlAKUKjuh5BBBVfUx3Z7AFABGl5LvKmK9yCF8xeaVAex14gGAXQ8DyKV8hyE9F8XCAyQECqcg94EgzUdGKmELCCCxycxuUfEKbwwwjEhG2JojgcobE8VEdoc8pxa9zoWfwgoC9wUw9i1awdW0G84K49UaUhwtoiwdu1sw8KUdE11o0cVU0Iq03vm00Id80qKG3-0tW0hq02Kd0ee07qi2E0hmwoU0j_w0CCw1We0Hpo1ao0x69w1jO3u0W817UgwfC2a","__req" : "l","__hs" : "19438.HYP:comet_pkg.2.1..2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007150578","__s" : "ajoats:subbv5:fs4kwq","__hsi" : "7213197347307427052","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : "25611","lsd" : self.lsd,"__aaid" : "710580363942837","__spin_r" : "1007150578","__spin_b" : "trunk","__spin_t" : "1679453381","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometUFIFeedbackReactMutation",'variables' : '{"input":{"attribution_id_v2":"CometGroupPermalinkRoot.react,comet.group.permalink,via_cold_start,1679453388936,459905,2361831622,","feedback_id":"'+feedback+'","feedback_reaction_id":"'+id+'","feedback_source":"OBJECT","is_tracking_encrypted":true,"tracking":["'+trackingdata+'"],"session_id":"12845410-1d81-40bd-95d0-ccd042ba90eb","actor_id":"'+self.user_id+'","client_mutation_id":"3"},"useDefaultActor":false,"scale":2}','server_timestamps' : 'true',"doc_id" : "5703418209680126"}
		get = requests.post("https://www.facebook.com/api/graphql/", headers=self.head, cookies=self.cookie, data=data)
		return get
	def likepage(self, id):
		data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHxqU5a5Q1ryUbFuC0BVU98nwgUao5-ewSwMwNw9G2S7o762S1DwUx60p-0LVEtwMw65xO0FE886C11xmfz83WwgEcEhwGxu782lwv89kbxS2218wc61uwZx-3m1mzXw8W58jwGzEaE766FobrwKxm5o7G4-5pUfEe872m7-8wywfCm2Sq2-azo2NwwwOg2cwMwhF8-4UdUcojxK2B0oobo8oC1hxG","__csr" : "g94hqPtB5JRh9lQAAAAQZimKRluh99CF4_WmZDmLqrB8Z29oKVGKQmbKrBBWBgCqmrx24WVUux6Ex0Ex2aBz9UC4U4O3C15xCdwsUhxa2WbwhUeE4Kby-0lfwam0q-00oQGA0haySJiKHg8UhwgogwEw","__req" : "o","__hs" : "19422.HYP:comet_pkg.2.0.0.2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007055511","__s" : "adfco7:2ievkh:x4z7bk","__hsi" : "7207283130392575182","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : self.jazoest,"lsd" : self.lsd,"__aaid" : "710580363942837","__spin_r" : "1007055511","__spin_b" : "trunk","__spin_t" : "1678076370","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometProfilePlusLikeMutation",'variables' : '{"input":{"page_id":"'+id+'","source":null,"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}',"server_timestamps" : "true","doc_id" : "4867271226642619"}
		get = requests.post("https://www.facebook.com/api/graphql/", headers=self.head, data=data, cookies=self.cookie)
		return get
	def group(self, id):
		data = {'av':self.user_id,'__user':self.user_id,'__a':'1','__dyn':'7AzHJ16U9ob8ng5K8G6EjBWo2nDwAxu13wsongS3q2ibwyzE2qwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO321Rwwwg8a8465o-cwfG12wOKdwGxu782lwv89kbxS2218wc61axe3S1lwlE-U2exi4UaEW2G1jxS6FobrwKxm5oe8464-5pUfEe88o4Wm7-8xmcwfCm2CVEbUGdG1Fwh888cA0z8c84qifxe3u364UrwFg662S26','__csr':'gadNAIYllhsKOE8IpidFPhcIx34Omy9-O9OO8hZ_8-kAymHGAybJqGlvmWl7nWBWJ7GqaXHz7GFe9oy_KBl7h6h4KVah94QeKVHACDyryqKdF5GuXXBCgNpbJ5jjGm8yQEWrCixl6xWuiih5yo-8wAy84mq4poN0Vzbxe16whAufgO5U8UKi4Eyu4EjwGK78527o8411wgocU5u1MwSwFyU8Uf8igaElw8e9xK2GewNgy5o5m1nDwLwrokm16www8G03cy0arw0Zyw0aaC0mG0eJzl8ow2Jw6tw44w4uzo045W1UgSeg0z-07X81-E0cNo0By1Wwi8fE0lYw2h81a8gw9u','__req':'k','__hs':'19363.HYP:comet_pkg.2.1.0.2.1','dpr':'2','__ccg':'EXCELLENT','__rev':'1006794317','__s':'gtlvj8:fxbzro:f2kk19','__hsi':'7185658639628512803','__comet_req':'15','fb_dtsg':self.fb,'jazoest':self.jazoest,'lsd':'gKT7R4dxIBjI4wUDUP5ivT','__aaid':'1576489885859472','__spin_r':'1006794317','__spin_b':'trunk','__spin_t':'1673041526','fb_api_caller_class':'RelayModern','fb_api_req_friendly_name':'GroupCometJoinForumMutation','variables':'{"feedType":"DISCUSSION","groupID":"'+id+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUP_MALL","attribution_id_v2":"CometGroupDiscussionRoot.react,comet.group,via_cold_start,1673041528761,114928,2361831622,","group_id":"'+id+'","group_share_tracking_params":{"app_id":"2220391788200892","exp_id":"null","is_from_share":false},"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":true,"scale":2,"source":"GROUP_MALL","renderLocation":"group_mall","__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true,"__relay_internal__pv__GlobalPanelEnabledrelayprovider":false}','server_timestamps':'true','doc_id':'5853134681430324','fb_api_analytics_tags':'["qpl_active_flow_ids=431626709"]',}
		join = requests.post('https://www.facebook.com/api/graphql/',headers=self.head, cookies=self.cookie, data=data)
		return join
	def follow(self, id):
		data = {"av" : self.user_id,"__user" : self.user_id,"__a" : "1","__dyn" : "7AzHJ16UW5Eb8ng5K8G6EjBWobVo66u2i5U4e2C17xt3odEnz8K361twYwJyEiwsobo6u3y4o2Gwfi0LVEtwMw65xO2OU7m2210wEwgolzUO0-E4a3a4oaEnxO0Bo7O2l2Utwwwi831wiEjwZx-3m1mzXw8W58jwGzE8FU5e7oqBwJK2W5olwUwgojUlDw-wUwxwjFovUy2a0SEuBwJCwLyES0Io88cA0z8c84qifxe3u364UrwFg662S269wkoqw","__csr" : "grl2YAW3lsBl4neziQkJhtlXNlFTsWEPsAGlkGjq8gygPqAmKoIBaQBLSWHQlpHpiHQG9QFeYyhWyFVq-iKKi8x2fKiFFFKWzpkiGDihVayCcQngjmmuFbzpUOWgpzEvy8WuueVkVUjKUC4WxmbyebzVE9oyt0xwDK4GxKUF6xOu4UWUu-EaosK7E4S3eEfE8Q58kxaHw_y8WUK9Bwfi8wCwiUhwTxqawam2G5Uc8yewFxW2t0s89Umgowue7awRwg8c80dp80Ka06980mow0b6aE0C648iO04vw10-0b9Bwa20TU0bn4A0zA0gO02oe2a2ibQ0kW03nq02cm0tGu0hm0_A08cg0Q210w2383IwSw","__req" : "l","__hs" : "19438.HYP:comet_pkg.2.1..2.1","dpr" : "2","__ccg" : "GOOD","__rev" : "1007155328","__s" : "x9k4g6:qvnrn2:gabyl2","__hsi" : "7213309158787601147","__comet_req" : "15","fb_dtsg" : self.fb,"jazoest" : "25533","lsd" : self.jazoest,"__aaid" : "2192309537797609","__spin_r" : "1007155328","__spin_b" : "trunk","__spin_t" : "1679479414","fb_api_caller_class" : "RelayModern","fb_api_req_friendly_name" : "CometUserFollowMutation",'variables' : '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1679479423097,686412,190055527696468,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+id+'","tracking":null,"actor_id":"'+self.user_id+'","client_mutation_id":"1"},"scale":2}',"server_timestamps" : "true","doc_id" : "5967051660053260"}
		fl = requests.post('https://www.facebook.com/api/graphql/',headers=self.head, cookies=self.cookie, data=data)
		return fl
	def cmt(self, id, nd):
		data={'fb_dtsg': self.fb, 'jazoest': self.jazoest,'comment_text': nd, 'photo': '(binary)', 'post': 'Bình luận'}
		url='https://upload.facebook.com/_mupload_/ufi/mbasic/advanced/?ids&photosrc=advanced_composer_comment&lpwfwef&ft_ent_identifier='+str(id)
		r=requests.post(url, headers=self.head, cookies=self.cookie, data=data)
		return r
	def share(self, id_post):
		data = {'fb_dtsg': self.fb,'jazoest': self.jazoest,'fb_api_caller_class': 'RelayModern','fb_api_req_friendly_name': 'useCometFeedToFeedReshare_FeedToFeedMutation','variables': '{"input":{"attachments":{"link":{"share_scrape_data":"{\\"share_type\\":22,\\"share_params\\":['+id_post+']}"}},"audiences":{"undirected":{"privacy":{"allow":[],"base_state":"EVERYONE","deny":[],"tag_expansion_state":"UNSPECIFIED"}}},"is_tracking_encrypted":true,"navigation_data":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,via_cold_start,1667131156143,908005,,"},"source":"www","tracking":["AZXOdDS2v_ZDJSDytbos1u5RXGugxb3OhZDbZyYCHeZ2BrvYu3bItkld1wPFdskAq-5K88-e9701dA_oMoXT0zuUhJnMZXXU6BO_MxONTSqjlEw7bJ-4xD31Gu2ZbEGkwVVHqgAXzioO3EdQK8VTlpDFlm3pCa66yMRxMhj_nyJD7teGP1rNsPo0y1ORuIt9TjhYgJZbimPC3FHaEjTsPPexCorotwXgF3W6IejdjsEIKGUud10LKHuJ3RQk2I7u6NNj6itxPCmOoLACwncbr4yDn1Z-D5TKZF_yxqYCDPv6Yh2zVJHHGOYP6noPYYFcLbHfgIeXq50FqOrd2kLwkeavk5wVA3a9Ig9PXPXfmB_JfA"],"actor_id":"'+self.user_id+'","client_mutation_id":"26"},"renderLocation":"homepage_stream","scale":1,"privacySelectorRenderLocation":"COMET_STREAM","useDefaultActor":false,"displayCommentsContextEnableComment":null,"feedLocation":"NEWSFEED","displayCommentsContextIsAdPreview":null,"displayCommentsContextIsAggregatedShare":null,"displayCommentsContextIsStorySet":null,"displayCommentsFeedbackContext":null,"feedbackSource":1,"focusCommentID":null,"UFI2CommentsProvider_commentsKey":"CometModernHomeFeedQuery"}','server_timestamps': 'true','doc_id': '5624054241022832',}
		response = requests.post('https://www.facebook.com/api/graphql/', headers=self.head, cookies=self.cookie, data=data)
		return response
	def reactcmt(self, idPost, type):
		feedback = base64.b64encode(f"feedback:{idPost}".encode('utf-8')).decode('utf-8')
		if type == "LIKE":id = "1635855486666999"
		if type == "LOVE":id = "1678524932434102"
		if type == "CARE":id = "613557422527858"
		if type == "HAHA":id = "115940658764963"
		if type == "WOW":id = "478547315650144"
		if type == "SAD":id = "908563459236466"
		if type == "ANGRY":id = "444813342392137"
		data = {
            'av': self.user_id,
            'dpr': '1',
            'fb_dtsg': self.fb,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
            'variables': '{"input":{"attribution_id_v2":"CometHomeRoot.react,comet.home,tap_tabbar,1727573265800,738538,4748854339,,","feedback_id":"'+feedback+'","feedback_reaction_id":"'+id+'","feedback_source":"DEDICATED_COMMENTING_SURFACE","feedback_referrer":"/ng.ngoc.tra.my.417070","is_tracking_encrypted":true,"tracking":["AZXxRyUYokpiUZc_kK12r3LhZ4F4OzYMIMKxDt5g9s4RIWcqbWUxvVqzlJ897AmhYxlMyW4qaN7Q7AjVuq-d77b-pTdWoFJlSQz9OMBtWhSRGEKRAzDuhGghN8eI5m3sd150-FxnJtjKIgvzmT2SMxCTaGHhrfL9HZcQuGEom9_xuiAqKQewpftvMshAVVmGLMEXPgf7DjfISYDksJ141oJPBWuGN7om5RsxCnzTc4pCo_5EMXA5rCrnO7RPtEpyQqMEWT31f6xqGrzgOM27UKBGg5PAWH2KWb-lO8GN7cPG8AC6uXd9JbfpJS5yQx2M6uwx1ifYfEXfOotbtTt4_yS4EFXUNMLuKE9Jf9ZA8vcfhCEOH1WRba0B_w7kCkYklDBvTcpLyWFWD5iiIPedx6hpWLiuzPR36qB-tusYR3ubLrbjJy6ohoUMd1k75Mrjrc1Ad4D6Ld6IYeaARA23upQIbrRqrije3kkRWNYLGfJK8dCzjf0fDYasnWmSKvcfJL5iA8fxIpXU7cYOs_0dzWZM6Lf4HiGQQnbw0lja6QOoo8FZiEujALKioICg93ub2_-T6l2VJNX2f43k7VNT5no904gn1Yy6HyMDHbAky0g7sAraowHAzAzc3w0wNangc53-FyxO-3d_IJXXU1-OcWNbUxJAJEXZ5RHJii9pZhupuz2Gp-WkCHQLSPPnrPDmz3JWj4GJgahe5NMWxxTa28z0kA6oZNgzqFZ7uImAQJ3MDFgcA77xXuC1_FnRrDI5VDncx2xd7IV_8d_ZzO2Rpu2BNXExAqS6o9OdLoqV-mgGU-B8e5xHq1fPZNvKcnh7gumILI09MUKYpCoqxEjFcigMB-TPnEri2YCWcI2chhDpTyVFQZwa0Ufi0RjaMY7nJyqXXwzy8VcnAbk-D4sAKbeS769nNxmtMiBO8N1FShXIdqrYbzq9YGr2tEVS146kfCAg7jvRGBnsrkaWYlnAOLvXDAPo0IDsN9Hf64_v9ojL7UIX5Ra4SR8t55xWNZgV1dl1_TI66ArEbki2cBPH7Rir9qcYdC-zf7KjhSoC9xF_TllHDOG0AjYhm3B_Aop29u-mBfh6YlWtD63i-kbG1toN-mV_-Ype7UWN2YYcgb8AQBws3vhLnrEFwuuqbekPaE4uWw0DxHqHpw5FnpoX0leM4SggL7z4tSITvbJYb4TBW_XQPC1kbMIg7eQMy8rCk_TSE89B9fGsm1O9Z4dAfLaAio-5VPiIpCjHFx4Z41Xogz2dsMy1YXuZJuYSp4atShaCkzW7WEjmxPCfRTIXbviLl-edV_Z_VQKY2mLXfnaVR9rH0NA3J9qOlBOqTcAxPlsUZm20Iw6uQJd_2JLFyia4VXLzp-rnuSGpX0ecnp-MaVN_jqa6jjUtHzdrCQNCWUUzpQmAIsPGBvPSTy-5-fK2jOexYDzkVE4EC-s2hrOGm8kXJZVTTYfcpFOnb76-YHs6mGys3eShS-MH2qAthdce23mIil34PLiVHP6JvgvPQogCClxUhZzJbGeBCSyqmCzpbs4Vl8SMsYSRqxJP2gq5"],"session_id":"f9ba1774-c42c-4477-93ce-257aba1d7cae","actor_id":"'+self.user_id+'","client_mutation_id":"2"},"useDefaultActor":false,"__relay_internal__pv__CometUFIReactionsEnableShortNamerelayprovider":false}',
            'server_timestamps': 'true',
            'doc_id': '8030707243693006',
        }
		response = requests.post('https://www.facebook.com/api/graphql/', headers=self.head, cookies=self.cookie, data=data)
		return response
class TDS:
	def __init__ (self, token) -> None:
		self.token = token
		self.head = {
		"Host":"traodoisub.com",
		"user-agent":"Mozilla/5.0 (Linux; Android 12; SM-A217F Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36",
		"accept":"*/*",
		"x-requested-with":"mark.via.gp",
		"sec-fetch-site":"same-origin",
		"sec-fetch-mode":"cors",
		"sec-fetch-dest":"empty",
		"referer":"https://traodoisub.com/ex/like/",
		"accept-encoding":"gzip, deflate",
		"accept-language":"vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
		}
	def login(self):
		get = requests.get("https://traodoisub.com/api/?fields=profile&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			self.xu = get["data"]["xu"]
			self.user = get["data"]["user"]
			return {"xu":self.xu, "user":self.user}
		else:
			return {"error":{"code":190}}
	def Cauhinh(self, id):
		get = requests.get("https://traodoisub.com/api/?fields=run&id="+id+"&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			return {"success":200}
		else:
			return {"error":200}
	def GetJob(self, type):
		get = requests.get("https://traodoisub.com/api/?fields="+type+"&access_token="+self.token, headers=self.head).json()
		try:
			if get["error"] == "Thao tác quá nhanh vui lòng chậm lại":
				print(do+"TẠM THỜI HẾT NHIỆM VỤ"+type+"                         ".upper(), end="             \r")
			else:
				print(do+"TẠM THỜI HẾT NHIỆM VỤ"+type+"                         ".upper(), end="             \r")
		except:
			return get
	def NhanJob(self, id, type):
		get = requests.get("https://traodoisub.com/api/coin/?type="+type+"&id="+id+"&access_token="+self.token, headers=self.head).json()
		if "success" in get:
			return {"success":200, "xu":get["data"]["xu"], "msg":get["data"]["msg"].replace("+", "").replace(" Xu", "")}
		else:
			return {"error":200}
def NhapTds():
	while True:
		if os.path.exists('tktds_Jiray.txt'):
			with open('tktds_Jiray.txt', 'r') as f:
				list = json.loads(f.read())
			log = TDS(list[0]).login()['user']
			print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}1{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Giữ Lại TDS : {vang}{log}")
			print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}2{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Đổi Tài Khoản FB")
			chon = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] {xanh_la_nhat}Nhập Lựa Chọn : {trang}')
			if chon == '1':
				khang(1)
				return list
			elif chon == '2':
				os.remove('tktds_Jiray.txt'); khang(34)
			else:
				print(do+'Vui Lòng Lựa Chọn Chính Xác'); khang(34); continue
		if not os.path.exists('tktds_Jiray.txt'):
			j = []
			while True:
				tk = input(f'{xanh_la_nhat}Nhập {vang}Access Token {xanh_la_nhat}TraoDoiSub : {trang}')
				login = TDS(tk).login()
				if "error" in login:
					print(f'{do_nhat}Token Die Hoặc Không Tồn Tại!')
					continue
				else:
					user = login["user"]
					khang(1)
					j.append(tk)
					with open('tktds_Jiray.txt', 'w') as f:
						json.dump(j, f)
					break
			try:
				with open('tktds_Jiray.txt', 'r') as f:
					list = json.loads(f.read())
				return list
			except:
				os.remove('tktds_Jiray.txt'); khang(34)
def random_color():
    colors = [do, xanh_la, nau, xanh_duong, tim, xanh_ngoc, xam_nhat, xam_dam, do_nhat, xanh_la_nhat, vang, xanh_duong_nhat, tim_nhat, hong, xanh_ngoc_nhat, trang_nhat]
    return random.choice(colors)
def success(dem, id, type, msg, xu):
    xuNow = '{:,}'.format(int(xu)).replace(',', '.')
    timeNow = datetime.now().strftime("%H:%M:%S") 
    print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ] {do_nhat}| {xanh_ngoc}{type} {do_nhat}| {hong}{id} {do_nhat}| {vang}+ {msg} Xu {do_nhat}| {nau}{timeNow} {do_nhat}| {xanh_la_nhat}XU : {vang}{xuNow} {do_nhat}|")
def error(id, type, dem):
	print(f'{do}[{vang}{dem}{do}] {type}|{id} ERROR							', end = '\r')
	print(' '*50, end='\r')
def NhapCookieFb():
	list = []
	z = 0
	cookie = input(f'{xanh_la_nhat}Nhập {vang}Cookie {xanh_la_nhat}Facebook{xanh_la_nhat} : {trang}')
	getid = GETID(jsoncookie(cookie))
	for i in getid:
		id = i["profile"]["id"]
		name = i["profile"]["name"]
		o = input(f'{xanh_la_nhat}[{z}] Sử Dụng Page : {vang}{name}(Y/N): ')
		if o.upper() == "Y":list.append(cookie+"; i_user="+id+";");z+=1
	khang(34)
	return list
def LuuCookie():
	while True:
		if os.path.exists('infoCKFB.txt'):
			print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}1{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Giữ Lại FB")
			print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}2{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Đổi Tài Khoản FB")
			chon = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] {xanh_la_nhat}Nhập Lựa Chọn : {trang}')
			if chon == '1':
				with open('infoCKFB.txt', 'rb') as f:list = json.load(f);break
			elif chon == '2':
				os.remove('infoCKFB.txt'); khang(34)
			else:
				print(do+'LỰA CHỌN KHÔNG XÁC ĐỊNh.'); khang(34); continue
		if not os.path.exists('infoCKFB.txt'):
			list = NhapCookieFb()
			with open('infoCKFB.txt', 'w') as f:
				json.dump(list, f)
			break
	return list
def main():
	#clear()
  #banner()
	get = NhapTds()
	listck = LuuCookie()
	clear()
	banner()
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}1{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}LIKE')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}2{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}REACTION')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}3{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}REACTION COMMENT')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}4{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}COMMENT')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}5{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}FOLLOW')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}6{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}SHARE')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}7{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}GROUP')
	print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}8{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}PAGE')
	nv = input(f'{trang}→ {xanh_la_nhat}Nhập Nhiệm Vụ ( Muốn Chạy Nhiều Nhiệm Vụ Thì Viết Liền Nhau : 123...) : {trang}')
	listnv = [int(j) for j in str(nv)]
	delaymin = int(input(f'{trang}→ {xanh_la_nhat}Nhập Delay {vang}MIN {xanh_la_nhat}: {trang}'))
	delaymax = int(input(f'{trang}→ {xanh_la_nhat}Nhập Delay {vang}MAX {xanh_la_nhat}: {trang}'))
	nvblock = int(input(f'{trang}→ {xanh_la_nhat}Sau Bao Nhiêu Nhiệm Vụ Thì Kích Hoạt Chống Block : {trang}'))
	delaybl = int(input(f'{trang}→ {xanh_la_nhat}Sau {vang}{nvblock}{xanh_la_nhat} NV Thì Nghỉ Bao Nhiêu Giây : {trang}'))
	if str(len(listck)) == "1":jjjj="0"
	else:
		doinick = int(input(f'{trang}→ {xanh_la_nhat}Sau Bao Nhiêu NV Thì Đổi Page : {trang}'))
	dem = 0
	demck = 0
	khang(1)
	while True:
		if len(listck) == 0:
			khang(34)
			print(do+'Tất Cả Cookie Đã Văng, Vui Lòng Nhập Lại')
			listck = NhapCookieFb()
			with open('infoCKFB.txt', 'w') as f:
				json.dump(listck, f)
		with open('infoCKFB.txt', 'w') as f:
			json.dump(listck, f)
		for cookie in listck:
			demck += 1
			try:
				z = listnv
				idck = cookie.split("i_user=")[1].split(";")[0]
				face = Facebook(cookie)
				aaa = face.infocookie()
				if "success" in aaa:
					Tds = TDS(get[0])
					cauhinh = Tds.Cauhinh(idck)
					name = aaa['name']
					if "success" in cauhinh:
						print(f'{xanh_la_nhat}UID : {vang}{idck} {xanh_la_nhat}<> NAME : {vang}{name} {xanh_la_nhat}<> Tổng Cookie : {vang}{len(listck)}       ')
						khang(34)
					else:
						print(do+"Page : "+vang+idck+do+" Chưa Được Cấu Hình")
						listck.remove(cookie)
						continue
				else:
					print(do+"Cookie: "+vang+idck+do+" Die Hoặc Hết Hạn!")
					listck.remove(cookie)
					continue
				spam = 0
				error_like_a = 0
				error_reactcmt = 0
				error_cx = 0
				error_fl = 0
				error_share = 0
				error_cmt = 0
				error_group = 0
				while True:
					nhiemvu = random.choice(z)
					if spam == 1:break
					if len(z) == 0:
						print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Hết Các Tính Năng")
						listck.remove(cookie)
						spam = 1
						break
					if nhiemvu == 1:
						getT = random.choice(['like', 'likegiare', 'likesieure'])
						try:
							listnvlike = Tds.GetJob(getT)
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvlike)} {xanh_la_nhat}Nhiệm Vụ {getT.upper()}              					', end='\r')
							for D in listnvlike:
								id = D["id"]
								if "_" in id:idlike = id.split("_")[1]
								else:idlike = id
								try:
									like = face.CamXuc(idlike, "LIKE")
									nhan = Tds.NhanJob(id, getT.upper())
									if "success" in nhan:
										dem += 1
										error_like_a = 0
										success(dem, id, getT.upper(), nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_like_a += 1
										error(id, getT.upper(), error_like_a)
										if error_like_a == 10: break
								except:
									error_like_a += 1
									error(id, getT.upper(), error_like_a)
									if error_like_a == 10: break
							if error_like_a == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng Like")
									z = z.remove(1)
									break
						except:print(end="\r")
					elif nhiemvu == 2:
						try:
							listnvcx = Tds.GetJob("reaction")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvcx)} {xanh_la_nhat}Nhiệm Vụ REACTION         			    ', end='\r')
							for D in listnvcx:
								id = D["id"]
								type = D["type"]
								if "_" in id:idlike = id.split("_")[1]
								else:idlike = id
								try:
									like = face.CamXuc(idlike, type)
									nhan = Tds.NhanJob(id, type)
									if "success" in nhan:
										dem += 1
										error_cx = 0
										success(dem, id, type, nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_cx += 1
										error(id, type, error_cx)
										if error_cx == 10: break
								except:
									error_cx += 1
									error(id, type, error_cx)
									if error_cx == 10: break
							if error_cx == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng Reaction")
									z = z.remove(2)
									break
						except:print(end="\r")
					elif nhiemvu == 3:
						try:
							listnvrect = Tds.GetJob("reactcmt")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvrect)} {xanh_la_nhat}Nhiệm Vụ REACTION CMT         			    ', end='\r')
							for D in listnvrect:
								id = D["id"]
								type = D['type']
								try:
									share = face.reactcmt(id, type)
									nhan = Tds.NhanJob(id, str(type).upper())
									if "success" in nhan:
										dem += 1
										error_share = 0
										success(dem, id, str(type).upper(), nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_reactcmt += 1
										error(id, "REACTCMT", error_reactcmt)
										if error_reactcmt == 10: break
								except:
									error_reactcmt += 1
									error(id, "REACTCMT", error_reactcmt)
									if error_reactcmt == 10: break
							if error_reactcmt == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng REACTCMT")
									z = z.remove(6)
									break
						except:print(end="\r")
					elif nhiemvu == 5:
						try:
							listnvfl = Tds.GetJob("follow")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvfl)} {xanh_la_nhat}Nhiệm Vụ FOLLOW         			    ', end='\r')
							for D in listnvfl:
								id = D["id"]
								if "_" in id:idshare = id.split("_")[1]
								else:idshare = id
								try:
									follow = face.follow(idshare)
									nhan = Tds.NhanJob(id, "FOLLOW")
									if "success" in nhan:
										dem += 1
										error_share = 0
										success(dem, id, "FOLLOW", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_fl += 1
										error(id, "FOLLOW", error_fl)
										if error_fl == 10: break
								except:
									error_fl += 1
									error(id, "FOLLOW", error_fl)
									if error_fl == 10: break
							if error_fl == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng FOLLOW")
									z = z.remove(5)
									break
						except:print(end="\r")
					elif nhiemvu == 6:
						try:
							listnvshare = Tds.GetJob("share")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvshare)} {xanh_la_nhat}Nhiệm Vụ SHARE         			    ', end='\r')
							for D in listnvshare:
								id = D["id"]
								if "_" in id:idshare = id.split("_")[1]
								else:idshare = id
								try:
									share = face.share(idshare)
									nhan = Tds.NhanJob(id, "SHARE")
									if "success" in nhan:
										dem += 1
										error_share = 0
										success(dem, id, "SHARE", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_share += 1
										error(id, "SHARE", error_share)
										if error_share == 10: break
								except:
									error_share += 1
									error(id, "SHARE", error_share)
									if error_share == 10: break
							if error_share == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng SHARE")
									z = z.remove(6)
									break
						except:print(end="\r")
					elif nhiemvu == 4:
						try:
							listnvcmt = Tds.GetJob("comment")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvcmt)} {xanh_la_nhat}Nhiệm Vụ COMMENT         			    ', end='\r')
							for D in listnvcmt:
								id = D["id"]
								msg = D["msg"]
								if "_" in id:idcmt = id.split("_")[1]
								else:idcmt = id
								try:
									cmt = face.cmt(idcmt, msg)
									nhan = Tds.NhanJob(id, "COMMENT")
									if "success" in nhan:
										dem += 1
										error_cmt = 0
										success(dem, id, "COMMENT", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_cmt += 1
										error(id, "COMMENT", error_cmt)
										if error_cmt == 10: break
								except:
									error_cmt += 1
									error(id, "COMMENT", error_cmt)
									if error_cmt == 10: break
							if error_cmt == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng COMMENT")
									z = z.remove(4)
									break
						except:print(end="\r")
					elif nhiemvu == 7:
						try:
							listnvgr = Tds.GetJob("group")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvgr)} {xanh_la_nhat}Nhiệm Vụ GROUP         			    ', end='\r')
							for D in listnvgr:
								id = D["id"]
								if "_" in id:idgr = id.split("_")[1]
								else:idgr = id
								try:
									gr = face.group(idgr)
									nhan = Tds.NhanJob(id, "GROUP")
									if "success" in nhan:
										dem += 1
										error_group = 0
										success(dem, id, "GROUP", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_group += 1
										error(id, "GROUP", error_group)
										if error_group == 10: break
								except:
									error_group += 1
									error(id, "GROUP", error_group)
									if error_group == 10: break
							if error_group == 10:
								aaa = face.infocookie()
								if "error" in aaa:
									check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
									try:
										if str(check["data"]["height"]) == "50":
											print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
										else:
											print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
									except:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
									listck.remove(cookie)
								else:
									print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng GROUP")
									z = z.remove(7)
									break
						except:print(end="\r")
					elif nhiemvu == 8:
						try:
							listnvpage = Tds.GetJob("page")
							print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(listnvpage)} {xanh_la_nhat}Nhiệm Vụ PAGE         			    ', end='\r')
							for D in listnvpage:
								id = D["id"]
								if "_" in id:idpage = id.split("_")[1]
								else:idpage = id
								try:
									page = face.likepage(idpage)
									nhan = Tds.NhanJob(id, "PAGE")
									if "success" in nhan:
										dem += 1
										error_group = 0
										success(dem, id, "PAGE", nhan["msg"], nhan["xu"])
										if str(len(listck)) == "1":jjjj="0"
										else:
											if dem % doinick == 0:
												spam = 1
												break
										if dem % nvblock == 0:
											idelayblock(delaybl)
										else:
											idelay(delaymin, delaymax)
									else:
										error_page += 1
										error(id, "PAGE", error_page)
										if error_page == 10: break
								except:
									error_page += 1
									error(id, "PAGE", error_page)
									if error_page == 10: break
							if error_page == 10:
								aaa = face.infocookie()
								check = requests.get("https://graph.facebook.com/"+idck+"/picture?redirect=false").json()
								try:
									if str(check["data"]["height"]) == "50":
										print(do+"Cookie Page "+vang+demck+do+" Đã Bị CP")
									else:
										print(do+"Cookie "+vang+idck+do+" Đã Bị Văng")
								except:
									print(do+"Cookie "+vang+idck+do+" Đã Bị Logout")
								listck.remove(cookie)
							else:
								print(do+"Page "+vang+aaa["name"]+do+" Đã Bị Block Tính Năng PAGE")
								z = z.remove(8)
								break
						except:print(end="\r")
					LoadJob("10")
			except:
				print(do+"Cookie "+vang+str(demck)+do+" Đã Bị Văng")
				listck.remove(cookie)
				os.remove('infoCKFB.txt')
main()
