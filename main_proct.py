from proct import Student
student=Student()

while True:
	choice=int(input('1. Enter Student Details \n2. Enter Marks of a student \n3. View Student Details \n4. Exit \n\
Please enter your choice: ')) 

	
	if choice==1:
		""" if user choose 1-- give personal details of student"""
		print('\n','='*50)
		print('You will have to enter the personal details of one student\n')
		student.studentdetails()
	
	elif choice == 2:
		"""if user choose2--enter  student marks """ 
		print('\n','='*50)
		print('Enter the marks of the student- ')
		student.enter_marks()

	elif choice==3:
		"""to see the complete details of the student"""
		print('\n','='*50)
		print('Displaying the marks of students')
		student.display_student_details()
	
	else:
		"""to exit out of from the loop"""
		break





 	













