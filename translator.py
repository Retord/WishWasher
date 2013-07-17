"""
Module to translate facebook post messages to English
"""

import requests
import xmltodict

# Microsoft Translator
class Bing:
	
	def get_access_token(self):

		try:
			with open("translate_details", "r") as bing:
				clientID = bing.readline().split("\n")[0]
				clientSecret = bing.readline().split("\n")[0]

		except Exception:
			print("File missing: Please make a file 'tarnslate_details' with the clientID and client_secret details in it (on 2 separate line).")

			
		payload = {'grant_type':'client_credentials', 'client_id':clientID, 'client_secret':clientSecret, 'scope':'http://api.microsofttranslator.com'}
		header = {'content-type':'application/x-www-form-urlencoded'}
		
		r = requests.post("https://datamarket.accesscontrol.windows.net/v2/OAuth2-13", data=payload, headers=header)
		
		access_token = r.json()['access_token']
		
		return access_token
		

	
	def translate(self, message):
	
		auth = "Bearer " + self.get_access_token()
		
		header = {'Authorization':auth}
		
		payload = {'text':message, 'to':'en'}

		translation_uri = "http://api.microsofttranslator.com/v2/Http.svc/Translate"
		trans = requests.get(translation_uri, headers=header, params=payload)

		d = xmltodict.parse(trans.text)
		
		return d["string"]["#text"]



"""
The Google Translator API is temporarily deprecated and the new API has a 0 courtesy limit by Google on translation (i.e. each translation costs money, no matter how small)
"""
# Google Translator
class Google:
	
	def get_key(self):
		"""
		Returns API key for making requests. This is a browser key.
		"""
		return 'AIzaSyA8fXdjKrtcJ_L6JukQh_uJLS0Vrw27wrs'


	def translate(self, message):

		translate_uri = "https://www.googleapis.com/language/translate/v2"

		payload = {'key':self.get_key(), 'target':'en', 'q':message}

		r = requests.get(translate_uri, params=payload)

		return r.json()["data"]["translations"]
	
