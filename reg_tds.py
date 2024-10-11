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
import string
from pystyle import *
from datetime import datetime
import requests,os,sys, time
##############
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

########################################
notification = requests.get("https://jirayshop.xyz/keytool/notification.php").text
res = requests.get('https://ipinfo.io/json').json()
ip = res['ip']
########################################
colors = [do, xanh_la, nau, xanh_duong, tim, xanh_ngoc, xam_nhat, xam_dam, do_nhat, xanh_la_nhat, vang, xanh_duong_nhat, tim_nhat, hong, xanh_ngoc_nhat, trang_nhat]
def random_color():
    return random.choice(colors)
def hoanthanh(dem, id, type, msg, xu):
	xuNow = '{:,}'.format(int(xu)).replace(',', ' ')
	timeNow = datetime.now().strftime("%H:%M:%S") 
	print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ] {do_nhat}| {xanh_ngoc}{type} THÀNH CÔNG {do_nhat}| {hong}{id} {do_nhat}| {vang}{msg} {do_nhat}| {nau}{timeNow} {do_nhat}| {xanh_la_nhat}XU : {vang}{xuNow}")

####[LOGO]#####
import binascii, codecs, base64, random
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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Auto Reg Acc Trao Đổi Sub{trang_nhat}
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
def Banner():
    t.Logo(key, date)
##############################
class RegTDS:
	def __init__(self, apikey):
		self.apiKey = apikey
	@property
	def RandomUser(self):
		length = randint(8, 12)
		valid_chars = string.ascii_letters + string.digits
		username = ''.join(random.choice(valid_chars) for _ in range(length))
		return username
	@property
	def RandomPass(self):
		length = randint(8, 12)
		all_chars = string.ascii_letters + string.digits + string.punctuation
		password = ''.join(random.choice(all_chars) for _ in range(length))
        
		while (not any(c.islower() for c in password) or
            not any(c.isupper() for c in password) or
            not any(c.isdigit() for c in password) or
            not any(c in string.punctuation for c in password)):
			password = ''.join(random.choice(all_chars) for _ in range(length))
		return password
	def PassRecaptcha(self):
		dem = 1
		res = requests.get('https://traodoisub.com/').text
		try:
			sitekey = '6LeGw7IZAAAAAECJDwOUXcriH8HNN7_rkJRZYF8a'
			baseURL = "https://traodoisub.com/"
			urlCaptcha  = 'https://api.3xcaptcha.com/'
			
			data = {
			    "clientKey": self.apiKey,
			    "task": {
			            "type": "RecaptchaV2TaskProxyless",
			            "websiteURL": baseURL,
			            "websiteKey": sitekey
			        }
			    }
			response = requests.post(urlCaptcha + 'createTask', json=data).json()
			try:
				taskID = response['taskId']
				while True:
					start = requests.post(urlCaptcha + 'getTaskResult', json = { "clientKey":self. apiKey, "taskId": taskID }).json()
					print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ]{do_nhat} | {xanh_ngoc_nhat}Đang Giải Captcha...", end='\r')
					dem+=1
					status = start['status']
					if status == "ready":
						dataCaptcha = start['solution']['gRecaptchaResponse']
						return True, dataCaptcha
					elif status == "error":
						return False, "Giải Captcha Thất Bại!"
					else:
						time.sleep(0.25)
			except:
				return False, "Không Thể Tạo Tiến Trình Giải Captcha"
		except:
			return False, "Lỗi Giải Captcha Trao Đổi Sub"
	def MainReg(self, userName, pwd):
		res = self.PassRecaptcha()
		result = res[1]
		if res[0] == False:
			return False, f"{do}{result}"
		else:
			data = {
                "dkusername": userName,
                "dkpassword": pwd,
                "rdkpassword": pwd,
                "g-recaptcha-response": result
            }
			response = requests.post('https://traodoisub.com/scr/check_reg.php', data=data)
			if "success" in response.text:
				return True, "Đăng Ký Thành Công!"
			else:
				msg = response.json()['error']
				return False, f"{do}{msg}"	
Banner()
print(f"{xanh_la_nhat}NẾU CHƯA CÓ TÀI KHOẢN 3XCAPTCHA CÓ THỂ ĐĂNG KÝ TẠI")
print(f'{trang_nhat}═════════════════════════════════════════════════════')
print(f'            {trang}https://3xcaptcha.com')
print(f'{trang_nhat}═════════════════════════════════════════════════════')
while True:
	apiKey = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] Nhập ApiKey 3xCaptcha : ')
	check = requests.post(f'https://api.3xcaptcha.com/getBalance', json={ "clientKey": apiKey })
	if check.json()['errorId'] == 0:
		balance = check.json()['balance']
		print(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] => \033[1;32mĐăng Nhập Thành Công ! Số Dư Hiện Tại: \033[1;33m{balance}')
		time.sleep(0.25)
		break
	else:
		print(f'{do_nhat}ApiKey Không Hợp Lệ!')
Banner()
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}1{nau} ] {xanh_la_nhat}Reg Acc {vang}Random')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}2{nau} ] {xanh_la_nhat}Reg Acc {vang}Theo Yêu Cầu')
typeUser = int(input(f'{trang}→ {xanh_la_nhat}Nhập Lựa Chọn : {trang}'))
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}1{nau} ] {xanh_la_nhat}Password {vang}Random')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}2{nau} ] {xanh_la_nhat}Password {vang}Theo Yêu Cầu')
typePass = int(input(f'{trang}→ {xanh_la_nhat}Nhập Lựa Chọn : {trang}'))
if typePass == 2:
    passReg = input(f'{trang}→ {xanh_la_nhat}Nhập Password Cần Reg : {trang}')
elif typePass == 1:
	passReg = "RD"
else:
	print(f'{do_nhat}Lựa Chọn Không Hợp Lệ!')
	exit()
if typeUser == 2:
    userReg = input(f'{trang}→ {xanh_la_nhat}Nhập Tên User Cần Reg : {trang}')
elif typeUser == 1:
	userReg = "RD"
else:
	print(f'{do_nhat}Lựa Chọn Không Hợp Lệ!')
	exit()
soluong = int(input(f'{trang}→ {xanh_la_nhat}Nhập Số Lượng Tài Khoản Muốn Tạo : {trang}'))
print(f'{trang_nhat}═════════════════════════════════════════════════════')
dem = 1
for i in range(0, soluong):
	reg = RegTDS(apiKey)
	if typeUser == 1:
		user = reg.RandomUser
	else:
		user = userReg
	if typePass == 1:
		pwd  = reg.RandomPass
	else:
		pwd  = passReg
	result = reg.MainReg(user, pwd)
	if result[0] == True:
		with open('taikhoantds.txt', 'a') as f:
			f.write(f'{user}|{pwd}\n')
		balance = requests.post(f'https://api.3xcaptcha.com/getBalance', json={ "clientKey": apiKey }).json()['balance']
		timeNow = datetime.now().strftime("%H:%M:%S") 
		print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ]{do_nhat} | {xanh_ngoc_nhat}Reg Thành Công {do_nhat} | {nau}{timeNow} {do_nhat}| {vang}{user} {do_nhat}| {vang}{pwd}{do_nhat} | {xanh_ngoc_nhat}Số Dư Captcha : {vang}{balance}")
		dem += 1
	else:
		i-=1
		rs = result[1]
		print(f'{do}Reg Thất Bại, Lý Do : {trang_nhat}{rs}', end='\r')
print(f'{xanh_la_nhat}Reg Thành Công : {vang}{soluong} {xanh_la_nhat} Tài Khoản, Tài Khoản Được Lưu Tại File taikhoantds.txt!')
exit()
		
	
