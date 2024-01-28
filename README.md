
# peek

> A lightweight web directory reconnaissance tool.

# Installation
1. Clone the repository
2. `cd` into the cloned repo
3. `pip install requirements.txt`
4. `cd` into `./peek/`

# Usage
> **NOTE:** This tool is intended for educational purposes. Do **not** use it against 		   sites that have not provided **prior consent**. I **do not** take responsibility if this tool is misused in accordance to relevant local law/legislation in any capacity.
> 
> It is on you, don't do something stupid.

- Peek provides a quick and easy to to conduct directory reconnaissance.
	`pingu@pingu:~$ python peek.py [url] [worldlist(.txt)]`
- For example,
	`pingu@pingu:~$ python peek.py 'http://127.0.0.1:8000 wordlist.txt'` 
	```
	+-----------------------------------------------------+
	|                Welcome to peek v1.0                 |
	+-----------------------------------------------------+
	| Target url: http://127.0.0.1:8000 (seems to be up!) |
	+-----------------------------------------------------+
	> NOTE: These requests can be monitored by the web server. They are not invisible.
	============================
	[+] Starting directory recon
	============================
	> / (200)
	> /beans (200)
	> /super (200)
	> /index (200)
	============================
	[+] Finished in 0.14s
	============================```


#### Note:
- This tool is currently under development
- There are more planned features
	- Providing custom extensions to be checked
	- Ability to enumerate through different sub domains
	- Ability to trace/follow 301 redirect codes
	- Ability to provide custom headers (authentication reasons etc)
	- Implement multithreading to improve performance on larger wordlist sets
	- Ability to choose custom timeout times (in case web server is slower than the default 1s to respond)
	- Ability to return other attributes about located pages
	- Verbose mode