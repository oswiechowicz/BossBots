import requests

command_family = 'game'
host = 'http://10.42.0.1:5000'
user = 'kbm383'
secret = 'secret'
index = 10 #amount of time it's held for
action = 'reset'
startH = 'start_holding'
stopH = 'stop_holding'
tick = 'tick'
benchmark = 'B'
'''
r = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + benchmark)
print (r.text)

'''
r4 = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' +  action)
print(r4.text)
