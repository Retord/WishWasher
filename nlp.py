"""
Script to analyze messages and determine friend relations
"""

#import fb
import requests
import string

def bday_wish(message):
	""" Analyze message to ascertain if it is a birthday wish
	    Params:
		       meassage: The message received from FB friend

		Note: This is a temporary hack. Hope to make it better soon via statistical NLP
	"""

	assert type(message) == str
	
	keywords = [["birthday", "happy", "best"], ["returns", "many", "bless"]]
	corrections = {"bday":"birthday", "hpy":"happy"}
	
	s = ''.join(c for c in message if c not in string.punctuation)
	l = s.lower().split()

	l = [corrections[x] if x in corrections.keys() else x for x in l]

	count = 0
	
	for p in  keywords:
		for x in l:
			if x in p:
				count += 1

	if count >= 2:
		return True
	else:
		return False


def get_relation(friend):
	""" Determine the relationship between you and the friend specified """

	relations = requests.get("https://graph.facebook.com/me/family", params={'access_token':fb.AUTH_TOKEN}).json()["data"]

	rel_list = [x["name"] for x in relations]

	relation = ''
	if friend["name"] in rel_list:
		relation = relations[rel_list(friend["name"])]["relationship"]

	return relation



def get_message(post, friend):
	""" Create the message to be posted as a reply
	    Input:
		     Dictionary representing FB wall post
			 Dictionary representing FB friend who posted

		Returns: A reply message to be posted in the comments
	"""
	
	relations = {"mother":"Mom", "father":"Dad", "sister":"Tinki", "brother":"bro", "cousin":"cousin", "aunt":"aunt"}
	relation = get_relation(friend["name"])

	if

	return ""
