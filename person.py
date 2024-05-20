class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am {self.gender}")
#create instance of person class
person2 = Person("Nana", "22", "female")
#create the introduce methodto display the information
person2.introduce()