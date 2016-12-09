#Citation 1: Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document]. 
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015)

from SimpleGraphics import* 

#function to get file name
def file(convChars):
	fileName = str(input("What is the file name: ")) 
	return(fileName)

#user input function gets user image and loads it. Also gets what type of background to run	
def userInput():
	#loop until the image is less than 80
	while True:
		imgName = str(input("Name of the Image: "))
		imgLoaded = loadImage(imgName)
		drawImage(imgLoaded,0,0)
		if(getWidth(imgLoaded) >80):
			print("Image width needs to be less than 80")
		else:
			break 
	
	convType = str(input("T if white background or F if black background"))
	#if its F then black background	
	if(convType == "F"): 
		convType = True
		convChars = [".",",","*","~","=","/","%","#","$","@"]
	#else if its T then white background
	elif(convType== "T"):
		convType = False
		convChars = ["@","$","#","%","/","=","~","*",",","."]
	#else its white background
	else:
		print("error, unrecognizable input. Default settings, black background")
		convChars = [".",",","*","~","=","/","%","#","$","@"]
		convType =False
	#returning the image and characters
	return(imgLoaded,convChars)

#this function turns the pixels to greyScale
def greyScale(img):
	print("gray is working")
	#nested for loop to go through the image
	for x in range(0, getWidth(img)):
		for y in range(0, getHeight(img)):
			# Retrieve the amounts of red, green and blue for the pixel
			r, g, b = getPixel(img, x, y)
			# Compute the average intensity
			avg = (r + g + b) / 3

			# Update the pixel so that it has equal amounts of red, green and blue
			putPixel(img, x, y, avg, avg, avg)
	# Display the modified image
	drawImage(img, 0, 0)
	return img

#this function turns the each pixel to ascii art
def conversion(img,characters):
	print("conversion is happening")
	
	asciiList = []#2D list
	convChars =characters #get characters from argument
	for rows in range(0, getHeight(img)):
		asciiRow = []#list for the row
		for column in range(0, getWidth(img)):
			r, g, b = getPixel(img, column, rows)#get greyscale avg
			avg = r
			if (avg >= 0 and avg <= 25.5):
				asciiRow.append(convChars[0])
			elif (avg > 25.5 and avg <= 51):
				asciiRow.append(convChars[1])
			elif (avg > 51 and avg <= 76.5):
				asciiRow.append(convChars[2])
			elif (avg > 76.5 and avg <= 102):
				asciiRow.append(convChars[3])
			elif (avg > 102 and avg <= 127.5):
				asciiRow.append(convChars[4])
			elif (avg > 127.5 and avg <= 153):
				asciiRow.append(convChars[5])
			elif (avg > 153 and avg <= 178.5):
				asciiRow.append(convChars[6])
			elif (avg > 178.5 and avg <= 204):
				asciiRow.append(convChars[7])
			elif (avg > 204 and avg <= 229.5):
				asciiRow.append(convChars[8])
			elif (avg > 229.5 and avg <= 255):
				asciiRow.append(convChars[9])
	
		asciiList.append(asciiRow)#add to the list
	return(asciiList)

#main function to output the characters	
def main():
	img,convChars =userInput()
	fileName =file(convChars)
	img =greyScale(img)
	lst = conversion(img,convChars)
	
	filehnd1 =open(fileName, "w") #write to the file
	filehnd1.write(str(convChars)+"\n")
	#nested for loop to go through the 2D list and print characters
	for column in range(0, len(lst)):
		for rows in range(0, len(lst[column])):
			txt= lst[column][rows]
			filehnd1.write(txt)#writing txt to the file
			print(lst[column][rows],end="")
		#if statement to start at new line
		if (len(lst[column]) <=80):
			filehnd1.write("\n") #new line
			print()
	filehnd1.close()

main()