# class Student:
#     roll_no = None
#     name = None

# s0 = Student()
# s0.roll_no=0
# s0.name = 'Dfadjf'
# print(s0.roll_no,s0.name)

# s1 = Student()
# print(s1.roll_no,s1.name)

# s2 = Student()
# s2.roll_no=2
# s2.name = 'hwrgf'
# print(s2.roll_no,s2.name)

# s50 = Student()
# s50.name = 'nagiorn'
# print(s50.roll_no,s50.name)




class Student:
    count=0
    def __init__(self,roll_no,name):
        self.roll_no =roll_no
        self.name = name

    def display(self):
        print(self.roll_no,self.name)

s0 = Student(0,'Dfadjf')
s0.display()
s0.count=5
Student.count+=1
print(s0.count)

s1 = Student(1,'fdgdf')
print(s1.roll_no,s1.name)
Student.count+=1
print(s1.count)
s1.count=9
print(s1.count)

print(s0.count)
print(Student.count)


'''
Here count variable belongs to clas itself as well as object
But roll_no, name all these variable belongs to only object
in line 47 when we call the s0.count=5 it assigns count variable of s0 object as 5
but count variable for Student class is still 0.
so when we call Student.count+=1 (line 37) it only increment the count varible only for class the class
it cannot affect any other object's value of count which is assigned already.
when we again call Student.count+=1 (line 42) the class variable count becomes 2
as still now no value is assigned for s1.count, when print s1.count it shows output 2 as value of the count of class is 2
but when we assign 8 for s1.count, it only change the value for s1 not for class
that's why we again print Student.count it gives 2
'''