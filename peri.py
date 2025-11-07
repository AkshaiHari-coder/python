class Rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def peri(self):
        return 2*(self.length+self.breadth)
l=int(input("enter length"))
b=int(input("enter breadth"))
rect = Rectangle(l,b)
print("Area of the rectangle: ",{rect.area()})
print("Perimeter of the rectangle: ",{rect.peri()})
