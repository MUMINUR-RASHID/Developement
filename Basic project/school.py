class Students:
    def __init__(self,Name,Course,Id):
        self.name=Name
        self.course=Course
        self.id=Id

    def __repr__(self) -> str:
        return f"Student: {self.name}, Course: {self.course}, Id: {self.id}"


class Teachers:
    def __init__(self,Name,Course,Id):
        self.name=Name
        self.course=Course
        self.id=Id

    def __repr__(self) -> str:
        return f"Teacher: {self.name}, Course: {self.course}, Id: {self.id}"




class School:
    def __init__(self,Name):
        self.name=Name
        self.teachers=[]
        self.students=[]


    def add_teacher(self, Name, Course):
        id=len(self.teachers)+101
        teacher=Teachers(Name,Course,id)
        self.teachers.append(teacher)


    def add_student(self, Name, Course):
        id=len(self.students)+1
        student=Students(Name,Course,id)
        self.students.append(student)


school=School("Phitron")

school.add_student("Nipu","C")
school.add_student("Tarek","C++")
school.add_student("Jibon","Python")
school.add_student("Rubel","C")
school.add_student("Jubair","Java")



school.add_teacher("Mijan", "DS")
school.add_teacher("Rupom", "Algorithm")
school.add_teacher("Dilen", "Math")
school.add_teacher("Afia", "Programming")
school.add_teacher("Husna", "Logic")

print(f"---------- Welcome To {school.name} ----------")

print(f"---------- This Is Our Students List ----------")
for st in school.students:
    print(st)

print(f"---------- This Is Our Teachers List ----------")
for th in school.teachers:
    print(th)


print("---------- Thank You ----------")


