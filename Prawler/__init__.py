import json
import random
import urllib.request

valid_codes = ['AF', 'AL', 'AM', 'AR', 'AT', 'AU', 'BA', 'BD', 'BG', 'BO', 'BR', 'BY', 'CA', 'CL', 'CM', 'CN', 'CO', 'CZ', 'DE', 'EC', 'EG', 'ES', 'FR', 'GB', 'GE', 'GN', 'GR', 'GT', 'HK', 'HN', 'HU', 'ID', 'IN', 'IQ', 'IR', 'IT', 'JP', 'KE', 'KG', 'KH', 'KR', 'KZ', 'LB', 'LT', 'LV', 'LY', 'MD', 'MM', 'MN', 'MU', 'MW', 'MX', 'MY', 'NG', 'NL', 'NO', 'NP', 'PE', 'PH', 'PK', 'PL', 'PS', 'PY', 'RO', 'RS', 'RU', 'SC', 'SE', 'SG', 'SK', 'SY', 'TH', 'TR', 'TW', 'TZ', 'UA', 'UG', 'US', 'VE', 'VN', 'ZA']
# country_codes = {'Afghanistan': 'AF', 'Albania': 'AL', 'Algeria': 'DZ', 'American Samoa': 'AS', 'Andorra': 'AD', 'Angola': 'AO', 'Anguilla': 'AI', 'Antarctica': 'AQ', 'Antigua and Barbuda': 'AG', 'Argentina': 'AR', 'Armenia': 'AM', 'Aruba': 'AW', 'Australia': 'AU', 'Austria': 'AT', 'Azerbaijan': 'AZ', 'Bahamas (the)': 'BS', 'Bahrain': 'BH', 'Bangladesh': 'BD', 'Barbados': 'BB', 'Belarus': 'BY', 'Belgium': 'BE', 'Belize': 'BZ', 'Benin': 'BJ', 'Bermuda': 'BM', 'Bhutan': 'BT', 'Bolivia (Plurinational State of)': 'BO', 'Bonaire, Sint Eustatius and Saba': 'BQ', 'Bosnia and Herzegovina': 'BA', 'Botswana': 'BW', 'Bouvet Island': 'BV', 'Brazil': 'BR', 'British Indian Ocean Territory (the)': 'IO', 'Brunei Darussalam': 'BN', 'Bulgaria': 'BG', 'Burkina Faso': 'BF', 'Burundi': 'BI', 'Cabo Verde': 'CV', 'Cambodia': 'KH', 'Cameroon': 'CM', 'Canada': 'CA', 'Cayman Islands (the)': 'KY', 'Central African Republic (the)': 'CF', 'Chad': 'TD', 'Chile': 'CL', 'China': 'CN', 'Christmas Island': 'CX', 'Cocos (Keeling) Islands (the)': 'CC', 'Colombia': 'CO', 'Comoros (the)': 'KM', 'Congo (the Democratic Republic of the)': 'CD', 'Congo (the)': 'CG', 'Cook Islands (the)': 'CK', 'Costa Rica': 'CR', "C&ocirc;te d'Ivoire": 'CI', 'Croatia': 'HR', 'Cuba': 'CU', 'Cura&ccedil;ao': 'CW', 'Cyprus': 'CY', 'Czechia': 'CZ', 'Denmark': 'DK', 'Djibouti': 'DJ', 'Dominica': 'DM', 'Dominican Republic (the)': 'DO', 'Ecuador': 'EC', 'Egypt': 'EG', 'El Salvador': 'SV', 'Equatorial Guinea': 'GQ', 'Eritrea': 'ER', 'Estonia': 'EE', 'Eswatini': 'SZ', 'Ethiopia': 'ET', 'Falkland Islands (the) [Malvinas]': 'FK', 'Faroe Islands (the)': 'FO', 'Fiji': 'FJ', 'Finland': 'FI', 'France': 'FR', 'French Guiana': 'GF', 'French Polynesia': 'PF', 'French Southern Territories (the)': 'TF', 'Gabon': 'GA', 'Gambia (the)': 'GM', 'Georgia': 'GE', 'Germany': 'DE', 'Ghana': 'GH', 'Gibraltar': 'GI', 'Greece': 'GR', 'Greenland': 'GL', 'Grenada': 'GD', 'Guadeloupe': 'GP', 'Guam': 'GU', 'Guatemala': 'GT', 'Guernsey': 'GG', 'Guinea': 'GN', 'Guinea-Bissau': 'GW', 'Guyana': 'GY', 'Haiti': 'HT', 'Heard Island and McDonald Islands': 'HM', 'Holy See (the)': 'VA', 'Honduras': 'HN', 'Hong Kong': 'HK', 'Hungary': 'HU', 'Iceland': 'IS', 'India': 'IN', 'Indonesia': 'ID', 'Iran (Islamic Republic of)': 'IR', 'Iraq': 'IQ', 'Ireland': 'IE', 'Isle of Man': 'IM', 'Israel': 'IL', 'Italy': 'IT', 'Jamaica': 'JM', 'Japan': 'JP', 'Jersey': 'JE', 'Jordan': 'JO', 'Kazakhstan': 'KZ', 'Kenya': 'KE', 'Kiribati': 'KI', "Korea (the Democratic People's Republic of)": 'KP', 'Korea (the Republic of)': 'KR', 'Kuwait': 'KW', 'Kyrgyzstan': 'KG', "Lao People's Democratic Republic (the)": 'LA', 'Latvia': 'LV', 'Lebanon': 'LB', 'Lesotho': 'LS', 'Liberia': 'LR', 'Libya': 'LY', 'Liechtenstein': 'LI', 'Lithuania': 'LT', 'Luxembourg': 'LU', 'Macao': 'MO', 'Republic of North Macedonia': 'MK', 'Madagascar': 'MG', 'Malawi': 'MW', 'Malaysia': 'MY', 'Maldives': 'MV', 'Mali': 'ML', 'Malta': 'MT', 'Marshall Islands (the)': 'MH', 'Martinique': 'MQ', 'Mauritania': 'MR', 'Mauritius': 'MU', 'Mayotte': 'YT', 'Mexico': 'MX', 'Micronesia (Federated States of)': 'FM', 'Moldova (the Republic of)': 'MD', 'Monaco': 'MC', 'Mongolia': 'MN', 'Montenegro': 'ME', 'Montserrat': 'MS', 'Morocco': 'MA', 'Mozambique': 'MZ', 'Myanmar': 'MM', 'Namibia': 'NA', 'Nauru': 'NR', 'Nepal': 'NP', 'Netherlands (the)': 'NL', 'New Caledonia': 'NC', 'New Zealand': 'NZ', 'Nicaragua': 'NI', 'Niger (the)': 'NE', 'Nigeria': 'NG', 'Niue': 'NU', 'Norfolk Island': 'NF', 'Northern Mariana Islands (the)': 'MP', 'Norway': 'NO', 'Oman': 'OM', 'Pakistan': 'PK', 'Palau': 'PW', 'Palestine, State of': 'PS', 'Panama': 'PA', 'Papua New Guinea': 'PG', 'Paraguay': 'PY', 'Peru': 'PE', 'Philippines (the)': 'PH', 'Pitcairn': 'PN', 'Poland': 'PL', 'Portugal': 'PT', 'Puerto Rico': 'PR', 'Qatar': 'QA', 'R&eacute;union': 'RE', 'Romania': 'RO', 'Russian Federation (the)': 'RU', 'Rwanda': 'RW', 'Saint Barth&eacute;lemy': 'BL', 'Saint Helena, Ascension and Tristan da Cunha': 'SH', 'Saint Kitts and Nevis': 'KN', 'Saint Lucia': 'LC', 'Saint Martin (French part)': 'MF', 'Saint Pierre and Miquelon': 'PM', 'Saint Vincent and the Grenadines': 'VC', 'Samoa': 'WS', 'San Marino': 'SM', 'Sao Tome and Principe': 'ST', 'Saudi Arabia': 'SA', 'Senegal': 'SN', 'Serbia': 'RS', 'Seychelles': 'SC', 'Sierra Leone': 'SL', 'Singapore': 'SG', 'Sint Maarten (Dutch part)': 'SX', 'Slovakia': 'SK', 'Slovenia': 'SI', 'Solomon Islands': 'SB', 'Somalia': 'SO', 'South Africa': 'ZA', 'South Georgia and the South Sandwich Islands': 'GS', 'South Sudan': 'SS', 'Spain': 'ES', 'Sri Lanka': 'LK', 'Sudan (the)': 'SD', 'Suriname': 'SR', 'Svalbard and Jan Mayen': 'SJ', 'Sweden': 'SE', 'Switzerland': 'CH', 'Syrian Arab Republic': 'SY', 'Taiwan (Province of China)': 'TW', 'Tajikistan': 'TJ', 'Tanzania, United Republic of': 'TZ', 'Thailand': 'TH', 'Timor-Leste': 'TL', 'Togo': 'TG', 'Tokelau': 'TK', 'Tonga': 'TO', 'Trinidad and Tobago': 'TT', 'Tunisia': 'TN', 'Turkey': 'TR', 'Turkmenistan': 'TM', 'Turks and Caicos Islands (the)': 'TC', 'Tuvalu': 'TV', 'Uganda': 'UG', 'Ukraine': 'UA', 'United Arab Emirates (the)': 'AE', 'United Kingdom of Great Britain and Northern Ireland (the)': 'GB', 'United States Minor Outlying Islands (the)': 'UM', 'United States of America (the)': 'US', 'Uruguay': 'UY', 'Uzbekistan': 'UZ', 'Vanuatu': 'VU', 'Venezuela (Bolivarian Republic of)': 'VE', 'Viet Nam': 'VN', 'Virgin Islands (British)': 'VG', 'Virgin Islands (U.S.)': 'VI', 'Wallis and Futuna': 'WF', 'Western Sahara': 'EH', 'Yemen': 'YE', 'Zambia': 'ZM', 'Zimbabwe': 'ZW'}

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

def get_proxy_list(no_of_proxies, proxytype, anonymity, country="all"):
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
	if country not in valid_codes:
		raise Exception("Invalid Country Code !!")

	proxies = []
		

	api1 = "https://api.proxyscrape.com/?request=getproxies&timeout=500&country="+country+"&ssl=all&type="+proxytype+"&anonymity="+anonymity
	res =  urllib.request.urlopen(api1).read().decode('utf-8').split("\r\n")
	res = [i for i in res if i]
	proxies+=res
	if proxytype=="http":
		api2 = "http://spys.me/proxy.txt"
		res =  urllib.request.urlopen(api2).read().decode('utf-8').split("\n\n")[1].split("\r")[:-1][0].split("\n")
		res = [i for i in res if i]
		for line in res:
			temp = line.split(" ")
			if country != "all":
				if anonymity=="elite" and temp[1].split("-")[1] == "H" and temp[1].split("-")[0] == country:
					proxies.append(temp[0])
				elif anonymity=="anonymous" and temp[1].split("-")[1] == "A" and temp[1].split("-")[0] == country:
					proxies.append(temp[0])
				elif anonymity=="transparent" and temp[1].split("-")[1] == "N" and temp[1].split("-")[0] == country:
					proxies.append(temp[0])
				else:
					pass
			else:
				if anonymity=="elite" and temp[1].split("-")[1] == "H":
					proxies.append(temp[0])
				elif anonymity=="anonymous" and temp[1].split("-")[1] == "A":
					proxies.append(temp[0])
				elif anonymity=="transparent" and temp[1].split("-")[1] == "N":
					proxies.append(temp[0])
				else:
					pass
	if anonymity != "all":
		if country != "all":
			api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity+"&country="+country
		else:
			api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&anon="+anonymity
	else:
		if country != "all":
			api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype+"&country="+country
		else:
			api3 = "https://www.proxy-list.download/api/v1/get?type="+proxytype
	res =  urllib.request.Request(api3, headers={'User-Agent': 'Mozilla/5.0'})
	res = urllib.request.urlopen(res).read().decode('utf-8').split("\r\n")
	res = [i for i in res if i]
	proxies+=res

	if anonymity != "all":
		if country != "all":
			api4 = "https://www.proxyscan.io/api/proxy?last_check=3800&country="+country+"&limit=20&type="+proxytype+"&level="+anonymity
		else:
			api4 = "https://www.proxyscan.io/api/proxy?last_check=3800&limit=20&type="+proxytype+"&level="+anonymity
	else: 
		if country != "all":
			api4 = "https://www.proxyscan.io/api/proxy?last_check=3800&country="+country+"&limit=20&type="+proxytype
		else:
			api4 = "https://www.proxyscan.io/api/proxy?last_check=3800&limit=20&type="+ proxytype
		
		res = json.loads(urllib.request.urlopen(api4).read().decode('utf-8'))
		for proxy in res:
			proxies.append('{}:{}'.format(proxy["Ip"], proxy["Port"]))

	random.shuffle(proxies)
	if no_of_proxies>len(proxies):
		return proxies
	else:
		return proxies[:no_of_proxies]
		
def get_proxy_json(no_of_proxies, proxytype, anonymity, country="all"):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in a JSON format as per your need.
	"""
	proxies=get_proxy_list(no_of_proxies, proxytype, anonymity, country)
	proxydict = dict()
	for proxy in proxies:
		ipadd = proxy.split(":")[0]
		port = proxy.split(":")[1]
		if ipadd not in proxydict.keys():
			proxydict[ipadd] = port
	return json.dumps(proxydict)

def get_proxy_txt(filename, no_of_proxies, proxytype, anonymity, country="all"):
	"""
	Valid Proxy Type: "http", "socks4", "socks5"
	Valid Anonymity Level: "elite", "anonymous", "transparent", "all"
	
	Returns a proxy list in TXT file as per your need.
	"""
	proxies=get_proxy_list(no_of_proxies, proxytype, anonymity, country)
	fp = open(filename,"w")
	for proxy in proxies:
		fp.write(proxy+"\n")
	fp.close()
	return