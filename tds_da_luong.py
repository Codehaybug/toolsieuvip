
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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Trao Đổi Sub Facebook V1{trang_nhat}
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
def ducthinh():print(f'{trang_nhat}═════════════════════════════════════════════════════')
def cv(coin):return '{:,}'.format(int(coin)).replace(',', '.')
def random_color():
    colors = [do, xanh_la, nau, xanh_duong, tim, xanh_ngoc, xam_nhat, xam_dam, do_nhat, xanh_la_nhat, vang, xanh_duong_nhat, tim_nhat, hong, xanh_ngoc_nhat, trang_nhat]
    return random.choice(colors)
def HoanThanh(dem, id, type, msg, xu):
    xuNow = '{:,}'.format(int(xu)).replace(',', '.')
    timeNow = datetime.now().strftime("%H:%M:%S") 
    print(f"{vang}[{random_color()}D{random_color()}T{vang}]{do_nhat} | {trang}[ {vang}{dem}{trang} ] {do_nhat}| {xanh_ngoc}{type} {do_nhat}| {hong}{id} {do_nhat}| {vang}{msg} {do_nhat}| {nau}{timeNow} {do_nhat}| {xanh_la_nhat}XU : {vang}{xuNow} {do_nhat}|")

def InputFacebook():
    listCK = []
    dem = 1
    while True:
        cookieFB = input(f'{xanh_la_nhat}Nhập {vang}Cookie {xanh_la_nhat}Facebook {vang}{dem}{xanh_la_nhat} : {trang}')
        if len(cookieFB) < 3:break
        if 'c_user' not in cookieFB:print(f'{do_nhat}Cookie Sai Định Dạng!');ducthinh()
        fb = FacebookV2(cookieFB)
        log = fb.FilterData
        if log[0] == True:
            idUser = log[1]
            print(f'{xanh_la_nhat}Đăng Nhập Thành Công Tài Khoản ID : {vang}{idUser}{xanh_la_nhat} !')
            listCK.append(cookieFB)
            ducthinh()
            dem+=1
        else:
            print(f'{do_nhat}Cookie Die Hoặc Không Tồn Tại!')
            ducthinh()
    with open('ckfb_Jiray.txt', 'w', encoding='utf-8') as f:
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
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [.....]                                                  ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•....]                                                    ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [••...]                                                   ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•••..]                                                      ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [••••.]                                                     ", end='\r')
        sleep(1/6)
        print(f"{vang}[{hong}J{xanh_ngoc}I{xanh_duong}R{nau}A{xanh_la}Y{vang}] {do_nhat}| {xanh_ngoc}KÍCH HOẠT TÍNH NĂNG CHỐNG BLOCK, ĐANG ĐỢI → {random_color()}{delaybl} [•••••]                                                     ", end='\r')
        sleep(1/6)
        delaybl -= 1
def nghingoi(delaymin, delaymax):
    delay = randint(delaymin, delaymax)
    while delay > 0:
        print(f"{vang}[{xanh_la}<{xanh_duong_nhat}DUCTHINHEXE{xanh_la}>{vang}]{vang}[{trang}{delay}{vang}]                                                                      ", end='\r')
        sleep(1)
        delay-=1
def ClearCookie(cookie):
    with open('ckfb_Jiray.txt', 'r') as f:
        a = json.load(f)
    if cookie in a:
        a.remove(cookie)
    with open('ckfb_Jiray.txt', 'w', encoding="utf-8") as f:
        json.dump(a, f)
##########################################
class FacebookV2:
    def __init__(self, cookieFB) -> None:
        self.cookie     = cookieFB
    @property
    def FilterData(self):
        response = requests.get("https://mbasic.facebook.com/profile.php",headers = {"Cookie":self.cookie}).text
        try:
            self.fb_dtsg = response.split('input type="hidden" name="fb_dtsg" value="')[1].split('"')[0]
            self.jazoest = response.split('input type="hidden" name="jazoest" value="')[1].split('"')[0]
            self.idAcc   = response.split('input type="hidden" name="target" value="')[1].split('"')[0]
            return True, self.idAcc
        except:
            return False, '?'
    def Follow(self, idFollow):
        data = {
                'av': self.idAcc,
                'dpr': '1',
                'fb_dtsg': self.fb_dtsg,
                'jazoest': self.jazoest,
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'CometUserFollowMutation',
                'variables': '{"input":{"attribution_id_v2":"ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1700578539103,293844,190055527696468,,","is_tracking_encrypted":false,"subscribe_location":"PROFILE","subscribee_id":"'+idFollow+'","tracking":null,"actor_id":"'+self.idAcc+'","client_mutation_id":"1"},"scale":1}',
                'server_timestamps': 'true',
                'doc_id': '6792650737481329',
            }
        headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Chromium\";v\u003d\"107\", \"Not\u003dA?Brand\";v\u003d\"24\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "afdisHHGuglOo_hNSDt3Fb","x-fb-friendly-name": "CometUserFollowMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/"+idFollow,"accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
        try:
            fl = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data)
            if 'IS_SUBSCRIBED' in fl.text:
                return True
            else:
                return False
        except:
            return False
    def Reaction(self, typeReaction, idPost):
        if typeReaction == "LIKE" : idReaction = "1635855486666999"
        if typeReaction == "LOVE" : idReaction = "1678524932434102"
        if typeReaction == "CARE" : idReaction = "613557422527858"
        if typeReaction == "HAHA" : idReaction = "115940658764963"
        if typeReaction == "WOW"  : idReaction = "478547315650144"
        if typeReaction == "SAD"  : idReaction = "908563459236466"
        if typeReaction == "ANGRY": idReaction = "444813342392137"
        headers = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="119.0.6045.160", "Chromium";v="119.0.6045.160", "Not?A_Brand";v="24.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
            'viewport-width': '608',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'CometUFIFeedbackReactMutation',
        }
        feedback_id = base64.b64encode(f"feedback:{idPost}".encode('utf-8')).decode('utf-8')
        data = {
            'av': self.idAcc,
            'dpr': '1',
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometUFIFeedbackReactMutation',
            'variables': '{"input":{"attribution_id_v2":"CometSinglePostRoot.react,comet.post.single,unexpected,1700580020739,357744,,,;CometHomeRoot.react,comet.home,tap_tabbar,1700580012191,775076,4748854339,229#230#340#301,","feedback_id":"'+feedback_id+'","feedback_reaction_id":"'+idReaction+'","feedback_source":"OBJECT","feedback_referrer":"/","is_tracking_encrypted":true,"tracking":["AZUWSff9IbOm7WYclNQ8Rdp3OiHQE93bPuGbIeTR-oR1dbegBG8_sAyrLAGv-lgtY5fJC2-VkDf3ET6NmkBl2ei3nAQfEtQb_Q-EWXdqExUrA4BwTdTja6w0IPHUbxfaakMAnDkPuc_d4-wxEGvRR4yYcw-AxqgxSCgyy76QJEjmMe8TtO-wLkbErMHEfWIlOEBEXX032c_5DMP5jLUoF-raGeDOZjSfNFqDPjiHOLCIF44pMODEmPwymgh40ypXG549DZslL_8NBXk-GNJDk-ozcClD4DfwyldPBYia1nv416ZD1EOM3cXeSgCQxZw5iATdTAlyxdX4CohdPNTf0Tl4XlREHJ7wFa8Q3HWwJstV4lLO3NMthPCQD6WA2aMvzh7XqVU42HOWhaoZWOmTu8XKjrcFTwimPHwuSJSaaSompUxYVEF8wwKBE5f0Wxhznp2gqXM_ff5kLmlBMpl4ZKJ7V5krGl37ToKFjBROyv0IXN7DQ1nRaa3uSLGMd1dPAi8fMjeBLUcuJKIgWulqx-J_H1foC8bFNxYqYA802aqGdhauF1CPLlO1fKWCayresorODNgLx_VolhhjfK34oiW2O1fgVqZCtYH8YaGeUY5_MvrCosOVyaNwDa0jrswco8tW0hNA_7q7HdqC6CoPS3RWJExFJr4O7NShfL5asubUpdkwncHHCJH4jGwCDfaWMhuYOHKt-ozn9NOllhj5bzYS4vPuctZddFTnRnUZXEV6TuGhP97B4fBoSsF3din7G8ix7GyF-OGs9KqxzH0gVHGb34m_yoV09a7E7a3BEhTZ3tCzan1qc_b25VFQy5uAjQLwuRvjA3n12AvhSF_QnRGeiPO6ixTQr58fV3irNNl692WWpK10FKkH18nZzyRfDPFKEbjuVD2443GxrLKrAvfaWKYqHvrb72dAkyndzms10x79Z723DE6olaGQD_Ck5DBnhDZvGE0AwmI22GWXrv1Fv1ukoubed0_fe3Du7eQXxL9CJXgWdu0hy-ycqeHXW5jnuyKBvtLp8JnOGrWJF_FBnwkAC2sBECkSN2Rx8F8f0BtHMLn1aQcYW5Ji7EyGS2WXAf86ejs5XI5TX5_7KBf8qDg2Ys5cCKjv90H66_9pUGcWI9cbvFAt6Y_VlksehEkJHJSX3hJVnTsxQNIukfQomAFQhDYpxVvl6XcWpN68--v5Oq2j25hSX_EEnORiUHFlYf6dzs5ZYzKXkEj7Rpsii3_ZT5MoOu53Pz2ubzFGr6fG4OmxfXI1qnjzVBTofiQFBJjZ7YTUDK6MF9v-wTf0"],"session_id":"'+str(uuid.uuid4())+'","actor_id":"'+self.idAcc+'","client_mutation_id":"3"},"useDefaultActor":false,"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6880473321999695',
        }

        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        if feedback_id in response.text:
            return True
        else:
            return False
    def JoinGroup(self, idGroup):
        headers = {"Host": "www.facebook.com","sec-ch-ua": "\"Not?A_Brand\";v\u003d\"8\", \"Chromium\";v\u003d\"108\", \"Google Chrome\";v\u003d\"108\"","sec-ch-ua-mobile": "?0","user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36","viewport-width": "980","content-type": "application/x-www-form-urlencoded","x-fb-lsd": "gKT7R4dxIBjI4wUDUP5ivT","x-fb-friendly-name": "GroupCometJoinForumMutation","sec-ch-prefers-color-scheme": "dark","sec-ch-ua-platform": "\"Linux\"","accept": "*/*","origin": "https://www.facebook.com","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://www.facebook.com/groups/"+idGroup+"/","accept-language": "vi-VN,vi;q\u003d0.9,fr-FR;q\u003d0.8,fr;q\u003d0.7,en-US;q\u003d0.6,en;q\u003d0.5","cookie":self.cookie}
        data = {
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'GroupCometJoinForumMutation',
            'variables': '{"feedType":"DISCUSSION","groupID":"'+idGroup+'","imageMediaType":"image/x-auto","input":{"action_source":"GROUPS_ENGAGE_TAB","attribution_id_v2":"GroupsCometCrossGroupFeedRoot.react,comet.groups.feed,tap_tabbar,1667116100089,433821,2361831622,","group_id":"'+idGroup+'","group_share_tracking_params":null,"actor_id":"'+self.idAcc+'","client_mutation_id":"2"},"inviteShortLinkKey":null,"isChainingRecommendationUnit":false,"isEntityMenu":false,"scale":1,"source":"GROUPS_ENGAGE_TAB","renderLocation":"group_mall","__relay_internal__pv__GlobalPanelEnabledrelayprovider":false,"__relay_internal__pv__GroupsCometEntityMenuEmbeddedrelayprovider":true}',
            'server_timestamps': 'true',
            'doc_id': '5915153095183264',
        }
        try:
            join = requests.post('https://www.facebook.com/api/graphql/',headers=headers, data=data).text
            if self.idAcc in join:
                return True
            else:
                return join
        except:
            return False 
    def Comment(self, idPost, text):
        rs = requests.get(f'https://mbasic.facebook.com/{idPost}', cookies={'Cookie':self.cookie}).text
        try:
            eav                 = rs.split('eav=')[1].split('"')[0]
            ft_ent_identifier   = rs.split('ft_ent_identifier=')[1].split('&')[0]
            gfid                = rs.split('gfid=')[1].split('&')[0]
            data = {
                    'fb_dtsg': self.fb_dtsg,
                    'jazoest': self.jazoest,
                    'comment_text': text,
            }
            response = requests.post(f'https://mbasic.facebook.com/a/comment.php?fs=7&actionsource=2&comment_logging&ft_ent_identifier={ft_ent_identifier}&eav={eav}&av={self.idAcc}&gfid={gfid}&paipv=0&refid=13',cookies={'Cookie':self.cookie},data=data).text
            if 'Bạn tạm thời bị hạn chế' in response or 'Nếu bạn cho rằng nội dung này không vi phạm Tiêu chuẩn cộng đồng của chúng tôi' in response:
                return False
            else:
                return True
        except:
            return False
    def Share(self, idPost):
        UUID = str(uuid.uuid4())
        rs = requests.get(f'https://mbasic.facebook.com/{idPost}', cookies={'Cookie':self.cookie}).text
        try:
            eav   = rs.split('eav=')[1].split('"')[0]
            files = {
                    'fb_dtsg': (None, self.fb_dtsg),
                    'jazoest': (None, self.jazoest),
                    'at': (None, ''),
                    'target': (None, self.idAcc),
                    'csid': (None, UUID),
                    'c_src': (None, 'share'),
                    'referrer': (None, 'permalink'),
                    'ctype': (None, 'advanced'),
                    'cver': (None, 'amber_share'),
                    'users_with': (None, ''),
                    'album_id': (None, ''),
                    'waterfall_source': (None, 'advanced_composer_timeline'),
                    'privacyx': (None, '300645083384735'),
                    'appid': (None, '0'),
                    'sid': (None, idPost),
                    'linkUrl': (None, ''),
                    'm': (None, 'self'),
                    'xc_message': (None, ''),
                    'view_post': (None, 'Chia sẻ'),
                    'shared_from_post_id': (None, idPost),
            }
            response = requests.post(f'https://mbasic.facebook.com/composer/mbasic/?csid='+UUID+'&incparms%5B0%5D=xc_message&av='+self.idAcc+'&eav='+eav+'&paipv=0',cookies={'Cookie':self.cookie},files=files).text
            if 'Bạn tạm thời bị hạn chế' in response or 'Nếu bạn cho rằng nội dung này không vi phạm Tiêu chuẩn cộng đồng của chúng tôi' in response:
                return False
            else:
                return True
        except:
            return False
    def Page(self, idPage):
        headers = {
            'accept': '*/*',
            'accept-language': 'vi-VN,vi;q=0.9,fr-FR;q=0.8,fr;q=0.7,en-US;q=0.6,en;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': self.cookie,
            'origin': 'https://www.facebook.com/api/graphql',
            'priority': 'u=1, i',
            'referer': f'https://www.facebook.com/profile.php?id={idPage}',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
            'sec-ch-ua-full-version-list': '"Not)A;Brand";v="99.0.0.0", "Google Chrome";v="127.0.6533.73", "Chromium";v="127.0.6533.73"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"10.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'CometProfilePlusLikeMutation',
        }
        data = {
            'av': self.idAcc,
            'fb_dtsg': self.fb_dtsg,
            'jazoest': self.jazoest,
            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'CometProfilePlusLikeMutation',
            'variables': '{"input":{"is_tracking_encrypted":false,"page_id":"'+idPage+'","source":null,"tracking":null,"actor_id":"'+self.idAcc+'","client_mutation_id":"10"},"scale":1}',
            'server_timestamps': 'true',
            'doc_id': '6716077648448761',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', headers=headers, data=data)
        if "IS_SUBSCRIBED" in response.text:
            return True
        else:
            return False
    def ReactionComment(self, id, typeReaction):
        index = None
        retry = 0
        access = ""
        url = requests.get("https://mbasic.facebook.com/" + id, cookies={'cookie': self.cookie}).url
        if id in url:
            return False
        else:
            pass
        index = 1 if typeReaction == "LIKE" else 2 if typeReaction == "LOVE" else 3 if typeReaction == "CARE" else 4 if typeReaction == "HAHA" else 5 if typeReaction == "WOW" else 6 if typeReaction == "SAD" else 7
        access = requests.get(url, cookies={'cookie': self.cookie}).text
        try:
            while retry < 10:
                if id in access:
                        find_cmt = access.split(id)[1].split('</a></span></span>')[0].split('/reactions/picker/?')[1].split('"')[0].replace("amp;", "")
                        access = requests.get("https://mbasic.facebook.com/reactions/picker/?" + find_cmt, cookies={'cookie': self.cookie}).text
                        ufi = access.split('/ufi/reaction/?')
                        hoan_thanh = requests.get("https://mbasic.facebook.com/ufi/reaction/?" + ufi[index].split('"')[0].replace("amp;", ""), cookies={'cookie': self.cookie}).text
                        if 'Bạn tạm thời bị hạn chế' in hoan_thanh or 'Nếu bạn cho rằng nội dung này không vi phạm Tiêu chuẩn cộng đồng của chúng tôi' in hoan_thanh:
                            return False
                        else:
                            return True
                else:
                    if "/comment/replies/" in url:
                        xemthemcmt = access.split('/comment/replies/?')[1].split('"')[0].replace("amp;", "")
                        access = requests.get("https://mbasic.facebook.com/comment/replies/?" + xemthemcmt, cookies={'cookie': self.cookie}).text
                    else:
                        xemthemcmt = access.split('/story.php?')[1].split('</a></div></div>')[0].replace("amp;", "").split('"')[0]
                        access = requests.get("https://mbasic.facebook.com/story.php?" + xemthemcmt, cookies={'cookie': self.cookie}).text
                    retry += 1
            return False
        except:
            return False
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
        return requests.get(self.baseUrl + f'api/?fields={typejob}&access_token={self.tokenTDS}').json()
    def GetCoin(self, idJob, type):
        typejob = type.upper()
        response =  requests.get(self.baseUrl + f'api/coin/?type={typejob}&id={idJob}&access_token={self.tokenTDS}')
        if "success" in response.text:
            xuNow, msg = response.json()['data']['xu'], response.json()['data']['msg']
            return True, xuNow, msg
        else:
            return False, '?'
    def CauHinh(self, id):
        rs = requests.get(self.baseUrl + f'api/?fields=run&id={id}&access_token={self.tokenTDS}')
        if 'success' in rs.text:
            return True
        else:
            return False
#########################################
os.system("cls" if os.name == "nt" else "clear")
banner()
while True:
    if os.path.exists('infoTDS_Jiray.txt'):
        with open('infoTDS_Jiray.txt', 'r') as f:
            tokenTDS = f.read().strip()
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
    if os.path.exists('ckfb_Jiray.txt'):
        with open('ckfb_Jiray.txt', 'r') as f:
            line = json.load(f)
        if len(line) == 0:os.remove('ckfb_Jiray.txt');file = open('ckfb_Jiray.txt', 'a').close()
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}1{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Giữ Lại FB")
        print(f"{trang}→ {xanh_la_nhat}Nhập Số {hong}[ {trang}2{xanh_la_nhat}{hong} ] {xanh_la_nhat}Để Đổi Tài Khoản FB")
        chon = input(f'{vang}[{trang}~{xanh_ngoc}.{trang}~{vang}] {xanh_la_nhat}Nhập Lựa Chọn : {trang}')
        if int(chon) == 1:
            break
        elif int(chon) == 2:
            os.remove('ckfb_Jiray.txt')
        else:
            print(f'{do_nhat}Lựa Chọn Không Hợp Lệ!')
            ducthinh()
    if not os.path.exists('ckfb_Jiray.txt'):
        open('ckfb_Jiray.txt', 'a').close()
        InputFacebook()
        break
time.sleep(1)
banner()
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}1{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}LIKE')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}2{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}REACTION')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}3{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}REACTION COMMENT')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}4{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}COMMENT')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}5{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}FOLLOW')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}6{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}SHARE')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}7{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}GROUP')
print(f'{xanh_la_nhat}Nhập Số {nau}[ {trang}8{nau} ] {xanh_la_nhat}Chạy Nhiệm Vụ {vang}PAGE')
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
######### VARIABLE ###########
tokenTDS = line[0]
tds = TraoDoiSub(tokenTDS)
xuNow = tds.Login[2]
dem, blocked = 1, 0
listJob = [int(j) for j in str(nhiemvu)]
linesCookie = {}
with open('ckfb_Jiray.txt', 'r', encoding="utf-8") as f:
    listCK = json.load(f)
for cookie in listCK:
    linesCookie[cookie] = {
        'LIKE'      : True,
        'COMMENT'   : True,
        'REACTCMT'  : True,
        'FOLLOW'    : True,
        'REACTION'  : True,
        'PAGE'      : True,
        'GROUP'     : True,
        'SHARE'     : True
    }
while(True):
        u = list(linesCookie.keys())
        for cookie in u:
            errorLike, errorReactCMT, errorFollow, errorReaction, errorPage, errorGroup, errorComment, errorShare, doiacc = 0, 0, 0, 0, 0, 0, 0, 0, 0
            fb = FacebookV2(cookie)
            check = fb.FilterData
            if check[0] == True:
                idUser = check[1]
                tds.CauHinh(idUser)
                print(f'{xanh_la_nhat}UID : {vang}{idUser} {xanh_la_nhat}<> XU : {vang}{xuNow} {xanh_la_nhat}<> Tổng Cookie : {vang}{len(u)}       ')
                ducthinh()
                while True:
                    nv = random.choice(listJob)
                    if nv == 1:
                        if linesCookie[cookie]['LIKE'] == False:continue
                        if errorLike == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block LIKE               ')
                            linesCookie[cookie]['LIKE'] = False
                            ducthinh()
                            continue
                        getT = random.choice(['like', 'likegiare', 'likesieure'])
                        get = tds.GetJob(getT)
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ {getT.upper()}, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ {getT.upper()} : {trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ {getT.upper()}{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ {getT.upper()}              ', end='\r')
                                for job in get:
                                    if errorLike == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block LIKE               ')
                                        linesCookie[cookie]['LIKE'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:
                                        break
                                    job = job['id']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Reaction('LIKE', idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, getT)
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, getT.upper(), msg, xuNow)
                                            errorLike = 0
                                            dem += 1
                                            doiacc +=1
                                            blocked +=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - {getT.upper()}               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorLike+=1
                                        print(f'{do_nhat}LIKE Thất Bại : {job} - {trang_nhat}{errorLike}/5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 3:
                        if linesCookie[cookie]['REACTCMT'] == False:continue
                        if errorReactCMT == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block REACTION CMT               ')
                            linesCookie[cookie]['REACTCMT'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('reactcmt')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ REACT CMT, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Lấy Nhiệm Vụ REACT CMT{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ REACT CMT{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ REACT CMT              ', end='\r')
                                for z in get:
                                    if errorReactCMT == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block REACTION CMT               ')
                                        linesCookie[cookie]['REACTCMT'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    typeReaction = z['type']
                                    like = fb.ReactionComment(job, typeReaction)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, f"{str(typeReaction).upper()}CMT")
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, job, f"{str(typeReaction).upper()}CMT", msg, xuNow)
                                            errorReactCMT = 0
                                            dem += 1
                                            blocked +=1
                                            doiacc+=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - {str(typeReaction).upper()}CMT              ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorReactCMT+=1
                                        print(f'{do_nhat}{str(typeReaction).upper()}CMT Thất Bại : {job} - {trang_nhat}{errorReactCMT}/5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 2:
                        if linesCookie[cookie]['REACTION'] == False:continue
                        if errorReaction == 5:
                                print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block REACTION               ')
                                linesCookie[cookie]['REACTION'] = False
                                ducthinh()
                                continue
                        get = tds.GetJob('reaction')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ REACTION, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ REACTION{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ REACTION{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ REACTION             ', end='\r')
                                for z in get:
                                    if errorReaction == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block REACTION               ')
                                        linesCookie[cookie]['REACTION'] = False
                                        ducthinh()
                                        break;break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    typez = z['type']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Reaction(typez, idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, typez)
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, typez, msg, xuNow)
                                            errorReaction = 0
                                            dem += 1
                                            blocked +=1
                                            doiacc+=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - REACTION               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorReaction+=1
                                        print(f'{do_nhat}REACTION Thất Bại : {job} - {trang_nhat}{errorReaction}/5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 4:
                        if linesCookie[cookie]['COMMENT'] == False:continue
                        if errorComment == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block COMMENT               ')
                            linesCookie[cookie]['COMMENT'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('comment')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ COMMENT, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ COMMENT{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ COMMENT{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ COMMENT             ', end='\r')
                                for z in get:
                                    if errorComment == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block COMMENT               ')
                                        linesCookie[cookie]['COMMENT'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    msg = z['msg']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Comment(idjob, msg)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, 'comment')
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, 'COMMENT', msg, xuNow)
                                            errorComment = 0
                                            dem += 1
                                            blocked +=1
                                            doiacc+=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - COMMENT               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorComment+=1
                                        print(f'{do_nhat}COMMENT Thất Bại : {job} - {trang_nhat}{errorComment} / 5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 5:
                        if linesCookie[cookie]['FOLLOW'] == False:continue
                        if errorFollow == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block FOLLOW               ')
                            linesCookie[cookie]['FOLLOW'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('follow')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ FOLLOW, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ FOLLOW{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ FOLLOW{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ FOLLOW             ', end='\r')
                                for z in get:
                                    if errorFollow == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block FOLLOW               ')
                                        linesCookie[cookie]['FOLLOW'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc  == doinick:break
                                    job = z['id']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Follow(idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, 'follow')
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, 'FOLLOW', msg, xuNow)
                                            errorFollow = 0
                                            dem += 1
                                            doiacc+=1
                                            blocked +=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - FOLLOW               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorFollow+=1
                                        print(f'{do_nhat}FOLLOW Thất Bại : {job} - {trang_nhat}{errorFollow}/5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 6:
                        if linesCookie[cookie]['SHARE'] == False:continue
                        if errorShare == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block SHARE               ')
                            linesCookie[cookie]['SHARE'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('share')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ SHARE, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ SHARE{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ SHARE{trang_nhat}         ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ SHARE             ', end='\r')
                                for z in get:
                                    if errorShare == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block SHARE               ')
                                        linesCookie[cookie]['SHARE'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Share(idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, 'share')
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, 'SHARE', msg, xuNow)
                                            errorShare = 0
                                            dem += 1
                                            blocked +=1
                                            doiacc+=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - SHARE               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorShare+=1
                                        print(f'{do_nhat}SHARE Thất Bại : {job} - {trang_nhat}{errorShare}/5              ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 7:
                        if linesCookie[cookie]['GROUP'] == False:continue
                        if errorGroup == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block GROUP               ')
                            linesCookie[cookie]['GROUP'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('group')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ GROUP, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ GROUP{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ GROUP{trang_nhat}          ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ GROUP             ', end='\r')
                                for z in get:
                                    if errorGroup == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block GROUP               ')
                                        linesCookie[cookie]['GROUP'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.JoinGroup(idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, 'group')
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, 'GROUP', msg, xuNow)
                                            dem += 1
                                            doiacc+=1
                                            blocked +=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - GROUP               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorGroup+=1
                                        print(f'{do_nhat}GROUP Thất Bại : {job} - {trang_nhat}{errorGroup}/5               ', end='\r')
                                        time.sleep(0.5)
                    elif nv == 8:
                        if linesCookie[cookie]['PAGE'] == False:continue
                        if errorPage == 5:
                            print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block PAGE               ')
                            linesCookie[cookie]['PAGE'] = False
                            ducthinh()
                            continue
                        get = tds.GetJob('page')
                        if 'error' in get:
                            try:
                                countdown = get['countdown']
                                print(f'{do_nhat}Đang Lấy Nhiệm Vụ PAGE, Countdown : {trang_nhat}{countdown}         ', end='\r');continue
                                time.sleep(1)
                            except:
                                msg = get['error']
                                print(f'{xanh_la_nhat}Đang Get Nhiệm Vụ PAGE{trang_nhat}{msg}          ', end='\r')
                                time.sleep(1)
                        else:
                            if len(get) == 0:
                                print(f'{do_nhat}Đã Hết Nhiệm Vụ PAGE{trang_nhat}            ', end='\r')
                            else:
                                print(f'{xanh_la_nhat}Đã Tìm Thấy {vang}{len(get)} {xanh_la_nhat}Nhiệm Vụ PAGE             ', end='\r')
                                for z in get:
                                    if errorPage == 5:
                                        print(f'{do_nhat}Cookie ID : {vang}{idUser}{do_nhat} Đã Bị Block PAGE               ')
                                        linesCookie[cookie]['PAGE'] = False
                                        ducthinh()
                                        break
                                    if blocked == nvblock:
                                        break
                                    if doiacc == doinick:break
                                    job = z['id']
                                    idjob = job.split('_')[1] if '_' in job else job
                                    like = fb.Page(idjob)
                                    if like:
                                        time.sleep(0.055)
                                        nhan = tds.GetCoin(job, 'page')
                                        if nhan[0] == True:
                                            #return True, xuNow, msg#
                                            xuNow = nhan[1]
                                            msg   = nhan[2]
                                            HoanThanh(dem, idjob, 'PAGE', msg, xuNow)
                                            errorPage = 0
                                            dem += 1
                                            doiacc+=1
                                            blocked +=1
                                            nghingoi(delaymin, delaymax)
                                        else:
                                            print(f'{do_nhat}Nhận Thất Bại : {job} - PAGE               ', end='\r')
                                            time.sleep(0.5)
                                    else:
                                        errorPage+=1
                                        print(f'{do_nhat}PAGE Thất Bại : {job} - {trang_nhat}{errorPage}/5               ', end='\r')
                                        time.sleep(0.5)
                    else:
                        pass
                    if blocked == nvblock:
                        chongblock(dlblock)
                        blocked = 0
                    if doiacc == doinick:
                        ducthinh()
                        doiacc = 0
                        break
                    check = linesCookie[cookie]
                    if all(value is False for value in check.values()):
                        check = fb.FilterData[0]
                        if check:
                            print(f'{do_nhat}Tài khoản UID : {vang}{idUser}{do_nhat} Đã Bị Block Tính Năng!             ')
                            ClearCookie(cookie)
                            linesCookie.pop(cookie)
                            ducthinh()
                            break
                        else:
                            print(f'{do_nhat}Tài khoản UID : {vang}{idUser}{do_nhat} Đã Bị Die Cookie                ')
                            linesCookie.pop(cookie)
                            ClearCookie(cookie)
                            ducthinh()
                            break
                    else:pass
                    if len(linesCookie) == 0:
                        with open('ckfb_Jiray.txt', 'r') as f:
                            a = json.load(f)
                        if len(a) == 0:
                            os.remove('ckfb_Jiray.txt')
                            print(f'{do_nhat}Tất Cả Các Cookie Đã Die, Vui Lòng Điền Cookie Mới!')
                            ducthinh()
                            InputFacebook()
                            with open('ckfb_Jiray.txt', 'r', encoding="utf-8") as f:
                                listCK = json.load(f)
                            for cookie in listCK:
                                linesCookie[cookie] = {
                                    'LIKE'      : True,
                                    'COMMENT'   : True,
                                    'REACTCMT'  : True,
                                    'FOLLOW'    : True,
                                    'REACTION'  : True,
                                    'PAGE'      : True,
                                    'GROUP'     : True,
                                    'SHARE'     : True
                                }
                            with open('ckfb_Jiray.txt', 'r', encoding="utf-8") as f:
                                json.dump(linesCookie, f)
                            break
                        else:
                            pass
                    for i in range(10, -1, -1):
                        print(f'{xanh_duong}Đang Thực Hiện Lấy NV Sau {i} Giây....                                                                                                                                              ', end='\r')
                        time.sleep(1)
            else:
                try:
                    idUser = cookie.split('c_user=')[1].split(';')[0]
                    print(f'{do_nhat}Cookie ID : {idUser} Đã Bị Die                 ')
                    linesCookie.pop(cookie)
                    ClearCookie(cookie)
                    ducthinh()
                    break
                except:
                    print(f'Cookie Này Die Rui, Get Lại Nhé                 ')
                    linesCookie.pop(cookie)
                    ClearCookie(cookie)
                    ducthinh()
                    break
