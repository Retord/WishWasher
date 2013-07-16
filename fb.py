"""
    Module containing all the relevant information related to Facebook such as Access token, FQL Queris etc.
"""

import requests



# FQL Queries
	
def POSTS_QUERY(time): return ("SELECT post_id, actor_id, message, created_time FROM stream WHERE filter_key = 'others' AND source_id = {0} AND created_time > {1} ORDER BY created_time LIMIT 200".format(USER_ID, time))


# URLs

def url_fql(): return "https://graph.facebook.com/fql"
def url_base(id): return "https://graph.facebook.com/%s" % id
def url_friend(friend_id): return url_base(friend_id)
def url_like(post_id): return url_base(post_id) + "/likes"
def url_comments(post_id): return url_base(post_id) + "/comments"
def url_family(id): return url_base(id) + "/family"


	
def get_access_token(token):
	"""
	Returns an extended access token for use with Wish-Washer. This token lives for more than the standard 2 hours (sufficient to last your occasion)
	"""
	
	if not token:
		token = "CAAJ3gRhmNPYBANhu9OYkZBqZBVL8EUjtaq7mNyH0RGUaZCNRWFSe6KLfnc0ZCzKEAtZBVakHkHbIZA1RcUNZCZAkIutVOZC6v6ZBOzGC7AP67Is25hZBwTYhrWZB1yMKLrRSeTVdRk3Pm8HOFXDauvGXgWfF1VTanZBUQlvkZD"
	
	# Get App details from app_details file
	with open("app_details", "r") as app:
		app_id = app.readline().split("\n")[0]
		app_secret = app.readline().split("\n")[0]

	payload = {'grant_type':'fb_exchange_token', 'client_id':app_id, 'client_secret':app_secret, 'fb_exchange_token':token}
	r = requests.get("https://graph.facebook.com/oauth/access_token", params=payload)
	
	access_token = str(r.text.split("&")[0].split("=")[1])
	
	
	return access_token



def get_posts(start_time):
	payload = { 'access_token': access_token, 'q':POSTS_QUERY(start_time) }
	posts = requests.get( url_fql(), params=payload )
	return posts.json()     # Creates Python object from the JSON
	

def get_friend(friend_id):
	return requests.get( url_friend(friend_id) ).json()
	
	


# Your FB user id. Be sure to change this!
USER_ID = '1587053882'

access_token = get_access_token()



#Token has to be updated
AUTH_TOKEN = 'CAAEKO64gS0YBANjtPD6NVXFnSrgM3ghzV30oOWLcvJ5cXEb7rWpcErM9idOM6U9lN7gqGnZAeNjEzMG0WMFqs6V1hrjt9c2L1pthlMZBBH8Lz9SQJAc8kyv70ApH7VTPCNzNNjZCC6gDpEohkZCAzZCpZCqywQAFQZD'

TOKEN_GRAPH_API = 'CAACEdEose0cBAPBleQCOHigvxY5CagD8xHwfmHMdZBzE4WHyD6dSZATdseWefZCkt9IZBnLmxpkmZB30dfXOuXf3SiUSZBZAp9Yn58aFaUzb2v3LpvSg2aPjWAjjMvyoGOmI8ZC6CfCflmsTanRNI2Ef2QaZBfEJ9pLU9Im8ZA9FhauAZDZD'
