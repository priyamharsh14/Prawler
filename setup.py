from distutils.core import setup
setup(
	name = 'Prawler',
	packages = ['Prawler'],
	version = '0.1',
	description = 'Scrape Proxies from Internet in seconds',
	author = 'Priyam Harsh',
	author_email = 'priyamharsh14@gmail.com',
	url = 'https://github.com/priyamharsh14/Prawler',
	download_url = 'https://github.com/priyamharsh14/Prawler/tarball/master',
	keywords = ['proxy', 'scraper', 'crawler', 'proxycrawler'],
	install_requires=['requests'],
	data_files=[('', ['LICENSE'])],
	include_package_data=True,
	long_description=open('README.md').read()
	classifiers=[
	'Development Status :: 4 - Beta',
	'Intended Audience :: Developers',
	'Topic :: Software Development :: Libraries :: Python Modules',
	'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
	'Programming Language :: Python :: 3',
	'Programming Language :: Python :: 3.4',
	'Programming Language :: Python :: 3.5',
	'Programming Language :: Python :: 3.6',
	'Operating System :: OS Independent',
	'Environment :: Console',
	],
)