"""
Module to get relation of friend to user.
"""

import requests



# Map of relation to message content
relations = {"mother":"Mom", "father":"Dad", "sister":"Tinki", "brother":"bro"}



def get_relation(friend):
	""" Determine the relationship between you and the friend specified """

	relations = requests.get("https://graph.facebook.com/me/family", params={'access_token':fb.access_token}).json()["data"]

	
	rel_list = [x["name"] for x in relations]
	
	relation = ''
	if friend["name"] in rel_list:
		relation = relations[rel_list.index(friend["name"])]["relationship"]
		
	return relation







# List of lists of relatives where each list is a specific type of relative
# The below lists should be edited as required

# [Maternal_aunts, Maternal_uncles, Paternal_aunts, Paternal_uncles, Maternal_cousin_sisters, Maternal_cousin_brothers, Paternal_cousin_sisters, Paternal_cousin_brothers]
people = [ ["Geeta", "Juli"], [], ["Shubhra"], [], ["Janica"], [], ["Pallavi", "Nikita", "Ankita"], ["Ashish", "Shobhit"] ]


	
def get_honorific(relation):
	"""
	Returns the honorific to be used when replying to a family member (E.g. Mom, Dad, Sis, Uncle Ben).

	Argument: Relation of friend to user.
	Return: Tuple where 1st value is the Honorific and 2nd value is a boolean value indicating whether the person's name is to be used.
	"""
	honorific = ""
	
	if relation in relations.keys():

		return (relations[relation], False)

	else:
	
		for (i, l) in enumerate(people):
		
			if friend["first_name"] in l:
				
				if i == 0:
					honorific = "maushi"
				elif i == 1:
					honorific = "uncle"
				elif i == 2:
					honorific = "taiji"
				elif i == 3:
					honorific = "taoji"
				elif i == 4:
					honorific = "baie"
				elif i == 5:
					honorific = "anna"
				elif i == 6:
					honorific = "di"
				elif i == 7:
					honorific = "bhaiya"
					
				break
			

		return (honorific, True)
