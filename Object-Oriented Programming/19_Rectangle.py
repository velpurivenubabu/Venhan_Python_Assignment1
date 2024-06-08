class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width
    
    def area(self) -> float:
        return self.length * self.width
    
    def perimeter(self) -> float:
        return 2 * (self.length + self.width)

# Example:
rectangle1 = Rectangle(6.0, 4.0)
print("Area:", rectangle1.area())
print("Perimeter:", rectangle1.perimeter())
