#Polymorphism is having different definitions of the same function name. 
#Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

#parent class shape
class Shape:
    def area(self):
        return "area of the figure is "
## Derived class 1
class Rectangle(Shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
        
    def area(self):
        return self.l * self.b
## Derived class 2
class Circle(Shape):
    def __init__(self,r):
        self.r=r
    
    def area(self):
        return 3.14 * self.r * self.r


Rect=Rectangle(2,3)
print(Rect.area())
C1=Circle(2)
print(C1.area())
