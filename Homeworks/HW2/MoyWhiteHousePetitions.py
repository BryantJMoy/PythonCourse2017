# HW2 
from bs4 import BeautifulSoup
import urllib2

#web_address ="https://petitions.whitehouse.gov/petitions"
#web_page = urllib2.urlopen(web_address)
#soup = BeautifulSoup(web_page.read()) 
#soup.prettify()
#title_of_petition = soup.find('h1', {"class": "title"})
#num_of_signatures=soup.find('span', {"class": "signatures-number"}).text
# date
#range(0:2)

"https://petitions.whitehouse.gov/petitions?page=0"
"https://petitions.whitehouse.gov/petitions?page=1"
"https://petitions.whitehouse.gov/petitions?page=2"

web_address =[ "https://petitions.whitehouse.gov/petitions?page=" + str(i) for i in range(0, 2) ]

indvdl_petitions = []


for i in web_address:
	web_page = urllib2.urlopen(i)
	soup = BeautifulSoup(web_page.read(),"html.parser") #added "html.parser" for Parse Warning #49
	soup.prettify()
	petitions = []
	petitions.append(soup.find_all('h3')) # .append=soup.find_all('a')) 
#flatten = []
#for sublist in list_of_lists:
    #for val in sublist:
        #flattened.append(val)
	flatten_petition_list= [] #one list out of a line of multiple list
	for sublist in petitions:
		for item in sublist:
			flatten_petition_list.append(item)
	for site in range(0,len(flatten_petition_list)): #change to try except statement to ignore rid of error
	#I dont know why I'm getting an error
	#https://stackoverflow.com/questions/574730/python-how-to-ignore-an-exception-and-proceed
		try:
			indvdl_petitions.append("https://petitions.whitehouse.gov"+flatten_petition_list[site].a['href'])
		except: 
			pass # Do nothing



title_of_petition  = [ ]
num_of_signatures  = [ ]
petition_issues    =[ ]
date               =[ ]



#Error. wrap everything in .encode("utf8") Is there a universal way to do this?
for i in range(0, len(indvdl_petitions)):
	web_page1 = urllib2.urlopen(indvdl_petitions[i])
	soup1 = BeautifulSoup(web_page1.read(),"html.parser")
	title = soup1.find('h1', {"class": "title"}).text #Title
	title_of_petition.append(title.encode("utf8")) #u
	num_of_signatures.append(soup1.find('span', {"class": "signatures-number"}).text)#num. of sign.
	get_attr = soup1.find('h4', {"class": "petition-attribution"}).text#Date
	date.append(" ".join(get_attr.split(" ")[-3:])) #20-Jan-17
	pet_iss = [] # issue
	chunk = soup1.find('section', {"id": "content"}).find_all('h6')

	for part in chunk:
		pet_iss.append(part.text.encode("utf8"))
	petition_issues.append(pet_iss)


#make issues into a flat list to get rid of ['']
petition_issues1=[]
for sublist in petition_issues:
	for item in sublist:
		petition_issues1.append(item)


title_of_petition
num_of_signatures
petition_issues
date  
