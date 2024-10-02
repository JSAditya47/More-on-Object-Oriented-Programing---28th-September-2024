class Circle:
    
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.1416 * (self.radius ** 2)
    
    def circumference(self):
        return 2 * 3.1416 * self.radius
    
radius = float(input("Enter the Radius: "))
circle = Circle(radius)

print(f"Radius: {radius}")
print(f"Area: {circle.area()}")
print(f"Circumference: {circle.circumference()}")
