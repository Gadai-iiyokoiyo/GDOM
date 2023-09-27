import re
import requests
class Connect():
	def __init__(self):
		self.urllist = {}
		self.reload()

	def reload(self):
		fp = open("connect.txt","r").readlines()
		for line in fp:
			url = re.sub(r"([a-zA-Z0-9]{1,20}\.[a-zA-Z0-9]{2,10}),\"(.*)\",\"([a-zA-Z0-9]*)\",\"([0-9]{2}/[0-9]{2})\"",r"\1,\3,\4",line)
			url_splitted = url.split(",")
			self.urllist["grd://"+url_splitted[0]] = [url_splitted[1].replace("\n",""), url_splitted[2].replace("\n",""),url_splitted[3].replace("\n","")]
			
	def real_domain(self,url):
		return self.urllist[url][0]

	def list_get(self):
		return self.urllist
	
	def get(self, url, param):
		return requests.get(self.urllist[url][0],param)

	def info(self,url):
		return f"""Type\t\t:\tGdom ==Redirect==> Whois
Register\t:\t{self.urllist[url][1]}
Register_date\t:\t{self.urllist[url][2]}
		"""