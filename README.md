<h1 align="center">
	<br>
	<img src="https://i.ibb.co/w7jx8Yg/prawler.png" alt="prawler">
</h1>
<h4 align="center">Advanced Proxy Scraper</h4>
<p align="center">
	<a href="https://pypi.org/project/Prawler/"><img src="https://img.shields.io/pypi/v/Prawler"></a>
<a href="https://raw.githubusercontent.com/priyamharsh14/Prawler/master/LICENSE"><img src="https://img.shields.io/github/license/priyamharsh14/Prawler"></a>
<img src="https://img.shields.io/pypi/pyversions/Prawler">
</p>
<br>

## What is Prawler ?
Prawler finds best and working proxies from the internet in seconds. Proxies are used by developers, ethical hackers, pentesters and so on, in order to cover their tracks or bypass firewall restrictions. Prawler helps to find desired proxy in all possible formats.

## Features
- Fast Proxy Server Scraping through multiple API's
- Extract various types of Proxy Servers (HTTP, SOCKS4, SOCKS5)
- Scrap for Proxy Servers based on their Anonymity Level (Transparent, Anonymous, Elite)
- Various output formats available (List, JSON, TXT file)

## What's new in 0.51beta update ?
- Bug fixes
- Reduced the code length
- User can specify the number of proxies he/she needs in all available formats (List, JSON, TXT file)

## Installation

New Installation:
```
pip install Prawler
```

Updating the package:
```
pip install --upgrade Prawler
```

## Usage
We can use Prawler in several ways:
- **Find a single random proxy server**

Syntax:
```
Prawler.get_random_proxy(<PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy = Prawler.get_random_proxy("http", "elite")
```

- **Find all proxies in list format**

Syntax:
```
Prawler.get_proxy_list(<NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_list(5, "http", "elite")
```

- **Find all proxies in JSON format**

Syntax:
```
Prawler.get_proxy_json(<NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_json(5, "http", "elite")
```

- **Find all proxies and save it into a text file**

Syntax:
```
Prawler.get_proxy_txt(<FILENAME>, <NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
Prawler.get_proxy_txt("proxy_list.txt", 50, "http", "elite")
```

## Note:

**Valid Proxy Type: http, socks4, socks5**

**Valid Anonymity Level: all, elite, anonymous, transparent**

## Donate

If you feel this project was awesome, you can give me a cup of coffee :)

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.me/priyamharsh14)
