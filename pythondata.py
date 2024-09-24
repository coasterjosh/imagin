import csv
import random
f = open("output.csv", "w")
f.truncate()
f.close()
teams = ['Buffalo Bulls', 'Akron Zips', 'Ball State Cardinals', 'Bowling Green Falcons', 'Central Michigan Chippewas', 'Eastern Michigan Eagles', 'Kent State Golden Flashes', 
         'Miami RedHawks', 'Northern Illinois Huskies', 'Ohio Bobcats', 'Toledo Rockets', 'Western Michigan Broncos' ]

firstnames = ['James', 'Micheal', 'John', 'Richard', "Joshua", 'Adam', 'Ben', 'Rudy', 'Farhan', 'Corey', 'William', 'Brendan', 'Matt', 'Franklin', 'Bryan', 'Hunter', 'Anthony',
              'Mark', 'Andrew', 'Donald', 'Mohammad', 'Sam', 'Cal', 'Calvin', 'Amir', 'Ralph', 'C.J.', 'Jimmy',  'Ronald', 'Thomas', 'George', 'Nick', 'Jeff', 'Gary', 'Eric', 'Jonathan', 'Tom', 'Thomas', 'Brett', 'Steven', 'Steve', 'Larry', 'Benjamin', 'Sam',
              'Samuel', 'Jarvis', 'Jose', 'Jerry', 'Zack', 'Henry', 'Peter', 'Kyle', 'Noah', 'Peter', 'Eric', 'Christian', 'Austin', 'Roger', 'Terry', 'Sean', 'Bo', 'Harold', 'Jordan', 'LeBron', 'Jesse']
lastnames = ['Smith', 'Pierce', 'Filmore', 'Snow', 'Leonard', 'Cooper', 'Love', 'Golden', 'Heartly', 'Brady', 'Mahomes', 'Allen', 'Purdy', 'James', 'Evans', 'Downey', 'Jobs', 
             'Harrison', 'Washinton', 'Jefferson', 'Lincoln', 'Mcdonald', 'Wilson', 'Murray', 'Herman', 'Swift', 'Kelce', 'Bush', 'Clinton', 'Obama', 'Kennedy', 'Hoover', 'Wayne', 'Kent',
             'Parker', 'Quill', 'Romanoff', 'Banner', 'Coolage', 'Pitt', 'Johnson', 'Kennedy', 'Gordon', 'Gordo'] 

numqbs = 3
numk = 2
numdef = 1
numrbs = 4
numwrs = 6
numtes = 2
numweeks = 12
playerid = 1000000
def getFirst():
    return random.choice(firstnames)
def getLast():
    return random.choice(lastnames)
def getRushing():
    return random.randint(0, 200)
def getPassingQB():
    return random.randint(0, 400)
def getPassing():
    return random.randint(0, 20)
def getTDs():
    return random.randint(0, 4)
def getReceptions():
    return random.randint(0, 13)
def getRecieving():
    return random.randint(0, 250)
def getfieldgoal():
    return random.randint(0,6)
def getpointsallowed():
    return random.randint(0, 55)
def getinterceptions():
    return random.randint(0,5)
def getPlayerID(x):
    playerid = x
    playerid = playerid + 1
    return playerid



data = []
data.append(['player ID ', 'Position ', 'name ','school ', 'week ', 'touchdowns ', ' receptions ', 'rushing-yards ', 'recieving-yards ', 'passing-yards ', 'field goals ', 'points allowed ', 'interceptions'])
# CSV FORMAT!!! playerid, position, name, school, week, tds, receptions, rushing yards, recieving yards, passing yards, field goals, points allowed, interceptions
for i in teams:
    for q in range(1, numqbs+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'QB', name,i, a, getTDs(), getReceptions(), getRushing(), getRecieving(), getPassingQB(), 0, 0, 0])

    for r in range(1, numrbs+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'RB', name,i, a, getTDs(), getReceptions(), getRushing(), getRecieving(), getPassingQB(), 0, 0, 0])
    for w in range(1, numwrs+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'WR', name,i, a, getTDs(), getReceptions(), getRushing(), getRecieving(), getPassingQB(), 0, 0, 0])

    for t in range(1, numtes+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'TE', name,i, a, getTDs(), getReceptions(), getRushing(), getRecieving(), getPassingQB(), 0, 0, 0])
    for k in range(1, numk+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'k', name,i, a, 0, 0, 0, 0, 0, getfieldgoal(), 0, 0])
    for d in range(1, numdef+1):
        id = getPlayerID(playerid)
        playerid = id
        first = getFirst()
        last = getLast()
        name = first + ' ' + last
        for a in range(1, numweeks+1):
            
            data.append([playerid, 'D', i,i, a, 0, 0, 0, 0, 0, 0, getpointsallowed(), getinterceptions()])
    
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for f in data:
        writer.writerow(f)






