from Prawler import *
from optparse import OptionParser

banner = '''
  ____                     _           
 |  _ \ _ __ __ ___      _| | ___ _ __ 
 | |_) | '__/ _` \ \ /\ / / |/ _ \ '__|
 |  __/| | | (_| |\ V  V /| |  __/ |   
 |_|   |_|  \__,_| \_/\_/ |_|\___|_|     V0.47beta

'''
print(banner)
parser = OptionParser(usage="Usage: %prog [-n, --num <no of proxies>] [-o, --format <output format>] [-f, --filename <filename>] [-t, --proxytype <proxy type>] [-a, --anonymity <anonymity level>]",version="%prog 0.4beta")
parser.add_option("-n", "--num",dest="no_of_proxies", default=1, help="Number of proxies to generate", type="int")
parser.add_option("-o", "--format",dest="format", default="random", help="Output Format [list, json, txt]", type="str")
parser.add_option("-f", "--filename",dest="filename", default="proxy_list.txt", help="Output Filename [Default: proxy_list.txt]", type="str")
parser.add_option("-t", "--proxytype",dest="proxytype", default="http", help="Proxy Type [http, socks4, socks5] [Default: HTTP]", type="str")
parser.add_option("-a", "--anonymity",dest="anonymity", default="elite", help="Anonymity Level [all, elite, anonymous, transparent] [Default: all]", type="str")

(options, args) = parser.parse_args()

if options.proxytype not in ["http", "socks4", "socks5"]:
	parser.error("Invalid Proxy Type !!")
if options.anonymity not in ["all", "elite", "anonymous", "transparent"]:
	parser.error("Invalid Anonymity Level !!")
if options.format not in ["list", "json", "txt", "random"]:
	parser.error("Invalid Output Format !!")
if options.filename != "proxy_list.txt" and options.format != "txt":
	parser.error("Use 'txt' as output format before providing filename !!")

if options.format == "txt":
	print("[i] Generating {}".format(options.filename))
	get_proxy_txt(options.filename, options.no_of_proxies, options.proxytype, options.anonymity)
	print("[i] Done !!")

elif options.format == "json":
	print("[i] Generating JSON..\n")
	print(get_proxy_json(options.no_of_proxies, options.proxytype, options.anonymity))

elif options.format == "list":
	print("[i] Generating LIST..\n")
	print(get_proxy_list(options.no_of_proxies, options.proxytype, options.anonymity))

elif options.format == "random":
	print("[i] Random Proxy Server: {} [Proxy Type: {}] [Anonymity Level: {}]".format(get_random_proxy(options.proxytype, options.anonymity), options.proxytype, options.anonymity))