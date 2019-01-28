import requests
import json

#r = requests.get('http://10.42.0.1:5000/', auth=('oep211', 'secret'))
# http://10.42.0.1:5000/<command-family>/<username>/<secret>/<action>/<index>

command_family = 'login'
host = 'http://10.42.0.1:5000'
user = 'oep211'
secret = 'secret'
index = 10 #amount of time it's held for
startH = 'start_holding'
stopH = 'stop_holding'
tick = 'tick'

#login
r = requests.post(host + '/' + command_family + '/' + user + '/' + secret)
print (r.text)

command_family = 'game'
s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)


r2 = requests.post(s2)
print (r2.text)

s3 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + startH)
r3 = requests.post(s3)
print(r3.text)

s4 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + stopH)
r4 = requests.post(s4)
print(r4.text)

'''
if r2 == True: #if request posts sucessfully
	s3 = s2 + '/' + startH + '/' + index + '/' + stopH
	# GET holding //if this returns true should be in if block
	r3 = request.post(s3) 
    #print(r3.text)
	if r3 == True: #how to check if the request posted successfully?
		print("The tick is being held.")
	else:
		print("The tick cannot be held")
else:
	print("Jesse is not ticking properly upon request")
    #This prints even though the server shows that we have succesfully ticked.
'''

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 50-54 show us direction to proceed in.

action = 'reset'
logout = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(logout.text)
#Game is used for logout.

