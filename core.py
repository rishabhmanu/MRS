import requests, bs4

def scrape(res):
	try:
		res.raise_for_status()
		resSoup = bs4.BeautifulSoup(res.text,"lxml")
		names = resSoup.select('h3 a')
		for i in range(10):
			print(names[i].getText())

	except Exception as exc:
		print("There was a problem %s" % (exc))


n = input("How are you feeling: ")

if n == "fear":
	# genere:sports
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=sport&sort=user_rating,desc")
	scrape(res)

elif n == "angry":
	# genere:family
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=family&sort=user_rating,desc")
	scrape(res)

elif n == "sad":
	#genere: comedy/drama
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=comedy,drama&sort=user_rating,desc")
	scrape(res)

elif n == "Joyful":
	#genere: romance/thriller
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=romance,thriller&sort=user_rating,desc")
	scrape(res)

elif n == "digust":
	#genere: romance/thriller
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=musical&sort=user_rating,desc")
	scrape(res)

elif n == "surprise":
	#genere: romance/thriller
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=mystery&sort=user_rating,desc")
	scrape(res)

elif n == "trust":
	#genere: romance/thriller
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=western&sort=user_rating,desc")
	scrape(res)

elif n == "anticipation":
	#genere: romance/thriller
	print("Hey! you can watch these top rated movies: ")
	print()
	res = requests.get("http://www.imdb.com/search/title?genres=horror,thriller&sort=user_rating,desc")
	scrape(res)

else:
	print("Not a valid emotion")