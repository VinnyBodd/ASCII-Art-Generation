#Citation 1: Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document]. 
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015)
#Citation 2:Using readlines in python? First time,Stack Overflow(2015-11-08).Retrieved from http://stackoverflow.com/questions/12996220/using-readlines-in-python-first-time

#load the file, read all the ascii characters
def loadFile():
	while True:
		try:
			fileName = input("File name to load :")
			fileHnd1 = open(fileName, "r")

			asciiLetterUsed = fileHnd1.readline() #reads the first line in text file
			print("These are ascii letters used: ", asciiLetterUsed)
			
			#the program will crash without the row.strip("\n")
			fileData = [row.strip("\n") for row in fileHnd1.readlines()] #stores all the ascii characters in the list. #also removes empty string line
			
			print("This is the image: \n")
			for row in range (0, len(fileData)):
				print(fileData[row])
			fileHnd1.close()
			
			break
		except FileNotFoundError: #stops the program from breaking
			print("File not Found ")
		except:#stops the program from breaking
			print("Some other error occurred.")
	return asciiLetterUsed, fileData, fileName

#menu where user is given options to choice
def menu():
	asciiLetterUsed, fileData, fileName = loadFile() #get ascii characters, file data and file name
	while True:
		
		print("pick the letter from A to E")
		print("A. Horizontal Flip.")
		print("B. Vertical Flip.")
		print("C. Rotate the image 90 degrees")
		print("D. invert the image")
		print("S. Save file and quit")
		menuSel = input("").upper() #get user selection
		
		#if its A then Flip horizontal
		if (menuSel == "A"):
			fileData = flipHor(fileData) #send File Data and get new ascii characters
			#nested for loops to go through the list and output the ascii characters
			for row in range (0, len(fileData)):
				for column in range (0, len(fileData[row])):
					print(fileData[row][column], end="")
				print("")
		
		#else if its B then Flip vertical		
		elif (menuSel == "B"):
			fileData = flipVer(fileData)
			for row in range (0, len(fileData)):
				for column in range (0, len(fileData[row])):
					print(fileData[row][column], end="")
				print("")
		#else if its C then rotate 90 degrees
		elif (menuSel == "C"):
			fileData = imgRotate(fileData)
			for row in range (0, len(fileData)):
				for column in range (0, len(fileData[row])):
					print(fileData[row][column], end="")
				print("")
		#else if its D then invert the image		
		elif (menuSel == "D"):
			fileData = imgInvert(fileData, asciiLetterUsed)
			for row in range (0, len(fileData)):
				for column in range (0, len(fileData[row])):
					print(fileData[row][column], end="")
				print("")
		#else if its S then save it to the file
		elif(menuSel =="S"):
			saveFile(asciiLetterUsed,fileData,fileName)
			break
		else:
			print("Invalid input")
		
#file horizontal			
def flipHor(fileData):
	lst = [] 
	#nested for loop to go through file Data and horizontal flip
	for row in range (0, len(fileData)):
		rowString = ""
		for column in range (len(fileData[row]) - 1, -1, -1):
			newLetter = fileData[row][column]
			rowString += newLetter
		lst.append(rowString)#add to the list
	return lst

#file Vertical	
def flipVer(fileData):    
	lst = []
	#nested for loop to go through file data and vertical flip
	for row in range (len(fileData)-1,-1,-1):
		rowString = ""
		for column in range (0,len(fileData[row])):
			newLetter = fileData[row][column]
			rowString += newLetter
		lst.append(rowString) #add to the list
	return lst

#image rotate 
def imgRotate(fileData):
	lst = []
	
	for row in range (0, len(fileData[0])):
		rowString = ""
		observableRow = ""
		for column in range (len(fileData) - 1, -1, -1):
			newLetter = fileData[column][row]
			rowString += newLetter
			
			if (len(observableRow) < 80):
				observableRow += newLetter
	
		lst.append(observableRow)
	return lst
#invert the image
def imgInvert(fileData, asciiLetterUsed):
	lst = []
	for row in range (0, len(fileData)):
		rowString = ""
		observableRow = []
		for column in range (0, len(fileData[row])):
			asciiLetter = fileData[row][column]
			if (asciiLetter =="."):
				newLetter = "@"
			elif (asciiLetter ==","):
				newLetter = "$"
			elif (asciiLetter =="*"):
				newLetter = "#"
			elif (asciiLetter =="~"):
				newLetter = "%"
			elif (asciiLetter =="="):
				newLetter = "/"
			elif (asciiLetter =="@"):
				newLetter = "."
			elif (asciiLetter =="$"):
				newLetter = ","
			elif (asciiLetter =="#"):
				newLetter = "*"
			elif (asciiLetter =="%"):
				newLetter = "~"
			elif (asciiLetter =="/"):
				newLetter = "="
			rowString += newLetter
			if(len(observableRow) <80):
				observableRow +=newLetter
		lst.append(observableRow)
	return lst
	
#writing to the file	
def saveFile(asciiLetter,fileData,fileName):
	print(asciiLetter)
	filehnd1 =open(fileName, "w")#write to the file
	filehnd1.write(str(asciiLetter)+"\n")
	#nested for loop to go through the 2D list and print characters
	for column in range(0, len(fileData)):
		for rows in range(0, len(fileData[column])):
			txt= fileData[column][rows]
			filehnd1.write(txt)
			print(fileData[column][rows],end="")
		#if statement to start at new line
		if (len(fileData[column]) <=80):
			filehnd1.write("\n")
			print()

menu()

