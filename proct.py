   
   #Student procter   

class Student():
	

	def studentdetails(self): #adding the student details
		"""
		Attributes:
			self.student_name --- name of the student
			self.usn  ---- usn of that perticutar student
			self.ph_no
			self.branch----branch of the student_details
			self.marks---student internal and externa marks
		"""
		#dictoinary to store all the personaldatails of the student
		self.student_details = {} 
		self.student_name=input('Enter the student\'s name:')
		self.usn=input('Enter the USN of the student: ')
		self.ph_no=int(input('Enter the phone number of the student: '))
		self.branch=input('Enter the branch in which the student is studying in: ')
		stud_dict = {}
		stud_dict["student_name"] = self.student_name
		stud_dict['ph_no']=self.ph_no
		stud_dict['branch']=self.branch

		self.student_details[self.usn]= stud_dict #using usn as a key



	def display_student_details(self):         #display all the personal details of the student
		
		for i, val in self.student_details.items():
			print(i ,val)



	def enter_marks(self):        #entering the student marks 
		
		a=[]
		i = 0
		#usn is used as pin 
		usn = input("Enter the USN of the student whose marks you want to enter: ") 
		
		while i < 3:
			print(i)
			internal=int(input('enter the marks:'))#to enter  the internal marks

			if internal<=20:
				a.append(internal)
				print(a)
				i += 1
			else:
				print('invalid')
				print(i)
		
		self.student_details[usn]['internal_marks']=a
		
		external=int(input('external marks:')) #external marks 
		if external<=80: 	            
			self.student_details[usn]['external_marks']=external
		else:
			print('invalid')	
		


if __name__ == "__main__":
	student=Student()
	student.studentdetails()
	student.display_student_details()
	student.enter_marks()
	


 

		

				
		
