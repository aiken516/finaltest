class Point:
    __x = 0
    __y = 0

    def __init__(self, xn=0, yn=0):
        self.__x = xn
        self.__y = yn

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def distance(point1, point2):
        return ((point1.getX() - point2.getX())**2 + (point1.getY() - point2.getY())**2)**(1/2)

    def __add__(self, point2):
        return Point(self.getX() + point2.getX(), self.getY() + point2.getY())


p1 = Point(1,1)
p2 = Point(2,2)
print(Point.distance(p1,p2))
p3 = p1 + p2
print("p1:{0:d}, p2:{1:d}".format(p3.getX(), p3.getY()))
