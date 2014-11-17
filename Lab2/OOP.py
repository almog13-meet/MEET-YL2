class animal:
    def __init__ (self, name, age):
        self.n = name
        self.a = age
    def sleep(self):
        print self.n, "who is", self.a, "years old is sleeping"
    def eat(self):
        print self.n, "who is", self.a, "years old is eating"
class bird(animal):
    def __init__ (self, name, age, wings):
        animal.__init__ (self, name, age)
        self.w = wings
    def fly(self):
        print self.n, "who is", self.a,"years old and has", self.w, "wings is flying"
class dog(animal):
    def __init__ (self, name, age, tail):
        animal.__init__ (self, name, age)
        self.t = tail
    def bark(self):
        print self.n, "who is", self.a,"years old and has a", self.t, "tail is barking"
        


a = bird("tweetie", 2, "blue")
b = dog("rex", 5, "brown")
