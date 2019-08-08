import json
import random
import requests

def get_random_proxy(self, proxytype, anonymity):
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
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	random.shuffle(res)
	return res[0]

def get_proxy_list(self, proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list as per your need.
	"""
	if proxytype not in ["http", "socks4", "socks5"]:
		raise Exception("Invalid Proxy Type !!")
	if anonymity not in ["all", "elite", "anonymous", "transparent"]:
		raise Exception("Invalid Anonymity Level !!")
	proxies = []
	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country=all&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	if proxytype=="http":
		api2 = "http://spys.me/proxy.txt"
		res = requests.get(api2).text.split("\n\n")[1].split("\r")[:-1][0].split("\n")
		for line in res:
			temp = line.split(" ")
			if anonymity=="elite":
				if temp[1].split("-")[1] == "H":
					proxies.append(temp[0])
			elif anonymity=="anonymous":
				if temp[1].split("-")[1] == "A":
					proxies.append(temp[0])
			elif anonymity=="transparent":
				if temp[1].split("-")[1] == "N":
					proxies.append(temp[0])
			else:
				pass
	if anonymity != "all":
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity
	else:
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	random.shuffle(proxies)
	return proxies

def get_proxy_json(self, proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in a JSON format as per your need.
	"""
	if proxytype not in ["http", "socks4", "socks5"]:
		raise Exception("Invalid Proxy Type !!")
	if anonymity not in ["all", "elite", "anonymous", "transparent"]:
		raise Exception("Invalid Anonymity Level !!")
	proxies = []
	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country=all&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	if proxytype=="http":
		api2 = "http://spys.me/proxy.txt"
		res = requests.get(api2).text.split("\n\n")[1].split("\r")[:-1][0].split("\n")
		for line in res:
			temp = line.split(" ")
			if anonymity=="elite":
				if temp[1].split("-")[1] == "H":
					proxies.append(temp[0])
			elif anonymity=="anonymous":
				if temp[1].split("-")[1] == "A":
					proxies.append(temp[0])
			elif anonymity=="transparent":
				if temp[1].split("-")[1] == "N":
					proxies.append(temp[0])
			else:
				pass
	if anonymity != "all":
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity
	else:
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	random.shuffle(proxies)
	proxydict = dict()
	for proxy in proxies:
		ipadd = proxy.split(":")[0]
		port = proxy.split(":")[1]
		if ipadd not in proxydict.keys():
			proxydict[ipadd] = port
	return json.dumps(proxydict)

def get_proxy_txt(self, filename, proxytype, anonymity):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in TXT file as per your need.
	"""
	if proxytype not in ["http", "socks4", "socks5"]:
		raise Exception("Invalid Proxy Type !!")
	if anonymity not in ["all", "elite", "anonymous", "transparent"]:
		raise Exception("Invalid Anonymity Level !!")
	proxies = []
	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country=all&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	if proxytype=="http":
		api2 = "http://spys.me/proxy.txt"
		res = requests.get(api2).text.split("\n\n")[1].split("\r")[:-1][0].split("\n")
		for line in res:
			temp = line.split(" ")
			if anonymity=="elite":
				if temp[1].split("-")[1] == "H":
					proxies.append(temp[0])
			elif anonymity=="anonymous":
				if temp[1].split("-")[1] == "A":
					proxies.append(temp[0])
			elif anonymity=="transparent":
				if temp[1].split("-")[1] == "N":
					proxies.append(temp[0])
			else:
				pass
	if anonymity != "all":
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity
	else:
		api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype
	res = requests.get(api1).text.split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	random.shuffle(proxies)
	fp = open(filename,"w")
	for proxy in proxies:
		fp.write(proxy+"\n")
	fp.close()
	return