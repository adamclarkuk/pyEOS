import json
import requests
import sys

class pyEOS(object):

	# Define all URL propeeties and chain based URI's

	__url       = "none"
	protocol    = "http://"
	version     = { 1 : "/v1/chain" }
	port        = "8888"
	chainInfo   = "/get_info"
	accountURL  = "/get_account" 
	accountdata = { 'account_name':'eosio' }
	code        = "/get_code"
	tableRows   = "/get_table_rows"

	# Variable to store returned JSON
	jsonDetails = {}

	# Session object for REST API calls
	session     = requests.session()

	def __init__( self, address = "127.0.0.1" , apiversion = 1 ):
		
		# Check that the version number sent through is in our dictiona
		try:
			x = self.version[apiversion]
		except:
			print("Unsupported API version")
			sys.exit()

		self.__url = self.protocol + address + ":"+ self.port + self.version[apiversion]
	
	def Get_URL(self):
		return self__url

	def hit_chain(self, URI, method = "GET", **kwargs):

		try:
			# Hit the URL stored and saved returned data to json dictionary
			
			if str.upper(method) == "GET":
				
				self.jsonDetails = self.session.get(self.__url+URI).json()
			
			elif str.upper(method) == "POST":
				
				self.jsonDetails = self.session.post(self.__url+URI, data = '{\"account_name\":\"'+str(kwargs['acct_name'])+'\"}' ).json()

		except requests.exceptions.ConnectionError as Error:
			print("Failed to connect")
		
		except:
			print("Unexpected error:", sys.exc_info()[0])
			sys.exit()

	def chain_details(self):

		self.hit_chain(self.chainInfo)

	def get_account(self, account_name):

		self.hit_chain(self.accountURL,"POST",acct_name=account_name)
		
		# Grab the accont name
		acct_name = self.jsonDetails['account_name']
		
		# Check if a key exsits first, if not return None 
		try:
			key = self.jsonDetails['permissions'][0]['required_auth']['keys'][0]['key']

		except:
			key = "None"

		return { 'account_name':acct_name, "key" : key }

	def printJson(self):

		print("")
		
		for item in self.jsonDetails:
			print(item+" : "+str(self.jsonDetails[item]))

		print("")
