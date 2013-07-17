#!/usr/bin/python

# Script to reply to all my Birthday wishes. :)

import requests
import time
import string
import sys
import codecs

import fb
import nlp


bday = "Thu Jul 11 00:00:00 2013"  # Default birthdate
start_time = int( time.mktime( time.strptime( bday ) ) )
end_time = time.mktime( time.strptime( "Fri Jul 12 00:00:00 2013" ) )


def get_start_time():
	s = str(input("Please enter the start time (day Mon dd HH:MM:SS YYYY)(0 for current time, 1 for inbuilt bday): "))

	if s == "0":
		return int(time.mktime(time.strptime(time.ctime())))
	elif s == "1":
		return start_time
	else:
		return int(time.mktime(time.strptime(s)))
	


def log(post, friend):

	s = "{0}: {1} {2} posted '{3}' Post Id: {4} \n".format(time.ctime(), post["created_time"], friend["name"], post["message"].encode('utf-8'), post["post_id"])
		
	with open("logfile."+str(post["created_time"]), "w") as f:
		f.seek(0, 2)
		f.write(s)


		
def get_posts(start_time):
	"""
	Returns json data of all the posts on your stream since the start time provided
	Input: start_time = Unix time referring from when to get posts till present.
	Return: Dictionary of all the posts since start_time till now.
	"""

	posts = fb.get_posts(start_time)
	
	if "data" not in posts.keys():
		print("Please reinitialize session token!")
		return None
	
	return posts["data"]



def reply_bday(posts):
	"""Generates a reply to the post if it is a birthday wish
	   Input: List of Dictionaries of all the posts on my wall since a specified time.
	"""

	payload = { 'access_token':fb.access_token, 'message':""}
	global start_time

	
	for post in posts:
		
		if nlp.bday_wish(post["message"]):

			friend = fb.get_friend( post['actor_id'] )
			friend_name = friend["first_name"]

			
			like_url = fb.url_like(post["post_id"])
			l = requests.post(like_url, data=payload)

			print("Commenting")
			comment_url = fb.url_comments(post["post_id"])
			payload["message"] = nlp.get_message(post, friend)
			c = requests.post(comment_url, data=payload)
			
			start_time = int(post["created_time"])
			log(post, friend)
			
			print( "Replied to {0} who posted {1}: {2}. :)".format( friend["name"], post["post_id"], post["message"].encode('utf-8') ) ) 




if __name__ == "__main__":

	start_time = get_start_time()

	fb.access_token = fb.get_access_token()
	
	if time.mktime(time.strptime(time.ctime())) < start_time:
		print("Please wait for your birthday")
		
		sys.exit(0)


	print("Starting up!")
		
	#while start_time < end_time :
	while True:
		posts = get_posts( start_time )
		if posts == None:
			print("Please reset")
			break
		
		reply_bday(posts)
	
