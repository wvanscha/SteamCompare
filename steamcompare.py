import requests
import re
import sys

#Check input
if len(sys.argv) != 3 : 
	print( 'Please input two Steam user IDs as arguments\n' ) 
	sys.exit()

input1 = str(sys.argv[1])
input2 = str(sys.argv[2])

try: 
	int(input1)
	input1 = 'profiles/' + input1
except ValueError:
	input1 = 'id/' + input1

try: 
	int(input2)
	input2 = 'profiles/' + input2
except ValueError:
	input2 = 'id/' + input2

#Get html of user page
userOne = requests.get('https://steamcommunity.com/' + input1 + '/games/?tab=all&sort=name')
userTwo = requests.get('https://steamcommunity.com/' + input2 + '/games/?tab=all&sort=name')

if userOne.status_code != 200 :
	print( 'Error getting first user\n' ) 
	sys.exit()
	
if userTwo.status_code != 200 :
	print( 'Error getting second user\n' ) 
	sys.exit()

#Make list of games with regex
resultOne = re.findall( '"name":"(.+?)","logo"', userOne.content ) 
resultTwo = re.findall( '"name":"(.+?)","logo"', userTwo.content ) 
	
print( "\nGames in common\n")

commonGames = list(set(resultOne).intersection(resultTwo))
commonGames.sort()

for elem in commonGames:
	print elem 

print( "\n")
