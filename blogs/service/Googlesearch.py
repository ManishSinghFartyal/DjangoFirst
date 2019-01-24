from bs4 import BeautifulSoup
import requests 
def fetch_result(str,num):	
	search_term=str.replace(' ','+')
	google_url='http://www.google.com/search?q={}&num={}'.format(search_term,num)
	response=requests.get(google_url)	
	soup=BeautifulSoup(response.text)
	text1=soup.find_all('div',attrs={'class':'g'})	
	links={}
	for div in text1:
		try:
			a=div.find('a',href=True)
			title=a.text		
			hre=a['href']
			#print(title," and link = ",href,"  \n\n")
			links[title]=hre
		except:
			continue

	return links


#fetch_result("stack overflow",10)