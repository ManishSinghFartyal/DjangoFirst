from .Googlesearch import fetch_result
def list_of_most_occured(str):
	str =str.replace('.','')	
	#str =str.replace(' ','.')
	words=str.split(" ")
	length=len(words)
	di={}
	for i in words:
		if i.lower() in di:			
			di[i.lower()] += 1
		else:
			di[i.lower()]=1	
	#print(di , length)
	new_string=""
	for i in di:
		if di[i]>=2:
			new_string+=i+"+"
	return new_string

'''
ret=list_of_most_occured("Django provides full support for anonymous sessions. The session framework lets you store and retrieve arbitrary data on a per-site-visitor basis. It stores data on the server side and abstracts the sending and receiving of cookies. Cookies contain a session ID – not the data itself (unless you’re using the cookie based backend).")
print(ret)
links=fetch_result(ret,10)
for key,value in links.items():
	print(key,"  href = ",value,"\n\n")
'''