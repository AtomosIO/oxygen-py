import time
import urllib2
import json

class OClient:
	endpoint = ""
	token = ""
	pollingSleep = 1

	def __init__(self, endpoint="", token="", user="", password=""):
		if len(endpoint) == 0:
			raise Error("Must specify endpoint")
			
		self.endpoint = endpoint
		
		if len(user) != 0 and len(password) != 0:
			self.token = self.doMethodAndUnmarshal(tokensEndpoint, "POST", { 
				"user": user,
				"password": password,
			})["token"]
		else:
			self.token = token
	
	def doGet(self, url):
		request = urllib2.Request(self.endpoint + url)
		request.add_header('Authorization', self.token)
		
		return urllib2.urlopen(request).read()
		
	def doMethod(self, url, method, data):
		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(self.endpoint + url, data=data)
		request.add_header('Authorization', self.token)
		request.get_method = lambda: method
		
		try:
			return opener.open(request)
		except urllib2.HTTPError, error:
			return error
	
	def getNode(self, nodeId):
		return self.doGet(str(nodeId) + "?id=true")
				
