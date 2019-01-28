
import requests
import json
#FOLLOWING FORMAT MUST BE USED (YES, EVERY TIME): 
# http://10.42.0.1:5000/<command-family>/<username>/<secret>/<action>/<index>

host = 'http://10.42.0.1:5000'
user = 'kbm383'
secret = 'secret'
index = '1' #amount of time it's held for
command_family = 'game'
benchmark = 'B'
startH = 'start_holding'
stopH = 'stop_holding'
get_status = 'get_status'
tck = 'tick'
direction = 'select_direction'
benchmark = 'B'
attempt = 'attempt_heal'
heal = 'heal_solution'
solution = 'solution'


#Logging in 
def login(): #commandfamily input MUST be 'login' not 'game'
    login = requests.post(host + '/' + 'login' + '/' + user + '/' + secret + '/' + benchmark)
    print(login.text)
    return login


#Logging out
def logout(): #action is reset
    logout = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + 'reset')
    print(logout.text)
    return logout

#Tick
def tick():
    tickrequest = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + tck)
    print (tickrequest.text)
    return tickrequest

#Get Status
def getstatus(): #action must be 'get_status'
    getstatus = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + get_status)
    print(getstatus.text)
    
    '''
    my_dictionary = json.loads(getstatus.text)
    print(my_dictionary['options'])
    '''

#Start Holding
def starthold():
    starthold = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + startH)
    print(starthold.text)
    return starthold

#Stop Holding
def stophold():
    stophold = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + stopH)
    print(stophold.text)
    return stophold

#Change Direction
def changedirection(): #needs index as input
    changedirection = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
    print(changedirection.text)
    return changedirection

#Attempt Heal
def attemptheal():
    healpost = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
    healrequest = requests.post(healpost)
    print(healrequest.text)
    return healrequest

#Heal Solution
def healsolution():
    hsolutionpost = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + solution)
    hsolutionrequest = requests.post(hsolutionpost)
    print(hsolutionrequest.text)

#Test Run - Uncomment below to test!
'''
login()

tick()

starthold()
stophold()

changedirection('1')

attemptheal()
healsolution()

logout()
'''