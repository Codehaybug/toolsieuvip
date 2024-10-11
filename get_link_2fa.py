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
import requests, json
from urllib.parse import urlencode
import binascii, codecs, base64

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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Unlock 956 VIP{trang_nhat}
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
				return None, f"{do}Chức Năng Chỉ Dành Cho Người Dùng Key Vip! Muốn Sử Dụng Hãy Lên JirayShop.Xyz Để Thuê Key!"
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
elif checkKey[0] == None:
    msg = checkKey[1]
    print(msg)
    exit()
else:
	key = checkKey[1]
	date = checkKey[2]

############## FUNCTION #################
def banner():
    t.Logo(key, date)
def ducthinh():print(f'{trang_nhat}═════════════════════════════════════════════════════')
def GetLink956(cookies):
    try:
        get = requests.get('https://www.facebook.com/checkpoint/828281030927956/', cookies={'Cookie':cookies}).text
        fb_Dtsg = get.split('DTSGInitialData",[],{"token":"')[1].split('"')[0]

        headers = {
                "accept": "*/*",
                "accept-language": "en-US,en;q=0.9",
                "content-type": "application/x-www-form-urlencoded",
                "priority": "u=1, i",
                "sec-ch-prefers-color-scheme": "light",
                "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Google Chrome\";v=\"128\"",
                "sec-ch-ua-full-version-list": "\"Chromium\";v=\"128.0.6613.115\", \"Not;A=Brand\";v=\"24.0.0.0\", \"Google Chrome\";v=\"128.0.6613.115\"",
                "sec-ch-ua-mobile": "?0",
                "sec-ch-ua-model": "\"\"",
                "sec-ch-ua-platform": "\"Windows\"",
                "sec-ch-ua-platform-version": "\"10.0.0\"",
                "sec-fetch-dest": "empty",
                "sec-fetch-mode": "cors",
                "sec-fetch-site": "same-origin",
                "x-asbd-id": "129477",
                "x-fb-friendly-name": "CometIXTFacebookAuthenticityWizardTriggerRootQuery",
                "x-fb-lsd": "OrwB6dDflbN5HVhfuhfISH"
            }
        body = {
            "__a": "1",
            "fb_dtsg": fb_Dtsg,
            "variables": urlencode({
                "input": {
                    "authenticity_product": "LOGIN_APPROVALS_SELFIE",
                    "country": None,
                    "location": "CHECKPOINT_FRAMEWORK",
                    "logger_session_id": None,
                    "msite_handoff_id": None,
                    "next_uri": None,
                    "security_token": None,
                    "trigger_event_type": "AUTHENTICITY_WIZARD_TRIGGER",
                    "nt_context": None,
                    "trigger_session_id": "3e0f3214-2aeb-4d0e-bcb0-294169da4420"
                },
                "scale": 1
            }),
            "server_timestamps": "true",
            "doc_id": "8517192768300807"
        }

        response = requests.post("https://www.facebook.com/api/graphql/", headers=headers, data=body)
        data = response.json()
        serialized_state = data['data']['ixt_authenticity_wizard_trigger']['screen']['view_model']['serialized_state']
        link = f"https://m.facebook.com/ixt/renderscreen/msite/?serialized_state={serialized_state}"
        return link
    except:
        return False
banner()
print(f'{xanh_la}( !! ) ĐÂY LÀ TOOL HỖ TRỢ LẤY LINK UP VIDEO SELFIE 956')
print(f'{xanh_la}( !! ) NÊN KHÔNG CHẮC CHẮN SẼ ĐÁP 100%, TOOL CHỈ HỖ TRỢ BẠN TỚI 80%')
print(f'{xanh_la}( !! ) VIỆC UNLOCK CÓ ĐÁP HAY KHÔNG LÀ DO BẠN, CHÚC MAY MẮN!')
ducthinh()
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập [\033[1;33m1\033[1;32m] Lấy 1 Link' )
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập [\033[1;33m2\033[1;32m] Lấy Nhiều Link')
chon = int(input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập \033[1;37m===>:\033[1;33m '))
if chon > 2 or chon < 0:
    print(f'{do}Vui Lòng Chọn Đúng Với Các Tùy Chọn!')
    exit()
time.sleep(1)
banner()
if chon == 1:
    while True:
        cookie = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Cookie Facebook : \033[1;33m ')
        get = GetLink956(cookie)
        if get == False:
            token = get
            print(f"""{trang}═══════════════════════════════════════════════════════""")
            print(f'\033[1;32mLỖI ===>{do}Cookie Die Hoặc Sai\033[1;33m')
        else:
            msg = get[1]
            print(f"""{trang}═══════════════════════════════════════════════════════""")
            print(f'\033[1;32mLINK ===> {trang}{get}\033[1;33m')
        choose = input('\033[1;37mTiếp Tục Get LINK ? ( Y / N ) :')
        if choose.upper() != "Y" and choose.upper() != "N":
            print(f'{do}Vui Lòng Chọn Đúng Với Các Tùy Chọn!')
            exit()
        else:
            if choose.upper() == "Y":
                print(f"""{trang}═══════════════════════════════════════════════════════""")
            else:
                print('CẢM ƠN BẠN VÌ ĐÃ SỬ DỤNG TOOL!')
                exit()

elif chon == 2:
    file = open('jiray-cookiefb.txt', 'a')
    input(f'{trang}Vui Lòng Thêm Các Cookie Vào File jiray-cookiefb.txt, Mỗi Cookie Một Dòng. Nếu Hoàn Thiện Vui Lòng Ấn Enter Để Tiếp Tục')
    banner()
    with open('jiray-cookiefb.txt', 'r') as fCookie:
        line = fCookie.read().split()
        if len(line) == 0:
            print(f'{do}Vui Lòng Thêm Cookie Vào File Sau Đó Thử Lại!')
            exit()
        else:
            for cookie in line:
                if "c_user=" not in cookie:
                    print(f"""{trang}═══════════════════════════════════════════════════════""")
                    print(f'{do}Cookie Sai Định Dạng')
                    continue
                else:
                    get = GetLink956(cookie)
                    if get == False:
                        print(f"""{trang}═══════════════════════════════════════════════════════""")
                        print(f'\033[1;32mLỖI ===>{do}Cookie Die Hoặc Sai\033[1;33m')
                    else:
                        print(f"""{trang}═══════════════════════════════════════════════════════""")
                        print(f'\033[1;32mLINK ===> {trang}{get}\033[1;33m')
            print('CẢM ƠN BẠN VÌ ĐÃ SỬ DỤNG TOOL!')
            exit()
