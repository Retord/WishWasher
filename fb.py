"""
    Module containing all the relevant information related to Facebook such as Access token, FQL Queris etc.
"""

import requests



# FQL Queries
	
def posts_query(time): return ("SELECT post_id, actor_id, message, created_time FROM stream WHERE filter_key = 'others' AND source_id = {0} AND created_time > {1} ORDER BY created_time LIMIT 200".format(USER_ID, time))


# URLs

def url_fql(): return "https://graph.facebook.com/fql"
def url_base(id): return "https://graph.facebook.com/%s" % id
def url_friend(friend_id): return url_base(friend_id)
def url_like(post_id): return url_base(post_id) + "/likes"
def url_comments(post_id): return url_base(post_id) + "/comments"
def url_family(id): return url_base(id) + "/family"


	
def get_access_token():
	"""
	Returns an extended access token for use with Wish-Washer. This token lives for more than the standard 2 hours (sufficient to last your occasion)
	"""
	
	
	# Get App details from app_details file
	try:
		
		with open("app_details", "r") as app:
			app_id = app.readline().split("\n")[0]
			app_secret = app.readline().split("\n")[0]
			
			access_token = app.readline().split("\n")[0]

			
		if access_token == "":         # Encountered EOF
			
			token = input("Please input the user access token (from Graph Explorer): ")
			payload = {'grant_type':'fb_exchange_token', 'client_id':app_id, 'client_secret':app_secret, 'fb_exchange_token':token}
			r = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)

			access_token = str(r.text.split("&")[0].split("=")[1])
	
			try:
				with open("app_details", "a") as app_file:
					app_file.write(access_token + "\n")
				
			except Exception:
				print("Write Error: File 'app_details' not present!")
	
				
	except Exception:
		print("File 'app_details' does not exist. Please create the file with the required data.")

	#print("Token: " + access_token)
	
	return access_token




def get_posts(start_time):
	"""
	Retrieve all the posts from user stream from the given start_time.
	"""
	
	payload = { 'access_token': access_token, 'q':posts_query(start_time) }
	posts = requests.get( url_fql(), params=payload )
	return posts.json()     # Creates Python object from the JSON
	

	
def get_friend(friend_id):
	"""
	Return the details of a friend given the Facebook id of the friend.
	"""
	return requests.get( url_friend(friend_id) ).json()
	
	


# Your FB user id. Be sure to change this!
USER_ID = '1587053882'

access_token = 'XXXXXXXXXXXXXXX'


