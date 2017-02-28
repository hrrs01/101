
import sys
import time

variables = {}
filename = sys.argv[1]
fileLines = []

commands = []

loops = {}

file = open(filename, "r");
def file_len(fname):
	with open(fname) as f:
		for i, l in enumerate(f):
			pass
	return i+1

temp = 0
	
for linenum in range(file_len(filename)):
	fileLines.append(file.readline())


for line in fileLines:
	line = line.rstrip()

	temp = line.split(" ")

	for x in temp:
		commands.append(x)


x = 0

def statement_checker(arg1, type, arg2):
	
	if type == "00":
		if returnVarValue(arg1) == returnVarValue(arg2):
			return True
		else:
			return False
	elif type == "11":
		if returnVarValue(arg1) == returnVarValue(arg2):
			return False
		else:
			return True
	elif type == "01":
		if returnVarValue(arg1) < returnVarValue(arg2):
			return True
		else:
			return False
	elif type == "10":
		if returnVarValue(arg1) > returnVarValue(arg2):
			return True
		else:
			return False
	
def commandChecker():
	global x
	global commands
	if len(commands[x]) == 5:
		createVar()
		
	elif len(commands[x]) == 3 or len(commands[x]) == 4:
		checkKeyWord()
		
def localCommandChecker(commands, x=0):
	
	while x < len(commands):
		if len(commands[x]) == 5:
			x = createLocalVar(x, commands)
			
			
		elif len(commands[x]) == 3 or len(commands[x]) == 4:
			x = checkLocalKeyWord(x,commands)
		x += 1
		
def returnVarValue(varName):
	if len(varName) >= 6:
		return int(varName,2)
	elif len(varName) == 1:
		if varName == "1":
			return True
		else:
			return False
	return variables[varName]


	
def checkKeyWord():
	global x
	global commands
	global temp
	temp = 5
	if commands[x] == "001":
		x += 1
		statement = commands[x]
		commandList = []
		x += 1
		while commands[x] != "111":
			commandList.append(commands[x])
			x += 1
		while_loop(statement, commandList)	
	elif commands[x] == "1111":
		x += 1
		print(returnVarValue(commands[x]))
	elif commands[x] == "0000":
		x+=1
	elif commands[x] == "1001":
		x+=1
		time.sleep(float(int(commands[x],2))/10)
		
	
		
		
	

def checkLocalKeyWord(x, commands):
	
	if commands[x] == "001":
		x += 1
		statement = commands[x]
		commandList = []
		x += 1
		while commands[y] != "111":
			commandList.append(commands[x])
			x += 1
		while_loop(statement, commandList)
		
	if commands[x] == "101":
		x+= 1
		statement = commands[x]
		commandList = []
		x += 1
		while commands[y] != "111":
			commandList.append(commands[x])
			x+=1
		if_func(statemnt, commandList)
	
	elif commands[x] == "1111":
		x += 1
		print(returnVarValue(commands[x]))
	elif commands[x] == "0000":
		x+= 1
	elif commands[x] == "1001":
		x+=1
		
		time.sleep(float(int(commands[x],2))/10)
		
	
	return x
		

def createVar():
	global x
	global commands
	if len(commands[x+1]) >= 6:
			variables[commands[x]] = int(commands[x+1], 2)
	elif commands[x+1] == "1":
			variables[commands[x]] = True
	elif commands[x+1] == "0":
			variables[commands[x]] = False
	elif commands[x+1] == "0001":
			variables[commands[x]] += int(commands[x+2],2)
	elif commands[x+1] == "0011":
			variables[commands[x]] -= int(commands[x+2],2)
	elif commands[x+1] == "0010":
			variables[commands[x]] /= int(commands[x+2],2)
	elif commands[x+1] == "0111":
			variables[commands[x]] *= int(commands[x+2],2)
	
def if_func(statement, commandList):
	if len(statement) == 2:
		if statement_checker(commandList[0], statement, commandList[1]):
			localCommandChecker(commandList, 2)
	else:
		if returnVarValue(statement):
			localCommandChecker(commandList)
	
def createLocalVar(x, commands):
	
	if len(commands[x+1]) >= 6:
			print len(commands[x+1])
			variables[commands[x]] = int(commands[x+1], 2)
	elif commands[x+1] == "1":
			variables[commands[x]] = True
	elif commands[x+1] == "0":
			variables[commands[x]] = False
	elif commands[x+1] == "0001":
			variables[commands[x]] += int(commands[x+2],2)
	#print variables
	elif commands[x+1] == "0011":
			variables[commands[x]] -= int(commands[x+2],2)
	elif commands[x+1] == "0010":
			variables[commands[x]] /= int(commands[x+2],2)
	elif commands[x+1] == "0111":
			variables[commands[x]] *= int(commands[x+2],2)
	
	return x
	
def while_loop(statement, commandList):
	
	
	if len(statement) == 2:
		while statement_checker(commandList[0], statement, commandList[1]):
			localCommandChecker(commandList, 2)
	else:
		while returnVarValue(statement):
			localCommandChecker(commandList)

while x < len(commands):
	commandChecker()
		
	x += 1
		
	
	