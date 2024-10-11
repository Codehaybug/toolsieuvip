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


import os, json, requests, sys, re, time
from datetime import datetime
import uuid, random, base64
from random import randint
from time import sleep
import random
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
try:
    with open('JirayKeyTool.txt', 'r') as f:
        key = f.read().split()[0]
        if len(key) < 5:
            print(f'{do}Xin Lỗi, Bạn Đang Cố Tình Hay Vô Ý Vậy?')
            exit()
        else:
            pass
except:
    print(f'{do}Xin Lỗi, Bạn Đang Cố Tình Hay Vô Ý Vậy?')
    exit()
########################################
notification = requests.get("https://jirayshop.xyz/keytool/notification.php").text
res = requests.get('https://ipinfo.io/json').json()
ip = res['ip']
########################################
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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Trao Đổi Sub Facebook V2{trang_nhat}
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
############## FUNCTION #################
def ducthinh():print(f'{trang_nhat}═════════════════════════════════════════════════════')
def cv(coin):return '{:,}'.format(int(coin)).replace(',', '.')
colors = [do, xanh_la, nau, xanh_duong, tim, xanh_ngoc, xam_nhat, xam_dam, do_nhat, xanh_la_nhat, vang, xanh_duong_nhat, tim_nhat, hong, xanh_ngoc_nhat, trang_nhat]
def random_color():
    return random.choice(colors)
def HoanThanh(dem, id, type, msg, xu):
    xuNow = '{:,}'.format(int(xu)).replace(',', '.')
    timeNow = datetime.now().strftime("%H:%M:%S") 
    print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ] {do_nhat}| {xanh_ngoc}{type} THÀNH CÔNG {do_nhat}| {hong}{id} {do_nhat}| {vang}{msg} {do_nhat}| {nau}{timeNow} {do_nhat}| {xanh_la_nhat}XU : {vang}{xuNow}")
def InputInstagram():
    listCK = []
    dem = 1
    while True:
        cookieFB = input(f'{xanh_la_nhat}Nhập {vang}Cookie {xanh_la_nhat}Instagram {vang}{dem}{xanh_la_nhat} : {trang}')
        if len(cookieFB) < 3:break
        ig = Instagram(cookieFB)
        log = ig.Login
        if log[0] == True:
            idUser = log[1]
            print(f'{xanh_la_nhat}Đăng Nhập Thành Công Tài Khoản : {vang}{idUser}{xanh_la_nhat} !')
            listCK.append(cookieFB)
            ducthinh()
            dem+=1
        else:
            print(f'{do_nhat}Cookie Die Hoặc Không Tồn Tại!')
            ducthinh()
    with open('infoCKIG_Jiray.txt', 'w', encoding='utf-8') as f:
        json.dump(listCK, f)
def InputTDS():
    while True:
        tokenTDS = input(f'{xanh_la_nhat}Nhập {vang}Access Token {xanh_la_nhat}TraoDoiSub : {trang}')
        tds = TraoDoiSub(tokenTDS)
        log = tds.Login
        if log[0] == True:
            userTDS, xu = log[1], log[2]
            xuNow = cv(xu)
            print(f'{xanh_la_nhat}Đăng Nhập Thành Công TraoDoiSub : {vang}{userTDS}{xanh_la_nhat} - Xu Hiện Tại : {vang}{xuNow} {xanh_la_nhat}!')
            with open('infoTDS_Jiray.txt', 'w') as f:
                f.write(tokenTDS)
            break
        else:
            print(f'{do_nhat}Token Die Hoặc Không Tồn Tại!')
            ducthinh()
def chongblock(delaybl):
    while delaybl > 0:
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [.....]                                                   ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•....]                                                  ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [••...]                                                  ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•••..]                                                  ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [••••.]                                                      ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•••••]                                                      ", end='\r')
        sleep(1/6)
        delaybl -= 1
def nghingoi(delaymin, delaymax):
    delay = randint(delaymin, delaymax)
    while delay > 0:
        print(f"{vang}[{xanh_la}<{xanh_duong_nhat}DUCTHINHEXE{xanh_la}>{vang}]{vang}[{trang}{delay}{vang}]                                                                      ", end='\r')
        sleep(1)
        delay-=1
def ClearCookie(cookie):
    with open('infoCKIG_Jiray.txt', 'r') as f:
        a = json.load(f)
    if cookie in a:
        a.remove(cookie)
    with open('infoCKIG_Jiray.txt', 'w', encoding="utf-8") as f:
        json.dump(a, f)
class TraoDoiSub:
        def __init__(self, tokenTDS):
            self.tokenTDS = tokenTDS
            self.baseUrl  = "https://traodoisub.com/"
        @property
        def Login(self):
            res = requests.get(self.baseUrl+'api/?fields=profile&access_token={}'.format(self.tokenTDS))
            if 'success' in res.text:
                userTDS, coinNow = res.json()['data']['user'], res.json()['data']['xu']
                return True, userTDS, coinNow
            else:
                return False, "?"
        def GetJob(self, type:str):
            typejob = type.lower()
            if typejob == "follow":jobType = "instagram_follow"
            elif typejob == "like":jobType = "instagram_like"
            elif typejob == "comment":jobType = "instagram_comment"
            return requests.get(self.baseUrl + f'api/?fields={jobType}&access_token={self.tokenTDS}').json()
        def SendFollowCache(self, idJob):
            res = requests.get(self.baseUrl + f'api/coin/?type=INS_FOLLOW_CACHE&id={idJob}&access_token={self.tokenTDS}')
            if 'success' in res.text:
                cache = res.json()['cache']
                return True, int(cache)
            else:
                return False
        def GetCoin(self, idJob, type:str):
            typejob = type.lower()
            if typejob == "follow":
                jobType = "INS_FOLLOW"
                id = 'INS_FOLLOW_API'
            elif typejob == "like":
                jobType = "INS_LIKE"
                id = idJob
            elif typejob == "comment":
                jobType = "INS_COMMENT"
                id = idJob
            response =  requests.get(self.baseUrl + f'api/coin/?type={jobType}&id={id}&access_token={self.tokenTDS}')
            if "success" in response.text:
                xuNow, msg = response.json()['data']['xu'], response.json()['data']['msg']
                return True, xuNow, msg
            else:
                return False, '?'
        def CauHinh(self, id):
            rs = requests.get(self.baseUrl + f'api/?fields=instagram_run&id={id}&access_token={self.tokenTDS}')
            if 'success' in rs.text:
                return True
            else:
                return False
class Instagram:
    def __init__(self, cookieIG:str):
        self.cookieIG = cookieIG
    @property
    def Login(self):
        if "csrftoken=" not in self.cookieIG:return False, '?'
        try:
            csrftoken = self.cookieIG.split('csrftoken=')[1].split(';')[0]
            self.baseHD = {
                    'accept': '*/*',
                    'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': self.cookieIG,
                    'origin': 'https://www.instagram.com',
                    'priority': 'u=1, i',
                    'referer': 'https://www.instagram.com/nhan0023/',
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.100", "Chromium";v="127.0.6533.100"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-model': '""',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-ch-ua-platform-version': '"10.0.0"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                    'x-asbd-id': '129477',
                    'x-bloks-version-id': 'd48864a035b1835e7d6839f3f4f6eccef248b3d94fbc4ded47b31025a6d691c3',
                    'x-csrftoken': csrftoken,
                    'x-fb-friendly-name': 'usePolarisFollowMutation',
                    'x-ig-app-id': '936619743392459',
            }
            res = requests.get('https://instagram.com', cookies={'cookie':self.cookieIG}).text
            try:
                username        = res.split('username":"')[1].split('"')[0]
                userID          = res.split('appScopedIdentity":"')[1].split('"')[0]
                self.actorID    = res.split('actorID":"')[1].split('"')[0]
                self.fb_dtsg    = res.split('DTSGInitData",[],{"token":"')[1].split('"')[0]
                self.jazoest    = res.split('jazoest=')[1].split('"')[0]
                return True, username, userID
            except:
                return False, f'{do}Cookie Die Hoặc Không Tồn Tại!'
        except:
            return False, '?'
    def FollowUser(self, idFollow):
        if self.Login[0] == True:
            data = {
                'av': self.actorID,
                'dpr': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisFollowMutation',
                'variables': '{"target_user_id":"'+idFollow+'","container_module":"profile","nav_chain":"PolarisFeedRoot:feedPage:1:via_cold_start,PolarisProfilePostsTabRoot:profilePage:2:unexpected"}',
                'server_timestamps': 'true',
                'doc_id': '7275591572570580',
            }
            response = requests.post('https://www.instagram.com/graphql/query', headers=self.baseHD, data=data)
            if 'outgoing_request' in response.text:
                crawl = response.json()['data']['xdt_create_friendship']['friendship_status']
                if crawl['following'] == True or crawl['outgoing_request'] == True:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    def LikePost(self, idPost):
        if self.Login[0] == True:
            data = {
                'av': self.actorID,
                'dpr': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'usePolarisLikeMediaLikeMutation',
                'variables': '{"media_id":"'+idPost+'"}',
                'server_timestamps': 'true',
                'doc_id': '8244673538908708',
            }
            res = requests.post('https://www.instagram.com/graphql/query', headers=self.baseHD, data=data)
            if 'error' not in res:
                return True
            else:
                return False
        else:
            return False
    def Comment(self, idPost, text:str):
        if self.Login[0] == True:
            data = {
                'comment_text':text
            }
            response = requests.post(f'https://www.instagram.com/api/v1/web/comments/{idPost}/add/', headers=self.baseHD, data=data)
            if response.json()['status'] == "fail":
                return False
            else:
                return True
        else:
            return False
banner()
while True:
    if os.path.exists('infoTDS_Jiray.txt'):
        with open('infoTDS_Jiray.txt', 'r') as f:
            line = f.read().split()
        tokenTDS = line[0]
        tds = TraoDoiSub(tokenTDS)
        log = tds.Login
        xuNow = '{:,}'.format(int(log[2])).replace(',', '.')
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}1{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Giữ Lại TDS : {vang}{log[1]}")
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}2{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Đổi Tài Khoản")
        chon = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] {xanh_la_nhat}Nhập Lựa Chọn : {trang}')
        if int(chon) == 1:ducthinh();break
        elif int(chon) == 2:
            os.remove('infoTDS_Jiray.txt')
        else:
            print(f'{do_nhat}Lựa Chọn Không Hợp Lệ!')
            ducthinh()
    if not os.path.exists('infoTDS_Jiray.txt'):
        open('infoTDS_Jiray.txt', 'a').close()
        InputTDS()
        ducthinh()
        break
while True:
    if os.path.exists('infoCKIG_Jiray.txt'):
        with open('infoCKIG_Jiray.txt', 'r') as f:
            line = json.load(f)
        if len(line) == 0:os.remove('infoCKIG_Jiray.txt');file = open('infoCKIG_Jiray.txt', 'a').close()
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}1{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Giữ Lại IG")
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}2{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Đổi Tài Khoản IG")
        chon = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] {xanh_la_nhat}Nhập Lựa Chọn : {trang}')
        if int(chon) == 1:
            break
        elif int(chon) == 2:
            os.remove('infoCKIG_Jiray.txt')
        else:
            print(f'{do_nhat}Lựa Chọn Không Hợp Lệ!')
            ducthinh()
    if not os.path.exists('infoCKIG_Jiray.txt'):
        open('infoCKIG_Jiray.txt', 'a').close()
        InputInstagram()
        break
time.sleep(1)
banner()
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}1{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}LIKE')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}2{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}FOLLOW')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}3{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}COMMENT')
nhiemvu = input(f'{trang}→ {xanh_la_nhat}Nhập Nhiệm Vụ ( Muốn Chạy Nhiều Nhiệm Vụ Thì Viết Liền Nhau : 123...) : {trang}')
delaymin = int(input(f'{trang}→ {xanh_la_nhat}Nhập Delay {vang}MIN {xanh_la_nhat}: {trang}'))
delaymax = int(input(f'{trang}→ {xanh_la_nhat}Nhập Delay {vang}MAX {xanh_la_nhat}: {trang}'))
nvblock = int(input(f'{trang}→ {xanh_la_nhat}Sau Bao Nhiêu Nhiệm Vụ Thì Kích Hoạt Chống Block : {trang}'))
dlblock = int(input(f'{trang}→ {xanh_la_nhat}Sau {vang}{nvblock}{xanh_la_nhat} NV Thì Nghỉ Bao Nhiêu Giây : {trang}'))
doinick = int(input(f'{trang}→ {xanh_la_nhat}Sau Bao Nhiêu NV Thì Đổi Acc : {trang}'))
time.sleep(0.5)
banner()
print(f'{trang}→ {xanh_la_nhat}Các Nhiệm Vụ : {trang}{nhiemvu}')
print(f'{trang}→ {xanh_la_nhat}Delay {vang}MIN {xanh_la_nhat}: {trang}{delaymin}')
print(f'{trang}→ {xanh_la_nhat}Delay {vang}MAX {xanh_la_nhat}: {trang}{delaymax}')
print(f'{trang}→ {xanh_la_nhat}Sau {trang}{nvblock} NV{xanh_la_nhat} Thì Nghỉ {trang}{dlblock} {xanh_la_nhat}Giây')
print(f'{trang}→ {xanh_la_nhat}Sau {trang}{doinick} NV{xanh_la_nhat} Thì Đổi Acc')
ducthinh()
with open('infoTDS_Jiray.txt', 'r') as f:
    line = f.read().split()
tokenTDS = line[0]
tds = TraoDoiSub(tokenTDS)
xuNow = tds.Login[2]
dem, blocked = 1, 0
listJob = [int(j) for j in str(nhiemvu)]
while(True):
    with open('infoCKIG_Jiray.txt', 'r', encoding="utf-8") as f:
        linesCookie = json.load(f)
        for cookie in linesCookie:
            error, doiacc = 0, 0
            ig       = Instagram(cookie)
            username = ig.Login[1]
            if tds.CauHinh(username):
                print(f'{xanh_la_nhat}User IG : {vang}{username} {xanh_la_nhat}<> XU : {vang}{xuNow} {xanh_la_nhat}<> Tổng Cookie : {vang}{str(len(linesCookie))}       ')
                ducthinh()
            else:
                print(f'{do_nhat}User IG : {username} Chưa Được Cấu Hình!                   ')
                ClearCookie(cookie)
                ducthinh()
                break
            while True:
                nv = random.choice(listJob)
                if nv == 1:
                    if error == 10:
                        continue
                    get = tds.GetJob('like')
                    if 'error' in get:
                        try:
                            countdown = get['countdown']
                            print(f'{do_nhat}Đang Lấy Nhiệm Vụ LIKE, Countdown : {trang_nhat}{countdown}         ', end='\r')
                            if int(countdown) > 7:
                                for i in range(10, -1 ,-1):
                                    print(f'{xanh_la_nhat}Đã Hết Job, Đang Chờ {vang}{i} Giây...', end='\r')
                                    time.sleep(1)
                        except:
                            msg = get['error']
                            print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ LIKE{trang_nhat}{msg}          ', end='\r')
                            time.sleep(1)
                    else:
                        b = get['data']
                        if len(b) == 0:
                            print(f'{do_nhat}Đã Hết Nhiệm Vụ LIKE{trang_nhat}          ', end='\r')
                        else:
                            print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(b)} {xanh_la_nhat}Nhiệm Vụ LIKE                  ', end='\r')
                            for z in get['data']:
                                if blocked == nvblock:
                                    break
                                if doiacc == doinick:
                                    break
                                job = z['id']
                                link = z['link']
                                idJob = job.split('_')[0]
                                like = ig.LikePost(idJob)
                                if like:
                                    time.sleep(0.25)
                                    nhan = tds.GetCoin(job, 'like')
                                    if nhan[0] == True:
                                        xuNow = nhan[1]
                                        msg   = nhan[2]
                                        HoanThanh(dem, job, 'LIKE', msg, xuNow)
                                        dem += 1
                                        doiacc +=1
                                        blocked +=1
                                        nghingoi(delaymin, delaymax)
                                    else:
                                        print(f'{do_nhat}Nhận Thất Bại : {job} - LIKE               ', end='\r')
                                        time.sleep(0.5)
                                else:
                                    print(f'{do_nhat}LIKE Thất Bại : {link}               ', end='\r')
                                    error+=1
                                    time.sleep(0.5)
                elif nv == 2:
                    if error == 10:
                        continue
                    get = tds.GetJob('follow')
                    if 'error' in get:
                        try:
                            countdown = get['countdown']
                            print(f'{do_nhat}Đang Lấy Nhiệm Vụ FOLLOW, Countdown : {trang_nhat}{countdown}         ', end='\r')
                            if int(countdown) > 7:
                                for i in range(10, -1 ,-1):
                                    print(f'{xanh_la_nhat}Đã Hết Job, Đang Chờ {vang}{i} Giây...', end='\r')
                                    time.sleep(1)
                        except:
                            msg = get['error']
                            print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ FOLLOW{trang_nhat}{msg}          ', end='\r')
                            time.sleep(1)
                    else:
                        if len(get['data']) == 0:
                            print(f'{do_nhat}Đã Hết Nhiệm Vụ FOLLOW{trang_nhat}          ', end='\r')
                        else:
                            b = get['data']
                            print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(b)} {xanh_la_nhat}Nhiệm Vụ FOLLOW                  ', end='\r')
                            for z in get['data']:
                                if blocked == nvblock:
                                    break
                                if doiacc == doinick:
                                    break
                                job = z['id']
                                link = z['link']
                                idJob = job.split('_')[0]
                                follow = ig.FollowUser(idJob)
                                if follow:
                                    time.sleep(0.25)
                                    nhan = tds.SendFollowCache(job)
                                    if nhan[0] == True:
                                        cache = nhan[1]
                                    else:
                                        print(f'{do_nhat}Gửi Duyệt Thất Bại : {job} - LIKE               ', end='\r')
                                        time.sleep(0.5)
                                    if cache > 10:
                                        get = tds.GetCoin(job, 'FOLLOW')
                                        if get[0] == True:
                                            xuNow = get[1]
                                            msg   = get[2]
                                            HoanThanh(dem, job, 'FOLLOW', msg, xuNow)
                                            dem += 1
                                            doiacc +=1
                                            blocked +=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {link} - FOLLOW               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        HoanThanh(dem, job, 'FOLLOW', f'CACHE : {cache}', xuNow)
                                        dem += 1
                                        doiacc +=1
                                        blocked +=1
                                        nghingoi(delaymin, delaymax)
                                else:
                                    print(f'{do_nhat}FOLLOW Thất Bại : {job}               ', end='\r')
                                    error+=1
                                    time.sleep(0.5)
                elif nv == 3:
                    if error == 10:
                        continue
                    get = tds.GetJob('comment')
                    if 'error' in get:
                        try:
                            countdown = get['countdown']
                            print(f'{do_nhat}Đang Lấy Nhiệm Vụ COMMENT, Countdown : {trang_nhat}{countdown}         ', end='\r')
                            time.sleep(1)
                            if int(countdown) > 7:
                                for i in range(10, -1 ,-1):
                                    print(f'{xanh_la_nhat}Đã Hết Job, Đang Chờ {vang}{i} Giây...', end='\r')
                                    time.sleep(1)
                        except:
                            msg = get['error']
                            print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ COMMENT{trang_nhat}{msg}          ', end='\r')
                            time.sleep(1)
                    else:
                        if len(get['data']) == 0:
                            print(f'{do_nhat}Đã Hết Nhiệm Vụ COMMENT{trang_nhat}          ', end='\r')
                        else:
                            b = get['data']
                            print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(b)} {xanh_la_nhat}Nhiệm Vụ COMMENT                  ', end='\r')
                            for z in get['data']:
                                if blocked == nvblock:
                                    break
                                if doiacc == doinick:
                                    break
                                job = z['id']
                                idJob = job.split('_')[0]
                                link = z['link']
                                nd    = z['noidung']
                                like = ig.Comment(idJob, nd)
                                if like:
                                    time.sleep(0.25)
                                    nhan = tds.GetCoin(job, 'comment')
                                    if nhan[0] == True:
                                        xuNow = nhan[1]
                                        msg   = nhan[2]
                                        HoanThanh(dem, job, 'COMMENT', msg, xuNow)
                                        dem += 1
                                        doiacc +=1
                                        blocked +=1
                                        nghingoi(delaymin, delaymax)
                                    else:
                                        print(f'{do_nhat}Nhận Thất Bại : {job} - COMMENT               ', end='\r')
                                        time.sleep(0.5)
                                else:
                                    print(f'{do_nhat}COMMENT Thất Bại : {link}               ', end='\r')
                                    error+=1
                                    time.sleep(0.5)
                if blocked == nvblock:
                    chongblock(dlblock)
                    blocked = 0
                if doiacc == doinick:
                    ducthinh()
                    doiacc = 0
                    break
                if error == 10:
                    ducthinh()
                    check = ig.Login[0]
                    if check:
                        print(f'{do_nhat}Tài khoản IG : {vang}{username}{do_nhat} Đã Bị Block Tính Năng!                    ')
                        ClearCookie(cookie)
                        ducthinh()
                    else:
                        print(f'{do_nhat}Tài khoản IG : {vang}{username}{do_nhat} Đã Bị Die Cookie                ', end='\r')
                        ClearCookie(cookie)
                        ducthinh()
                    break
                with open('infoCKIG_Jiray.txt', 'r') as f:
                    a = json.load(f)
                if len(a) == 0:
                    os.remove('infoCKIG_Jiray.txt')
                    print(f'{do_nhat}Tất Cả Các Cookie Đã Die, Vui Lòng Điền Cookie Mới!')
                    ducthinh()
                    InputInstagram()
                else:
                    pass
# t = Instagram('wd=336x552;datr=CH6oZlhAoyob6l6LzekvuiTW;ps_n=1;ig_nrcb=1;shbts="1723331548\05458634573624\0541754867548:01f78dc218cc56f0e108a01e7b083dce08ce760fcd4089840d6a551e2fe61c6de89cedb8";ds_user_id=58634573624;shbid="8033\05458634573624\0541754867548:01f7a9b5abb1df34e858fac047e8f2d584ab1d60bc7d3dc1814e80a0e807e7bbff3a0d12";csrftoken=q3TYx570a6XMzpGjW7rp8EKudZTz8cuT;rur="VLL\05467648447369\0541753854396:01f7d923af2ad05024141cdcd4f92fbc27823d298eaa7fb34403a435bc59c4a0ac208561";ps_l=1;mid=Zqh-CgALAAF2bYI77LtgoVLeDDYH;wd=725x559;ig_did=26FB44F4-ED0E-4EDD-A719-AF85D21B2261;sessionid=58634573624%3AfCCgOGLZ6gTUPu%3A18%3AAYdNfqyB0AEOkQsM26KnBs4nRk0VcJQ7T9LgzyeYxQ;dpr=0.5;dpr=1.5;rur="CCO\05458634573624\0541754867897:01f76a0a1b1583695c2437645e7b84eaf2ef1b611afbf2c3cc1595cc6035a779c44a6dd4"')
# print(t.Comment('342336552406z1748172', 'test'))
        
