#Andrew Anstaett
#CNN Web Crawler in Python

from bs4 import BeautifulSoup
import urllib2



def getSoup(url):
	#requests html from website
	html = urllib2.urlopen(url).read()
	#makes it into a BeautifulSoup datatype that we can use to parse out the infomation needed
	soup = BeautifulSoup(html)
	#returns it to 'main'
	return soup

def pullArticles(soup,category):
	#for all the unordered lists
	#the categories are seperated into diffrent unordered lists, so we seperate them
	#and find the ones we are looking for
	for ul in soup.find_all('ul'):
		#h2 is the title of the category
		for h2 in ul.children:
			#we find the category we are looking for
			if(h2.text == category):
				#cnn uses the class 'cd__headline-text' for the headline articles titles
				#we look for all the headline titles
				for span in ul.select(".cd__headline-text"):
					#we print the titles
					print("\t" + span.text)




#'main'
cnn = getSoup("http://www.cnn.com")

print("Top Stories:")
pullArticles(cnn,"Top Stories")

print("\n\n")

print("News and Buzz:")
pullArticles(cnn,"News and Buzz")

print("\n\n")

print("Sports:")
pullArticles(cnn,"Sports")

print("\n\n")
