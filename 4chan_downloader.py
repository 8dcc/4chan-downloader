#!/usr/bin/env python3

#  Made by r4v10l1 (ch0colate)
#  https://github.com/r4v10l1

try:
	import requests, time, sys
	from bs4 import BeautifulSoup
except Exception:
	exit(" [!] Error importing necesary modules: requests, random, string, time, bs4, sys")

############ EDIT ME ############
useTorProxy = False             #  << Put here True or False
#################################

if useTorProxy == False:
	proxies = ""
elif useTorProxy == True:
	proxies = {'http': 'socks5://127.0.0.1:9150', 'https': 'socks5://127.0.0.1:9150'}
else:
	print()
	print(" [!] Error. Invalid proxy. Exiting...")
	print()
	exit(1)

def banner():
	print("   __ __       __              ")
	print("  / // / _____/ /_  ____ _____ ")
	print(" / // /_/ ___/ __ \\/ __ `/ __ \\")
	print("/__  __/ /__/ / / / /_/ / / / /")
	print("  /_/  \\___/_/ /_/\\__,_/_/ /_/  Downloader")
	print()

def main():
	banner()
	try:
		board = input(" [i] Welcome to 4chan downloader! Type the board name: ")
	except KeyboardInterrupt:
		print()
		print(" [!] Detected Ctrl+C. Exiting...")
		print()
		exit(1)
	print("     Starting at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	with open("4chan_debug.log", "a") as DebugLog:  # Append to the log file
		DebugLog.write("[%s] User started.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	print()
	pageNumber = 1
	can_download = False
	images = {"image/jpeg"}
	try:
		while True:
			URL = "https://boards.4channel.org/" + board + "/" + str(pageNumber)
			if pageNumber == 1:
				URL = "https://boards.4channel.org/" + board + "/"
			r = requests.get(URL, proxies=proxies, allow_redirects=True)
			souped = BeautifulSoup(r.text, 'html.parser')
			img_tags = souped.find_all('img')
			for img in img_tags:
				img_scr = img.get('src')
				if "vip" in img_scr:
					can_download = True
				if can_download:
					if "http" not in img_scr:
						img_scr = f"https:{img_scr}"
						img_id = img_scr.split("/")[-1].split(".")[0].replace("s", "")
						sys.stdout.write(" [+] Downloading " + img_id + "                                              ")
						sys.stdout.write('\b'*90)
						sys.stdout.flush()
						img_url = "https://i.4cdn.org/lgbt/" + img_id + ".jpg"
						r2 = requests.get(img_url)
						if r2.headers["content-type"] in images:
							with open("4chan_downloads/" + img_id + ".jpg", "wb") as i:
								i.write(r2.content)
			pageNumber += 1
	
	except KeyboardInterrupt:
		print()
		print(" [!] Detected Ctrl+C. Exiting...")
		print()
		exit(1)
	except Exception as e:
		with open("4chan_debug.log", "a") as DebugLog:  # Append to the log file
			DebugLog.write("[%s] Error: %s \n" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), e))

main()