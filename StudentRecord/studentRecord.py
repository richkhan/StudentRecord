

#####Declarations

nameString = "Student Name:"
courseGradeStr = "Course Grade:"
averageStr = "Average Grade:"
letterGradeStr = "Final Grade:"


avg = 0

name_array = list()
course_array = list()

#####Banner
print ("\n------------Student Record------------\n")
print ("This Program allows you to search or create student records.")

#Database Search
studentQry = input("Do you want to 'create', or 'search' student record? ")

if (studentQry.lower() == 'create' or studentQry.upper () == 'create'):

	###Data Gathering 
	numOfStudents = input("How many students are there? ")
	if (int(numOfStudents) > 0):
		numOfCourses = input("How many courses are there?")
	elif (int(numOfStudents) == 0):
		print("Closing program.")
		quit()
	else:
		print ("invalid entry")
		
	for i in range(int(numOfStudents)):
		stdName = input("Enter Student Name: ")
		name_array.append(stdName)

		#create txt file with the student name
		with open (stdName + '.txt', 'w') as wf:
			wf.write(nameString + stdName + '\n')
			
			for j in range(int(numOfCourses)):
				c = input("What was their course grade:")
				course_array.append(c)
				wf.write(str(j+1) + ':' + courseGradeStr + c +'\n')
		
			if (int(numOfCourses) > 1):	
				#Calculate GPA 
				total = sum (int(j) for j in course_array)
				avg = total / int(numOfCourses)
			elif (int(numOfCourses) == 1):
				avg = int(c)

			#write GPA to studentname file
			wf.write(averageStr + ':' + str(avg) + '\n')

			if (avg > 100):
				letterGrade = "A+"
			elif (avg > 90 and avg < 100):
				letterGrade = "A"
			elif (avg > 80 and avg < 90):
				letterGrade = "B"
			elif (avg > 70 and avg < 80):
				letterGrade = "C"
			elif (avg > 60 and avg < 70):
				letterGrade = "D"
			elif (avg < 60 ):
				letterGrade = "F"

				
			wf.write(letterGradeStr + ':' + letterGrade + '\n')

	query = input("Do you want to show student's grades? ")
	if (query.lower() == "yes" or query.upper() == "yes" or query.lower() == "y" or query.upper() == "y"):
		try:
			askNum = int(input ("How many students do you want to search? "))
			numOfStudents = askNum
		except ValueError:
			print("Invalid Entry: Must enter integer.")	
		
		
	elif(query.lower() == "no" or query.upper() == "no" or query.lower() == "n" or query.upper() == "n"):
		print("Closing Program...")
		quit()
	
	else:
		print("Invalid Entry")
		print("Closing Program")
		quit()

elif(studentQry.lower() == 'search' or studentQry.upper () == 'search'):
	query = input("Do you want to show student's grades? ")
	if (query.lower() == "yes" or query.upper() == "yes" or query.lower() == "y" or query.upper() == "y"):
		try:
			askNum = int(input ("How many students do you want to search? "))
			numOfStudents = askNum
		except ValueError:
			print("Invalid Entry: Must enter integer.")	
		
		
	elif(query.lower() == "no" or query.upper() == "no" or query.lower() == "n" or query.upper() == "n"):
		print("Closing Program...")
		quit()
	
	else:
		print("Invalid Entry")
		print("Closing Program")
		quit()
else:
	print("Invalid Entry")
	print("Closing Program")
	quit()		

if (int(askNum) <= int(numOfStudents) or studentQry == "search" or studentQry == "search"):
	for k in range (int(askNum)):
		if (query.lower() == "yes" or query.upper() == "yes" or query.lower() == "y" or query.upper() == "y"):
			stdName = input("Search Student Name: " )
			with open (stdName + ".txt", 'r') as rf:
				reader = rf.read()
				print('\n' + reader)
		elif(query == "no" or query == "NO" or query == "No" or query == 'n'):
			quit()

elif (int(askNum) > int(numOfStudents)):
	overide = input ("Would you like to overide the number of students entered in this session? ")
	if (overide.lower() == "yes" or overide.upper() == "yes" or overide.lower() == "y" or overide.upper() == "y"):	
		for k in range (int(askNum)):		
			stdName = input("Search Student Name: " )		
			with open (stdName + ".txt", 'r') as rf:
				reader = rf.read()
				print('\n' + reader)

	elif(overide == "no" or overide == "NO" or overide == "No" or overide == 'n'):
		quit()
