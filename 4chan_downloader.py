#!/usr/bin/env python3

#  Made by r4v10l1 (ch0colate)
#  https://github.com/r4v10l1

try:
	import requests, time, sys
	from bs4 import BeautifulSoup
	from colorama import Fore, Style
except Exception:
	exit(" [!] Error importing necesary modules: requests, random, string, time, bs4, sys")

############ EDIT ME ############
useTorProxy = False             #  << Put here True or False
debugPrint = False              #  << Put here True or False
sessionMode = False             #  << Put here True or False
#################################

def check_variable_types():
	if type(useTorProxy) is not bool:
		exit(" [!] The variable 'useTorProxy' must be a boolean.")
	elif type(debugPrint) is not bool:
		exit(" [!] The variable 'debugPrint' must be a boolean.")

def banner():
	print(f"{Style.BRIGHT}{Fore.GREEN}   __ __       __              ")
	print("  / // / _____/ /_  ____ _____ ")
	print(" / // /_/ ___/ __ \\/ __ `/ __ \\")
	print("/__  __/ /__/ / / / /_/ / / / /")
	print(f"  /_/  \\___/_/ /_/\\__,_/_/ /_/  {Style.RESET_ALL}{Fore.GREEN}Downloader{Style.RESET_ALL}")
	print()


def main():
	check_variable_types()
	banner()

	s = requests.Session() # Create a session because of the cookie

	if useTorProxy == False:
		proxies = ""
	elif useTorProxy == True:
		proxies = {'http': 'socks5://127.0.0.1:9150', 'https': 'socks5://127.0.0.1:9150'}
		try:
			if sessionMode:
				s.get("https://4chan.org/", proxies=proxies)
			else:
				requests.get("https://4chan.org/", proxies=proxies)
		except Exception:
		    exit(f" {Style.RESET_ALL}{Fore.RED}[!] We could not verify the proxies. Make sure tor is running.{Style.RESET_ALL}")

	try:
		board = input(f" {Style.BRIGHT}{Fore.BLUE}[i] Welcome to 4chan downloader! Type the board name: {Style.RESET_ALL}").lower()
	except KeyboardInterrupt:
		print()
		print(f"{Style.RESET_ALL}{Fore.RED} [!] Detected Ctrl+C. Exiting...{Style.RESET_ALL}")
		print()
		exit(1)
	print(f"{Style.RESET_ALL}{Fore.BLUE}     Starting at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL}")
	with open("4chan_debug.log", "a") as DebugLog:  # Append to the log file
		DebugLog.write("[%s] User started.\n" % time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()))
	print()
	pageNumber = 1
	img_scr_old = ""
	double_count = 0
	images = {"image/jpeg"}
	try:
		while True:
			URL = "https://boards.4channel.org/" + board + "/" + str(pageNumber)
			if pageNumber == 1:
				URL = "https://boards.4channel.org/" + board + "/"
			if sessionMode:
				r = s.get(URL, proxies=proxies, allow_redirects=True)
			else:
				r = requests.get(URL, proxies=proxies, allow_redirects=True)
			if "Attention Required! | Cloudflare" in r.text:
				exit(f" {Style.RESET_ALL}{Fore.RED}[!] Cloudflare captcha needed. Exiting...{Style.RESET_ALL}")
			souped = BeautifulSoup(r.text, 'html.parser')
			img_tags = souped.find_all('img')
			for img in img_tags:
				img_scr = img.get('src')
				if img_scr_old == img_scr:
					if double_count > 2:
						print(f"{Style.RESET_ALL}{Fore.BLUE}     All done.{Style.RESET_ALL}")
						print(f"{Style.RESET_ALL}{Fore.BLUE}     Stopping at "+ time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()) + f"{Style.RESET_ALL}")
					else:
						double_count += 1
				if debugPrint:
					print(f"IMG_SCR: {img_scr}\n")
				if f"i.4cdn.org/{board}" in img_scr:
					if "http" not in img_scr:
						img_scr = f"https:{img_scr}"
						img_id = img_scr.split("/")[-1].split(".")[0].replace("s", "")
						sys.stdout.write(f"\r {Style.RESET_ALL}{Style.BRIGHT}[{Fore.GREEN}+{Style.RESET_ALL}{Style.BRIGHT}] Downloading {Style.RESET_ALL}{Fore.GREEN}{img_id}{Style.RESET_ALL}")
						sys.stdout.flush()
						img_url = "https://i.4cdn.org/" + board + "/" + img_id + ".jpg"
						if debugPrint:
							print(f"IMG_URL: {img_url}\n")
						if sessionMode:
							r2 = s.get(img_url)
						else:
							r2 = requests.get(img_url)
						# print(r2.text)  # Inspect every request for debug
						if "Checking your browser" in r2.text:
							sys.stdout.write(f"\r {Style.RESET_ALL}{Style.BRIGHT}[{Fore.RED}!{Style.RESET_ALL}{Style.BRIGHT}] 4chan is requesting a human verification for image: {Fore.RED}{img_id}{Style.RESET_ALL}")
							sys.stdout.flush()
							print()
						elif "404 Not Found" in r2.text:
							sys.stdout.write(f"\r {Style.RESET_ALL}{Style.BRIGHT}[{Fore.RED}!{Style.RESET_ALL}{Style.BRIGHT}] 4chan returned 404 for image: {Fore.RED}{img_id}{Style.RESET_ALL}")
							sys.stdout.flush()
							print()
						if r2.headers["content-type"] in images:
							with open("4chan_downloads/" + img_id + ".jpg", "wb") as i:
								i.write(r2.content)
				img_scr_old = img_scr
			pageNumber += 1

	except KeyboardInterrupt:
		print()
		print(f"{Style.RESET_ALL}{Fore.RED} [!] Detected Ctrl+C. Exiting...{Style.RESET_ALL}")
		print()
		exit(1)
	except Exception as e:
		with open("4chan_debug.log", "a") as DebugLog:  # Append to the log file
			DebugLog.write("[%s] Error: %s \n" % (time.strftime("%d %b %Y - %H:%M:%S", time.gmtime()), e))

main()
