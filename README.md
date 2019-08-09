<h1 align="center">
	<br>
	Prawler
	<br>
</h1>
<h4 align="center">Advanced Proxy Scraper</h4>
<p align="center">
<img src="https://img.shields.io/github/license/priyamharsh14/Prawler">
<img src="https://img.shields.io/pypi/v/Prawler">
<img src="https://img.shields.io/pypi/pyversions/Prawler">
</p>
<br>

### What is Prawler ?
Prawler finds best and working proxies from the internet in seconds. Proxies are used by developers, ethical hackers, pentesters and so on, in order to cover their tracks or bypass firewall restrictions. Prawler helps to find desired proxy in all possible formats.

### Installation
```
pip install Prawler
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
Prawler.get_proxy_list(<PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_list("http", "elite")
```

- Find all proxies in JSON format

Basic Syntax:
```
Prawler.get_proxy_json(<PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
proxy_list = Prawler.get_proxy_json("http", "elite")
```

- Find all proxies and save it into a text file

Basic Syntax:
```
Prawler.get_proxy_txt(<FILENAME>, <PROXY TYPE>, <PROXY ANONYMITY LEVEL>)
```
Example:
```
import Prawler
Prawler.get_proxy_txt("proxy_list.txt", "http", "elite")
```

### Note:
**Valid Proxy Type: http, socks4, socks5**

**Valid Anonymity Level: all, elite, anonymous, transparent**
