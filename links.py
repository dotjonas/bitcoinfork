import httplib2
import urllib2
from bs4 import BeautifulSoup, SoupStrainer
#from BeautifulSoup import SoupStrainer

#Create and open a new .csv data file 
f = open('bitcoin-links.csv', 'w')

url = "https://bitcointalk.org/index.php?board=1.0"

#http = httplib2.Http()
#import httplib2
#if __name__ == "__main__":
#    h = httplib2.Http(".cache", disable_ssl_certificate_validation=True)
#    response, content = h.request(url, "GET")
    #print str(h) + str(content)

#Iterate through the posts on bitcointalk 

links = []

page = urllib2.urlopen(url)
soup = BeautifulSoup(page, "lxml")

pageLinks = [soup.find_all(attrs={'class' : 'href'})]
html = str(pageLinks)
#print "LINKS: " + str(html)

for a in soup.find_all('a', href=True):
    print "Found the URL:", a['href']
    linkTxt = str(a['href'])
    linkStrp = linkTxt.strip()
    link = linkStrp.replace("'", "")
    links.append(link)

print links
f.write(str(links) + ',' + '\n')

f.close()
	

#for line in pageLinks:
 #   l = line.findAll('a')
  #  print l

#print "PAGE: " + str(page) 
#print "SOUP: " + str(soup) 
#class="windowbg3"

#links = soup.find_all(attrs={"class":"href"})
#print "LINKS: " + str(links)





#for div in pageLinks:
 #   print div.a['href']
    #link = str(div.a['href'])
	#link = linkTxt.strip()
	#print "LINK: " + str(link)

#for l in links:
	#	linkbit = ''.join(t.findAll(text=True))
	#	link = titleText.strip()
	#	print "Link: " + link
		


#for link in BeautifulSoup(response, parseOnlyThese=SoupStrainer('a')):
#    if link.has_attr('href'):
#        print link['href']


