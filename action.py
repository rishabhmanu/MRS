import requests, bs4
res = requests.get("http://www.imdb.com/search/title?genres=action&sort=moviemeter,asc")
try:
	res.raise_for_status()
	resSoup = bs4.BeautifulSoup(res.text,"lxml")
	# print(type(resSoup))

	names = resSoup.select('h3 a')
	# print(len(names))

	# print(names[0].getText())

	for i in range(10):
		print(names[i].getText())

except Exception as exc:
	print('There was a problem: %s' % (exc))

