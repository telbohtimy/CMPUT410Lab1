class Student:
    courseMarks={}
    name=""
    def __init__(self,name,family):
	self.name=name+' '+family
    def addCourseMark(self,course,mark):
	self.courseMarks[course]=mark
    def average(self):
	avg=0
	for v in self.courseMarks.values():
	    avg=avg+v
	avg=avg/len(self.courseMarks)
	return avg
#Tests
#s=Student("Tarek","El Bohtimy")
#s.addCourseMark('a',4)
#s.addCourseMark('b',3)
#s.addCourseMark('c',5)
#s.addCourseMark('d',10)
#s.addCourseMark('e',8)
#print(s.average())


