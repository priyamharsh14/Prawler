<h1 align="center">
	<br>
	Prawler
	<br>
</h1>
<h4 align="center">Advanced Proxy Scraper</h4>
<p align="center">
<img src="https://img.shields.io/pypi/v/Prawler">
<img src="https://img.shields.io/github/license/priyamharsh14/Prawler">
<img src="https://img.shields.io/pypi/pyversions/Prawler">
</p>
<br>

### What is Prawler ?
Prawler finds best and working proxies from the internet in seconds. Proxies are used by developers, ethical hackers, pentesters and so on, in order to cover their tracks or bypass firewall restrictions. Prawler helps to find desired proxy in all possible formats.

### Features
- Fast Proxy Server Scraping through multiple API's
- Extract various types of Proxy Servers (HTTP, SOCKS4, SOCKS5)
- Scrap for Proxy Servers based on their Anonymity Level (Transparent, Anonymous, Elite)
- Various output formats available (List, JSON, TXT file)

### What's new in 0.31beta update ?
- Bug fixes
- User can specify the number of proxies he/she needs in all available formats (List, JSON, TXT file)

### Installation

New Installation:
```
pip install Prawler
```

Updating the package:
```
pip install --upgrade Prawler
```

### Usage
We can use Prawler in several ways:
- Find a single random proxy server

Basic Syntax:
```
Prawler.get_random_proxy(<PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy = Prawler.get_random_proxy("http", "elite")
```

- Find all proxies in list format

Basic Syntax:
```
Prawler.get_proxy_list(<NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_list(5, "http", "elite")
```

- Find all proxies in JSON format

Basic Syntax:
```
Prawler.get_proxy_json(<NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_json(5, "http", "elite")
```

- Find all proxies and save it into a text file

Basic Syntax:
```
Prawler.get_proxy_txt(<FILENAME>, <NO. OF PROXIES>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
Prawler.get_proxy_txt("proxy_list.txt", 50, "http", "elite")
```

### Note:
**Valid Proxy Type: http, socks4, socks5**

**Valid Anonymity Level: all, elite, anonymous, transparent**
