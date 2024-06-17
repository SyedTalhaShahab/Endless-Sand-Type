class enemyInfo:
    color = [255, 255, 255]
    radians = 0
    angle = 0
    image, term, x, y, height, width, speed = None, None, None, None, None, None, None


    def __init__(self, image, term, x, y, width, height, speed):
        self.image = image
        self.term = term
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def getRadians(self):
        return self.radians

    def getAngle(self):
        return self.angle

    def getColor(self):
        return self.color

    def getWord(self):
        return self.term

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getAcceleration(self):
        return self.speed

    def getImage(self):
        return self.image

    def setWord(self, term):
        self.term = term

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setColor(self, color):
        self.color = color

    def setAngle(self, angle):
        self.angle = angle

    def setRadians(self, radians):
        self.radians = radians

    def toString(self):
        print("Word:", self.term, "XPos:", self.x, "YPos:", self.y, "Width:", self.width,
              "Height:", self.height, "Speed:", self.speed, "Angle Facing:", self.angle)

    def toStringSameNames(self):
        print("Word:", self.term, "XPos:", self.x, "YPos:", self.y, "Width:", self.width,
              "Height:", self.height, "Speed:", self.speed, "Angle Facing:", self.radians)
