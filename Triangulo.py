class Triangulo:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def type(self):
        if self.side1 == self.side2 == self.side3:
            return "Equilátero"
        elif self.side1 == self.side2 or self.side2 == self.side3 or self.side1 == self.side3:
            return "Isósceles"
        else:
            return "Escaleno"

    def maxside(self):
        return max(self.side1, self.side2, self.side3)