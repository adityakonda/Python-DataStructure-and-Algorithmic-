class Person:
    def __init__(self, person, age):
        self.name = person
        self.age = age

    def my_func(self,text):
        print("Hello ", self.name, "you age is: ",self.age, text)



p1 = Person("Aditya", 30)
p1.my_func("hello")