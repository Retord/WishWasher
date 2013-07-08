"""
    Module containing all the relevant information related to Facebook such as Access token, FQL Queris etc.
"""

USER_ID = '1587053882'


#Token has to be updated
AUTH_TOKEN = 'CAAEKO64gS0YBAFZBm0YDGxOQVrXCJuwmJUnJuZBlAGAVkTpRaA4BxHKxW5IBysrceHHCqOHssS3FF90AC5dMD7iVuDJE8fKHm43ysIUlo1jZAbxPYa4cJ5g1VHieasRcdm1s1eL3ERaKaCFZAXqjGOitm5hshYwZD'

TOKEN_GRAPH_API = 'CAACEdEose0cBAPBleQCOHigvxY5CagD8xHwfmHMdZBzE4WHyD6dSZATdseWefZCkt9IZBnLmxpkmZB30dfXOuXf3SiUSZBZAp9Yn58aFaUzb2v3LpvSg2aPjWAjjMvyoGOmI8ZC6CfCflmsTanRNI2Ef2QaZBfEJ9pLU9Im8ZA9FhauAZDZD'


# FQL Queries

# Better use the url https://graph.facebook.com/me/friends
ALL_FRIEND_FQL = 'SELECT uid, first_name, last_name, name, pic, pic_small, pic_big, birthday_date, sex, current_location, profile_url, is_app_user FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'

	
def POSTS_QUERY(time): return ("SELECT post_id, actor_id, message, created_time FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time > %d ORDER BY created_time") % time


# URLs

def url_fql(): return "https://graph.facebook.com/fql"
def url_base(id): return "https://graph.facebook.com/%s" % id
def url_friend(friend_id): return url_base(friend_id)
def url_like(post_id): url_base(post_id) + "/likes"
def url_comments(post_id): url_base(post_id) + "/comments"
def url_family(): url_base + "/family" % "me"
