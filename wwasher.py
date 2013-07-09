# Script to reply to all my Birthday wishes. :)

import requests
import json
import time

import fb
import nlp


bday = "Thu Jul 11 00:00:00 2013"
start_time = time.mktime(time.strptime("Tue Jul  9 00:00:00 2013"))#time.mktime( time.strptime( bday ) )
end_time = time.mktime( time.strptime( "Fri Jul 12 00:00:00 2013" ) )



def get_posts(start_time):
	""" Returns json data of all the posts on your stream since the start time provided"""

	payload = { 'access_token': fb.AUTH_TOKEN, 'q':fb.POSTS_QUERY(start_time) }
	r = requests.get( fb.url_fql(), params=payload )
	posts = json.loads(r.text)     # Creates Python object from the JSON
	print("received posts")
	if "data" not in posts.keys():
		print("Please reinitialize session token!")
		
	return posts["data"]



def reply_bday(posts):
	"""Generates a reply to the post if it is a birthday wish
	   Input: List of Dictionaries of all the posts on my wall since a specified time.
	"""

	payload = { 'access_token':fb.AUTH_TOKEN, 'message':""}
	
	for post in posts:
		print(post["message"])
		
		if not nlp.bday_wish(post["message"]):

			friend = requests.get( fb.url_friend(post['actor_id']) ).json()
			friend_name = friend["first_name"]
			print("Got friend details")

			print(post["post_id"].split('_')[-1])
			like_url = fb.url_like(post["post_id"].split('_')[-1])
			print(like_url)
			l = requests.post(like_url, data=payload)
			print("Got Like URL")

			print("commenting")
			comment_url = fb.url_comments(post["post_id"])
			payload["message"] = nlp.get_message(post, friend)
			c = requests.post(comment_url, data=payload)

			start_time = post["created_time"]
			
			print( "Replied to {0} who posted {1}: {2}. :)".format( friend["name"], post["post_id"], post["message"] ) ) 




if __name__ == "__main__":

	if time.mktime(time.strptime(time.ctime())) < start_time:
		print("Waiting for your birthday")

		while time.mktime(time.strptime(time.ctime())) < start_time:
			continue

		
	while start_time < end_time :
		reply_bday( get_posts( start_time ) )
	
