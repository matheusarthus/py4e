class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5   
    
    def get_picture(self):
        picture = ''

        if self.height > 50 or self.width > 50:
            return "Too big for picture."

        for line in range(self.height):
            picture = picture + (self.width * '*') + '\n'

        return picture

    def get_amount_inside(self, shape):
        externalArea = self.get_area()
        insideArea = shape.get_area()

        timesOfFit = externalArea // insideArea

        return timesOfFit



class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.height})'

    def set_side(self, side):
        self.width = side
        self.height = side
    
    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side