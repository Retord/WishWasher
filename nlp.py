"""
Script to analyze messages and determine friend relations
"""

import fb
import requests


def bday_wish(message):
	""" Analyze message to ascertain if it is a birthday wish """
	return True



def get_relation(friend):
	""" Determine the relationship between you and the friend specified """

	relations = requests.get("https://graph.facebook.com/me/family", params={'access_token'=fb.AUTH_TOKEN}).json()["data"]

	rel_list = [x["name"] for x in relations]

	if friend["name"] in rel_list:
		relation = relations[rel_list(friend["name"])]["relationship"]

	return relation



def get_message(post, friend):
	""" Create the message to be posted as a reply """
	return ""
