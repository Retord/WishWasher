"""
    Module containing all the relevant information related to Facebook such as Access token, FQL Queris etc.
"""

USER_ID = '1587053882'


#Token has to be updated
AUTH_TOKEN = 'CAAEKO64gS0YBAB36rQ4i39B29H3ZCRry1kvrYj09BwOEwQYVGVLaZAJh0wLrW0chQ34xSKyFoZB2ruatgoqMYTFiydlfLnRA6okZClrpK13WbjIPoGSCIkCbPTWHjgEh9HbCLCOfSMxY5uwNOnLiQpaAZB3xNsxkZD'

TOKEN_GRAPH_API = 'CAACEdEose0cBAPBleQCOHigvxY5CagD8xHwfmHMdZBzE4WHyD6dSZATdseWefZCkt9IZBnLmxpkmZB30dfXOuXf3SiUSZBZAp9Yn58aFaUzb2v3LpvSg2aPjWAjjMvyoGOmI8ZC6CfCflmsTanRNI2Ef2QaZBfEJ9pLU9Im8ZA9FhauAZDZD'


# FQL Queries

# Better use the url https://graph.facebook.com/me/friends
ALL_FRIEND_FQL = 'SELECT uid, first_name, last_name, name, pic, pic_small, pic_big, birthday_date, sex, current_location, profile_url, is_app_user FROM user WHERE uid IN (SELECT uid2 FROM friend WHERE uid1 = me())'

	
POSTS_QUERY = ("SELECT post_id, actor_id, message, created_time FROM stream WHERE filter_key = 'others' AND source_id = me() AND created_time > %d ORDER BY created_time")


# URLs

url_fql = "https://graph.facebook.com/fql"
url_base = "https://graph.facebook.com/%s"
url_friend = url_base
url_like = url_base + "/likes"
url_comments = url_base + "/comments"
url_family = url_base + "/family" % "me"
