# student1 = {
#   "f_name":"Test",
#   "l_name":"Doe",
#   "age":999,
#   "isNinja":False
# }
# student2 = {
#   "f_name":"John",
#   "l_name":"Doe",
#   "age":1,
#   "isNinja":True
# }


class Student:
  
  # Constructor / init function
  # instance method
  def __init__(self,first_name,last_name,age,is_ninja=False):
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.is_ninja = is_ninja
  def __str__(self):
    return f"Student values \n firstName: {self.first_name}\n lastName: {self.last_name}\n age: {self.age}\n isNinja: {self.is_ninja}"
    
  def say_hi(self):
    return f"Hello,{self.first_name}"
  
  def get_older(self):
    self.age += 1
    # self.age = self.age + 1
    return self.age

# create instance of the class Student
student1 = Student("Test","Doe",999,True)
print(student1.say_hi())
print(student1.get_older())
print(student1.get_older())
print(student1.get_older())
print(student1.get_older())
print(student1)