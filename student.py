# A class starts with a capital letter and in singular form
# A class has properties or attributes 
class Student:
    # student_no 
    # name 
    # email  
    # contact 
    # age  
    # cohort 
    # def__init__() is the constructor used in  oop
    # The self keyword tells that the attribute belong to that particular class
    def __init__(self, student_no, name, email, contact, age, cohort):
        self.student_no = student_no
        self.name = name
        self.email = email
        self.contact = contact
        self.age = age
        self.cohort = cohort 
    # string representation of an object
    def __str__(self):
        return f'{self.student_no}, {self.name}'
# create   a function that returns the student's name, their cohort and email address
# access this function using any instance of the class
  
    def name_email_cohort(self):
        return f'{self.name}, {self.email}, {self.cohort}'
        
        
        
    
# OBJECT/INSTANCE
# Each object has the same attributes form the class
student1 = Student('2023/DCSE/0032/SS', 'Kwagala Joanna Victor', 'kwagjovic@gmail.com', '+256703910899', 21, 3,)
# The object belonging to a class has access the attributes/properties and the class
print(student1.age)
# for the case of the function we call it.
print(student1.name_email_cohort())



 