import json
import random
import urllib.request

def get_random_proxy(proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a random proxy as per your need.
	"""
	if proxytype not in ["http", "socks4", "socks5"]:
		raise Exception("Invalid Proxy Type !!")
	if anonymity not in ["all", "elite", "anonymous", "transparent"]:
		raise Exception("Invalid Anonymity Level !!")
	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country=all&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res = urllib.request.urlopen(api1).read().decode('utf-8').split("\r\n")
	res = [i for i in res if i]
	random.shuffle(res)
	return res[0]

def get_proxy_list(no_of_proxies, proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list as per your need.
	"""
	if not no_of_proxies:
		raise Exception("Please specify the number of proxies you need !!")
	if str(type(no_of_proxies))!="<class 'int'>":
		raise Exception("Please enter a valid number of proxies you need !!")
	if proxytype not in ["http", "socks4", "socks5"]:
		raise Exception("Invalid Proxy Type !!")
	if anonymity not in ["all", "elite", "anonymous", "transparent"]:
		raise Exception("Invalid Anonymity Level !!")
	proxies = []
	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country=all&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res =  urllib.request.urlopen(api1).read().decode('utf-8').split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	if proxytype=="http":
		api2 = "http://spys.me/proxy.txt"
		res =  urllib.request.urlopen(api2).read().decode('utf-8').split("\n\n")[1].split("\r")[:-1][0].split("\n")
		res = [i for i in res if i]
		for line in res:
			temp = line.split(" ")
			if anonymity=="elite" and temp[1].split("-")[1] == "H":
				proxies.append(temp[0])
			elif anonymity=="anonymous" and temp[1].split("-")[1] == "A":
				proxies.append(temp[0])
			elif anonymity=="transparent" and temp[1].split("-")[1] == "N":
				proxies.append(temp[0])
			else:
				proxies.append(temp[0])
	if anonymity != "all":
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity
	else:
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype
	res =  urllib.request.Request(api3, headers={'User-Agent': 'Mozilla/5.0'})
	res = urllib.request.urlopen(res).read().decode('utf-8').split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	random.shuffle(proxies)
	if no_of_proxies>len(proxies):
		return proxies
	else:
		return proxies[:no_of_proxies]
def get_proxy_json(no_of_proxies, proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in a JSON format as per your need.
	"""
	proxies=get_proxy_list(no_of_proxies, proxytype, anonymity)
	proxydict = dict()
	for proxy in proxies:
		ipadd = proxy.split(":")[0]
		port = proxy.split(":")[1]
		if ipadd not in proxydict.keys():
			proxydict[ipadd] = port
	return json.dumps(proxydict)

def get_proxy_txt(filename, no_of_proxies, proxytype, anonymity):

	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in TXT file as per your need.
	"""

	proxies=get_proxy_list(no_of_proxies, proxytype, anonymity)
	fp = open(filename,"w")
	for proxy in proxies:
		fp.write(proxy+"\n")
	fp.close()
	return
