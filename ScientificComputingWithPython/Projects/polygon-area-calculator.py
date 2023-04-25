class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5
    
    def get_picture(self):

        if self.width > 50 or self.height > 50 :
            return "Too big for picture."
        
        picture = ("*" * self.width + "\n") * self.height

        return picture
    
    def get_amount_inside(self, shape):
        return int(self.width / shape.width) * int(self.height / shape.height)

    def __str__(self):
        return "Rectangle(" + "width=" + str(self.width) + ", " + "height=" + str(self.height) + ")"
    
class Square(Rectangle):
        
    def __init__(self, side):
        self.width = side
        self.height = side
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return "Square(" + "side=" + str(self.width) + ")"  #It's a square, use width or height is the same

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))