class bulletInfo:
    img = None
    xCordinate = None
    yCordinate = None
    imgW = None
    imgH = None
    speedN = None
    angle = None
    shipFacingDirection = None

    def __init__(self, img, xCordinate, yCordinate, imgW, imgH, speedN, angle, shipFacingDirection):
        self.img = img
        self.xCordinate = xCordinate
        self.yCordinate = yCordinate
        self.imgW = imgW
        self.imgH = imgH
        self.speedN = speedN
        self.angle = angle
        self.shipFacingDirection = shipFacingDirection

    def getImage(self):
        return self.img

    def getX(self):
        return self.xCordinate

    def getY(self):
        return self.yCordinate

    def getWidth(self):
        return self.imgW

    def getHeight(self):
        return self.imgH

    def getSpeed(self):
        return self.speedN

    def getAngle(self):
        return self.angle

    def getShipHeadedTowards(self):
        return self.shipFacingDirection

    def setImage(self, img):
        self.img = img

    def setX(self, xCordinate):
        self.xCordinate = xCordinate

    def setY(self, yCordinate):
        self.yCordinate = yCordinate

    def setWidth(self, imgW):
        self.imgW = imgW

    def setHeight(self, imgH):
        self.imgH = imgH

    def setSpeed(self, speedN):
        self.speedN = speedN

    def setAngle(self, angle):
        self.angle = angle

    def toString(self):
        return f"XPosition: {self.xCordinate}, YPosition: {self.yCordinate}, Image dimensions: {self.imgW}x{self.imgH}"
