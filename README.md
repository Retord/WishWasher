Wish-Washer
===========

Version 2.1

Bot that Washes the Wishes on your Facebook Wall.
(Like a Dish-Washer)


Ever been stormed by hundreds of birthday wishes and in the end simply put up a status message saying, "Thanks everyone for your lovely wishes"?

Here is your solution! Wish-Washer starts reading your Facebook wall for posts regarding your birthday or any other occasion (you can specify which!) and then likes and replies on those posts, thus giving your friends the "thank you" they deserve (and not the one they need). All you have to do is start him up and he keeps running until the time you decide that he has done you proud (which is usually when your special occasion ends).


Requirements:
-------------

- [Requests - HTTP for Humans.](http://docs.python-requests.org/en/latest/)
- [xmltodict](https://github.com/martinblech/xmltodict)
- [Facebook Access Token.](https://developers.facebook.com/tools/explorer)
- A working internet connection. (duh)


How-To
------
- Install the Requests and xmltodict modules. (pip install *module_name*)



Version 2 Updates:
------------------
1. Access tokens are now Extended Access Tokens. No need to supply a new access token every 2 hours.
2. Relationships moduled out for easier editing.
3. Security details now stored in a separate file for each user = Greater degree of security. 
4. Lots of code cleanup. The design is much simpler and elegant than before.
5. Validations and Error Handling.



Powered by:

![Python](http://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/40px-Python-logo-notext.svg.png "Python")

![Facebook](http://musically.com/wp-content/uploads/2012/11/Facebook-logo-47x47.jpg "Facebook")
