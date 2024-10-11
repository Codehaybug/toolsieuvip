
import requests, time, os, sys, random
from datetime import datetime

try:
    with open('JirayKeyTool.txt','r') as f:
        key =f.read().split()
        if len(key) == 0:
            print('Yah, Mò được đến đây rồi thì hẳn chắc cũng pro lắm :v nma kệ cmm nhé đ crack đc của t đâu =))')
            exit()
        else:
            pass
except Exception as e:print('Làm gì vậy fen._.?');exit()
black     = "\033[30m"
red       = "\033[31m"
green     = "\033[32m"
yellow    = "\033[33m"
blue      = "\033[34m"
purple    = "\033[35m"
whiteBlue = "\033[36m"
gray      = "\033[37m" 
white     = "\033[37m"
black     = "\033[40m"

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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Auto Game QuackQuack Telegram{trang_nhat}
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
class QuackQuack:
    def __init__(self, token):
        self.token = token
        self.headers = {
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9',
            'authorization': f'Bearer {self.token}',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://dd42189ft3pck.cloudfront.net',
            'priority': 'u=1, i',
            'referer': 'https://dd42189ft3pck.cloudfront.net/',
            'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'cross-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
        }
    def GetTotalEgg(self):
        listEgg = []
        response = requests.get('https://api.quackquack.games/nest/list-reload', headers=self.headers).json()
        #
        if response["error_code"] == '':
            egg = response["data"]['nest']
            for idEgg in egg:
                id = idEgg["id"]
                listEgg.append(id)
            return listEgg, response
        else:
            return 0
    def GetTimeGolderDuck(self):
        response = requests.get('https://api.quackquack.games/golden-duck/info', headers=self.headers).json()
        if response["error_code"] == "":
            timeWait = response["data"]["time_to_golden_duck"]
            return timeWait / 60
        else:
            return 0
    def BreakEgg(self, nestID):
        data = {
            'nest_id': nestID,
        }

        response = requests.post('https://api.quackquack.games/nest/collect-duck', headers=self.headers, data=data).json()
        if response["error_code"] == "":
            duck = response["data"]["duck_id"]
            return True, duck
        else:
            return False, "?"
    def GetBalance(self):
        response = requests.get('https://api.quackquack.games/balance/get', headers=self.headers).json()
        # print(response)
        if response["error_code"] == "":
            balance = response["data"]["data"][2]["balance"]
            return True, balance
        else:
            return False, "?"
    def HatchEgg(self, nestID):
        data = {
            'nest_id': nestID,
        }

        response = requests.post('https://api.quackquack.games/nest/hatch', headers=self.headers, data=data).json()
        if response["error_code"] == "":
            timeWait = response["data"]["time_remain"]
            return timeWait
        else:
            return False
    def CollectReward(self):
        response = requests.get("https://api.quackquack.games/golden-duck/reward", headers=self.headers)
        if response["error_code"] == "":
            amount = response["data"]["amount"]
            return amount
        else:
            return '?'
    def CollectEgg(self, nestID):
        data = {
            'nest_id': nestID,
        }

        response = requests.post('https://api.quackquack.games/nest/collect', headers=self.headers, data=data).json()
        if response["error_code"] == "":
            return True
        else:
            return False

def Line():
    print('='*35)

colors = [do, xanh_la, nau, xanh_duong, tim, xanh_ngoc, xam_nhat, xam_dam, do_nhat, xanh_la_nhat, vang, xanh_duong_nhat, tim_nhat, hong, xanh_ngoc_nhat, trang_nhat]
def random_color():
    return random.choice(colors)

Banner()
while True:
    token = input("\033[1;32mNhập AccessToken QuackQuack :\033[1;33m  ")
    t = QuackQuack(token)
    if t.GetBalance()[0] == False:
        print('\033[31mSai Token Hoặc Token Die, Vui Lòng Thử Lại !')
        print('\033[1;31m────────────────────────────────────────────────────────────')
    else:
        balance = t.GetBalance()[1]
        print(f'\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mĐăng Nhập Thành Công ! Số Dư Hiện Tại: \033[1;33m{balance}')
        break
time.sleep(0.5)
Banner()
print('\033[1;31m────────────────────────────────────────────────────────────')
dem = 1
while True:
    try:
        totalEgg = t.GetTotalEgg()
        if t.GetTimeGolderDuck() / 60 == 0 or t.GetTimeGolderDuck() / 60 == 1 :
            time.sleep(0.5)
            breakEGG = t.CollectReward()
            print(f'\033[37m─────────────────  \033[1;36mGOLDER EGG ! AMOUNT : \033[1;33m{breakEGG} \033[37m─────────────────')
        if totalEgg != 0:
            total = t.GetTotalEgg()[0]
            if len(total) == 0:
                print(f'\033[1;31mHết trứng rồi, chờ nào ~.~',end='\r')
            else:
                for egg in total:
                    a = t.CollectEgg(egg)
                    if a == True:
                        timeNow = datetime.now().strftime("%H:%M:%S")
                        tte = t.GetBalance()[1]
                        print(f"{vang}[{random_color()}D{random_color()}U{random_color()}C{random_color()}T{random_color()}H{random_color()}I{random_color()}N{random_color()}H{random_color()}E{random_color()}X{random_color()}E{random_color()}{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ] {do_nhat}| {xanh_ngoc}NHẶT THÀNH CÔNG {do_nhat}| {hong}{egg} {do_nhat}| {nau}{timeNow} {do_nhat}| {xanh_la_nhat}TOTAL EGG : {vang}{tte}")
                        dem+=1
                    else:
                        print(f'\033[1;31mHết trứng, đợi đẻ đã ní ơi :() ! ',end='\r')
        else:
            print(f'\033[1;31mĐang hết trứng, vui lòng đợi nào ~.~',end='\r')
            time.sleep(1)
    except Exception as e:pass
