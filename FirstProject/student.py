#Student.py

class Student:
	def __init__(self,sno,sname,height):
		self.sno=sno;
		self.sname=sname;
		self.height=height;
	#def display(self):
	#	print(self.sno,self.sname,self.height)
		
	def __str__(self):
		ss=str(self.sno)+"\t"+self.sname+"\t"+str(self.height);
		return ss;
	
s1 = Student(1001,"Sai",6.2);
s2 = Student(1002,"Ram",5.9);
s1.display()
s2.display()
#print(s1)
#print(s2)

