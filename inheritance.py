class sweetfruits:
    taste="sweet"
    def getTaste(self):
        print("it tatse sweet")

class Apple(sweetfruits):
    colour="red"
    def details(self):
        print("Name=Apple\nColor={}\nTaste={}".format(self.colour,self.taste))

obj=Apple()
obj.details()