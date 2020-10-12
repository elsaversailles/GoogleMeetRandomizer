import string
import random
import webbrowser
def get_random_string(length):
	letters = string.ascii_lowercase
	result_str = ''.join(random.choice(letters) for i in range(length))
	b = ''.join(random.choice(letters) for i in range(length))
	c = '-'.join(random.choice(letters) for i in range(length))
	a = ("https://meet.google.com/" + result_str)
	webbrowser.get("firefox").open(a)
	print(a)
get_random_string(10) 



