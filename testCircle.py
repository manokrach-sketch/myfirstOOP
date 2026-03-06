from circle import Circle
def main():
    circle0 = Circle()
    print(f"The perimeter of the circle with radius {circle0.radius} units is {circle0.getPerimeter():.4f} units")
    
    circle1 = Circle(125)
    print(f"The perimeter of the circle with radius {circle1.radius} units is {circle1.getPerimeter():.4f} units")
    
    circle2 = Circle(100)
    print(f"The perimeter of the circle with radius {circle2.radius} units is {circle2.getPerimeter():.3f} units")
    
    circle3 = Circle(2500)
    print(f"The perimeter of the circle with radius {circle3.radius} units is {circle3.getPerimeter():.2f} units")
main()

