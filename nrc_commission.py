import requests
import json

# http://10.42.0.1:5000/<command-family>/<username>/<secret>/<action>/<index>

command_family = 'login'
host = 'http://10.42.0.1:5000'
user = 'kbm383'
secret = 'secret'
index = '1' #amount of time the nanorobot is held stationary
startH = 'start_holding'
stopH = 'stop_holding'
tick = 'tick'
direction = 'select_direction'
benchmark = 'C'
attempt = 'attempt_heal'
heal = 'heal_solution'
solution = 'solution'


#login
r = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + benchmark)
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

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])
#Lines 55-60 show us direction to proceed in.

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

#check the number of options until you check one that's not one

#loop 1
while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])
  

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print("11111111111111111111111111111111111111111")

#loop 2

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print("222222222222222222222222222222222222222222")

#loop 3

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('333333333333333333333333333333333333333333')


#loop 4

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
    r7 = requests.post(s7)
    print(r7.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
    r7 = requests.post(s7)
    print(r7.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

index ='2'

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)



print('444444444444444444444444444444444444444444444')

index ='0'

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
r7 = requests.post(s7)
print(r7.text)

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + solution)
r8 = requests.post(s8)
print(r8.text)


#loop 5

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
    r7 = requests.post(s7)
    print(r7.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

print('===============ENDLOOP=============')

print(r7.text)
lst = r7.text.split()
num1 = 0
num2 = 0
for i in range(len(lst)):
    #print(lst[i])
    if("Challenge" in lst[i]):
        elem1 = lst[i+4]
        print(elem1)
        num1 = int(elem1[:len(elem1)-1])
        elem2 = lst[i+5]
        num2 = int(elem2[:len(elem2)-2])

solution = num1 % num2
    
s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + str(solution))
r8 = requests.post(s8)
print(r8.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('===============CHALLENGECOMPLETED===============')


#loop 6

index ='1'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])
  

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('6666666666666666666666666666666666666666666666666')

#loop 7

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print("77777777777777777777777777777777777777777777777777")

#loop 8

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])

index = '1'

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r8 = requests.post(s8)
print(r8.text)

s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
r2 = requests.post(s2)
print (r2.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('88888888888888888888888888888888888888888888')

#loop 9

index = '0'

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)
my_dictionary = json.loads(test.text)
print(my_dictionary['options'])

s6 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + direction + '/' + index)
r6 = requests.post(s6)
print(r6.text)

while (my_dictionary['number_of_options'] == 1):
    command_family = 'game'
    s2 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + tick)
    r2 = requests.post(s2)
    print (r2.text)
    action = 'get_status'
    test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
    print(test.text)
    s7 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + attempt)
    r7 = requests.post(s7)
    print(r7.text)
    my_dictionary = json.loads(test.text)
    print(my_dictionary['options'])
    if (my_dictionary['player_position'] == 'BrainL_1'):
        break

print(r7.text)

lst1 = r7.text.split()
start_ind = 0
arr = []
for i in range(len(lst1)):
    if ("sum" in lst1[i]):
        start_ind = i+1
        break

while (start_ind <= len(lst1)-1):
    if ("Message" in lst1[start_ind]):
        break
    print(lst1[start_ind])
    arr.append(lst1[start_ind])
    start_ind += 1

print(arr)

last = arr[len(arr)-1]
arr[len(arr)-1] = int(last[:len(last)-2])
print(arr)

for i in range(len(arr)-1):
    temp = arr[i]
    arr[i] = int(temp[:len(temp)-1])
    print(arr[i])

print(sum(arr))
solution = sum(arr)

s8 = (host + '/' + command_family + '/' + user + '/' + secret + '/' + heal + '/' + str(solution))
r8 = requests.post(s8)
print(r8.text)

action = 'get_status'
test = requests.get(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(test.text)

print('=================DONE======================')


#Game is used for logout.
action = 'reset'
logout = requests.post(host + '/' + command_family + '/' + user + '/' + secret + '/' + action)
print(logout.text)