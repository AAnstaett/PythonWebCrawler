from bs4 import BeautifulSoup
import urllib2



def getSoup(url):
	html = urllib2.urlopen(url).read()
	soup = BeautifulSoup(html)
	return soup

def pullCategories(soup,category):
	for a in soup.find_all("a",text=category):
		categories = a['href']

	return categories

def pullArticles(soup):
	for span in soup.find_all("span",itemprop='name'):
		print("\t" + span.string)


	return

cnn = getSoup("http://www.cnn.com")
category = pullCategories(cnn,"Tech")

print("Tech:")
category = pullCategories(cnn,"Tech")
articles = getSoup("http://www.cnn.com" + category)
pullArticles(articles)

print("\n\n")

print("Entertainment:")
category = pullCategories(cnn,"Entertainment")
articles = getSoup("http://www.cnn.com" + category)
pullArticles(articles)

print("\n\n")

print("Travel:")
category = pullCategories(cnn,"Travel")
articles = getSoup("http://www.cnn.com" + category)
pullArticles(articles)
