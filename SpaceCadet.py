import pygame
import os
import math
import sys
from tkinter import *
from pygame.locals import *
import random
import enemyInfo as ship
import bulletInfo as bullet

pygame.font.init()
pygame.init()

# get the size of window
root = Tk()
M_WIDTH = root.winfo_vrootwidth()
M_HEIGHT = root.winfo_screenheight()
# 1536 M_WIDTH
# 864 M_HEIGHT
screen = pygame.display.set_mode((M_WIDTH, M_HEIGHT))

Dict = []
enemy_List = []
enemy_Number = 4
bg_Speed = 2

player_X_Pos = (M_WIDTH / 2) - 20
player_Y_Pos = (M_HEIGHT - 50)

# vars
total_FPS = 2000
TXT_COLOR = (255, 0, 0)

font = pygame.font.SysFont("Verdana", 20)
header = pygame.font.SysFont("Verdana", 40)

clock = pygame.time.Clock()

# bullets fired by the ship
current_Lazers_List = []

player_Boundaries = pygame.Rect(player_X_Pos, player_Y_Pos, 40, 40)

score_Var = 0
wrds_Typd = 0
trajectoryAngle = 0
livesVar = 3
lvl_Var = 0
EMP_Stored = 3
displayDistance = 0
target_Var = ""

# title
pygame.display.set_caption('Space Cadet')


# icon image
icon = pygame.image.load(os.path.join("Sprites", "icon.jfif"))
pygame.display.set_icon(icon)

# Emp
EMPImg = pygame.image.load(os.path.join("Sprites", "plasmaICON.jpg"))
EMPImg = pygame.transform.scale((EMPImg), (30, 30))

BG_IMG = pygame.image.load(os.path.join(
    "Sprites", "waterJPG.jpg"))

top = pygame.image.load(os.path.join(
    "Sprites", "topPNG.png"))
bottom = pygame.image.load(os.path.join(
    "Sprites", "bottomPNG.png"))

BG_IMG = pygame.transform.scale((BG_IMG), (M_WIDTH, M_HEIGHT))


bottomControls = pygame.transform.scale(
    (bottom), (M_WIDTH, bottom.get_height()))
topControls = pygame.transform.scale((top), (M_WIDTH, top.get_height()))

# player
user = pygame.image.load(os.path.join("Sprites", "player.png"))
user = pygame.transform.scale((user), (20, 20))

# bullets
LAZER = pygame.image.load(os.path.join("Sprites", "blueShot.png"))


def createShips(totalEnemies):
    while (totalEnemies > 0):
        randomShipNum = random.randrange(4)
        enemyImage = pygame.image.load(os.path.join(
            "Sprites", f"enemy{randomShipNum}.jpg"))
        enemyImage = pygame.transform.scale((enemyImage), (30, 30))
        # no need to exclude words already used
        randomWord = Dict[random.randint(0, (len(Dict)-1))]
        randomSpeed = .09
        randomX = random.randint(0, M_WIDTH)  # random x
        randomY = ((random.randint(50, 100))*-1)  # random y
        currentShip = ship.enemyInfo(enemyImage, randomWord, randomX, randomY, 30, 30, randomSpeed)
        enemy_List.append(currentShip)
        totalEnemies = totalEnemies - 1

# def createDic():
#     global Dict
#     global dictS_ize
#     f = open("Dictionary.txt", "r")
#     lines = f.readlines()
#     for line in lines:
#         word = line.strip('\n')
#         if (len(line)) > 6 and word.isalpha() == True:
#             Dict.append(word.lower())
#     dictS_ize = len(Dict)

def createDic():
    global Dict
    global dictS_ize
    Dict = []  # Initialize Dict as an empty list
    with open("Dictionary.txt", "r") as f:
        lines = f.readlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        word = line.strip('\n')
        if len(line) > 6 and word.isalpha():
            Dict.append(word.lower())
        index += 1
    dictS_ize = len(Dict)

class FPS():
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = font
        self.text = self.font.render(
            str(self.clock.get_fps()), True, TXT_COLOR)

    def render(self, display):
        self.text = self.font.render(
            str(round(self.clock.get_fps())), True, TXT_COLOR)
        # fps screen postion
        display.blit(
            self.text, (M_WIDTH - (self.text).get_width() - 5, M_HEIGHT - 80))
# self.text, (M_WIDTH - (self.text).get_width() - 5, M_HEIGHT - 30))


def storedEMPs():  # shows stored emp blasts
    global EMPImg
    global EMP_Stored
    # shows 3 shockwaves images
    initX = M_WIDTH - 30
    for index in range(EMP_Stored):
        screen.blit(EMPImg, (initX, 5))
        initX -= 30


def showFactsAndPlayer():
    """
    the purpose of these labels is to show the person on the screen where each of the values of the ship are
    """
    global score_Var
    global wrds_Typd
    global trajectoryAngle
    global livesVar
    global lvl_Var
    # show stored EMP images

    """
    thee stored emps display the images
    """
    storedEMPs()
    screen.blit(user, ((M_WIDTH/2) - 20, (M_HEIGHT - 50)))

    # shows player image
    # shows emp (word)

    """
    font render is used to show numbers
    """
    EMPs_lbl = font.render(f"EMPs: ", 1, TXT_COLOR)
    screen.blit(EMPs_lbl, (M_WIDTH - (EMPs_lbl).get_width() - 80, 5))

    # shows Words Typed
    wrds_typed = font.render(f"Words Typed: {wrds_Typd}", 1, TXT_COLOR)
    screen.blit(wrds_typed, (M_WIDTH - (wrds_typed).get_width() -
                5, EMPs_lbl.get_height() + 5))

    # shows score
    score_lbl = font.render(f"Score: {score_Var}", 1, TXT_COLOR)
    screen.blit(score_lbl, (M_WIDTH - (score_lbl).get_width() - 5,
                wrds_typed.get_height() + EMPs_lbl.get_height() + 5))

    # shows fps (word)
    fps_lbl = font.render(
        f"Nearest Ship: {round(displayDistance)}", 1, TXT_COLOR)

    # shows user angle
    t_angle_lbl = font.render(f"Enemy Count: {len(enemy_List)}", 1, TXT_COLOR)
    screen.blit(t_angle_lbl, (M_WIDTH - (t_angle_lbl).get_width() -
                5, M_HEIGHT - fps_lbl.get_height() - 30))

    # shows distance
    nearest_ship = font.render(
        f"FPS:", 1, TXT_COLOR)

    screen.blit(nearest_ship, (M_WIDTH - 100,
                M_HEIGHT - t_angle_lbl.get_height() - fps_lbl.get_height() - 30))
    screen.blit(fps_lbl, (M_WIDTH - (fps_lbl).get_width() - 10, M_HEIGHT - 30))

    # shows danger (word)
    dnger_lbl = font.render(f"Danger: ", 1, TXT_COLOR)
    screen.blit(dnger_lbl, (5, M_HEIGHT - 30))

    # shows (target) word
    typingW = font.render(f"Target:", 1, TXT_COLOR)

    # updates word being looked at using color
    typingW2 = font.render(target_Var, 1, [255, 22, 12])

    # updates lives
    typing_lbl = font.render(f"Lives: {livesVar}", 1, TXT_COLOR)
    screen.blit(typing_lbl, (5, M_HEIGHT -
                typing_lbl.get_height() - typingW.get_height() - 30))
    screen.blit(typingW, (5, M_HEIGHT - typing_lbl.get_height() - 30))

    dnger_lbl = header.render(f"Level: {lvl_Var}", 1, TXT_COLOR)
    screen.blit(dnger_lbl, (5, 5))
    screen.blit(typingW2, (typingW.get_width() + 10,
                M_HEIGHT - typing_lbl.get_height() - 30))


def measureDistance():
    global displayDistance

    # Define danger thresholds
    HIGH_DANGER_THRESHOLD = 300
    MEDIUM_DANGER_THRESHOLD = 600

    # Initialize shortest distance to a large number
    shortest = float('inf')

    # Calculate the shortest distance to any enemy
    player_position = (player_X_Pos, player_Y_Pos)
    for enemy in enemy_List:
        enemy_position = (enemy.getX() + 20, enemy.getY() + 20)
        tempDist = math.hypot(player_position[0] - enemy_position[0],
                              player_position[1] - enemy_position[1])
        shortest = min(shortest, tempDist)

    # Determine the danger level based on the shortest distance
    if shortest < HIGH_DANGER_THRESHOLD:
        danger_text = "High"
        danger_color = (255, 0, 0)
    elif shortest < MEDIUM_DANGER_THRESHOLD:
        danger_text = "Medium"
        danger_color = (255, 127, 0)
    else:
        danger_text = "Safe"
        danger_color = (0, 255, 0)

    dangerLvl = font.render(danger_text, True, danger_color)
    screen.blit(dangerLvl, (100, M_HEIGHT - 30))

    # Set the global displayDistance to the shortest distance
    displayDistance = shortest


# gets the newest positon
def getNewPos(preX, preY, speed, angleInRad):
    # Calculate the change in position
    delta_x = speed * math.cos(angleInRad)
    delta_y = speed * math.sin(angleInRad)

    # Calculate the new position
    new_x = preX + delta_x
    new_y = preY + delta_y

    return new_x, new_y


'''
This part of the code turns the ship. It turns the ship by an angle.
'''


def turnShpByAngl(image, angle, xPos, yPos):
    # 0 is top, -90 -> -180 right, 90 -> 180 is left
    rotated_image = pygame.transform.rotate(image, round(angle))
    new_rect = rotated_image.get_rect(
        center=image.get_rect(center=(xPos, yPos)).center)
    return rotated_image, new_rect


"""
this part of the code turns the bullet by the angle, which is calculated
by the rotated image and also turns the player and enemy ships by thier ange
args: takes in 4 and returns the rotated image and new rect angle
"""


def turn_bul_byAngle(bulletImg, angle, xPosition, yPosition):
    # 0 is top, -90 -> -180 right, 90 -> 180 is left
    rotated_image = pygame.transform.rotate(bulletImg, angle)
    new_rect = rotated_image.get_rect(
        center=bulletImg.get_rect(center=(xPosition, yPosition)).center)
    return rotated_image, new_rect


def turnBul(bullet):
    rotatedImage, bulletRectangle = turn_bul_byAngle(
        bullet.getImage(), bullet.getAngle(), bullet.getX(), bullet.getY())
    screen.blit(rotatedImage, bulletRectangle.center)  # blit top left


def createBul(enemyShipFacing):
    bulSpawnX = (M_WIDTH/2)
    bulSpawnY = player_Y_Pos - 30
    bulWid = LAZER.get_width()
    bulHgt = LAZER.get_height()
    bulSpeed = -80
    bulletAngleRoute = enemyShipFacing.getAngle()
    bulFired = bullet.bulletInfo(LAZER, bulSpawnX, bulSpawnY,
                                 bulWid, bulHgt, bulSpeed, bulletAngleRoute, enemyShipFacing)
    current_Lazers_List.append(bulFired)


def turnIMG(obj, img, angle, x, y):
    rotated_image = pygame.transform.rotate(img, -angle+90)
    obj.setAngle(-angle+90)
    new_rect = rotated_image.get_rect(
        center=img.get_rect(center=(x, y)).center)
    return rotated_image, new_rect


def turnEnmyShowWrd(obj, objX, objY):
    word = font.render(obj.getWord(), True, obj.getColor())

    # turn radian angle into degrees
    theDegrees = math.degrees(math.atan2(objY-obj.getY(), objX-obj.getX()))
    rotated_image, new_rect = turnIMG(obj, obj.getImage(), theDegrees,
                                      obj.getX()+obj.getWidth()/2, obj.getY()+obj.getHeight()/2)
    screen.blit(rotated_image, new_rect.topleft)
    if (obj.getY() > -100):
        screen.blit(word, (obj.getX(), obj.getY()+60))


def clearScreen(numb):
    # 0 uses emp blast
    # 1 does not use emp blast
    global EMP_Stored
    shps2Del = []
    if (numb == 0):
        if (EMP_Stored > 0):
            EMP_Stored = EMP_Stored - 1
    for ship in enemy_List:
        if (ship.getY() > -100):  # ship is on screen
            shps2Del.append(ship)
    for temp in shps2Del:
        enemy_List.remove(temp)
    storedEMPs()


def main():
    fps = FPS()
    createDic()

    global EMP_Stored
    global score_Var
    global wrds_Typd
    global trajectoryAngle
    global livesVar
    global target_Var
    global lvl_Var

    global bg_Speed
    global score_Var

    global user
    global enemy_List

    enemy_Number = 0
    EMP_zoom = 40
    i = 0
    using_EMP = False

    # vars for EMP blast
    EMP_Center_X = player_X_Pos
    EMP_Center_Y = player_Y_Pos

    saveIndexOFSPACESHIPp = -1
    letter = ""
    letter2 = ""
    while True:
        if (livesVar == 0):
            sys.exit()

        # background image
        screen.fill((0, 0, 0))
        # controls

        screen.blit(BG_IMG, (0, 0))
        screen.blit(BG_IMG, (0, i))
        screen.blit(BG_IMG, (0, -(BG_IMG.get_height()) + i))
        if (i >= BG_IMG.get_height()):
            screen.blit(BG_IMG, (0, -(BG_IMG.get_height()) + i))
            i = 0
        i += bg_Speed

        screen.blit(bottomControls, (0, M_HEIGHT-100))
        screen.blit(topControls, (0, 0))

        # load in the player boundary and show the controls
        # show player boundaries
        pygame.draw.rect(screen, (0, 0, 0, 0), player_Boundaries, -1)
        # -1 for invisible

        # showFactsAndPlayer
        showFactsAndPlayer()

        # increase round when all ships are destroyed
        if (len(enemy_List) == 0):
            lvl_Var += 1
            enemy_Number += 1
            createShips(enemy_Number)

        # use EMP
        if (using_EMP):
            shockWave = pygame.image.load(
                os.path.join("Sprites", "shockWave.png"))
            shockWave = pygame.transform.scale(shockWave, (EMP_zoom, EMP_zoom))
            screen.blit(shockWave, (EMP_Center_X, EMP_Center_Y))
            EMP_zoom += 10
            EMP_Center_X -= 5
            EMP_Center_Y -= 5.5
            if EMP_Center_Y < (M_HEIGHT * 0.7):
                EMP_zoom = 600
                using_EMP = False
                # reset EMP vars
                EMP_Center_X = player_X_Pos
                EMP_Center_Y = player_Y_Pos


# -------# loop through enemy objects and make them travel at an angle

    # this part of hte code loops through the ships and gets thier positions
    # this for loop then sets the x and y position after measuring the distance
        for currEnmy in enemy_List:
            measureDistance()
            XPosEnemy = 0
            YPosEnemy = 0

            angleInRadians = math.atan2(
                player_Y_Pos - currEnmy.getY(), player_X_Pos - currEnmy.getX())
            angleInRaidansForBullets = math.atan2(player_Y_Pos - currEnmy.getY() - (
                currEnmy.getHeight()/2), player_X_Pos - currEnmy.getX() - (currEnmy.getWidth()/2))
            currEnmy.setRadians(angleInRaidansForBullets)
            XPosEnemy, YPosEnemy = getNewPos(
                currEnmy.getX(), currEnmy.getY(), currEnmy.getAcceleration(), angleInRadians)
            currEnmy.setX(XPosEnemy)
            currEnmy.setY(YPosEnemy)

            turnEnmyShowWrd(currEnmy, player_X_Pos, player_Y_Pos)

            enemyRect = pygame.Rect(
                currEnmy.getX(), currEnmy.getY(), currEnmy.getWidth(), currEnmy.getHeight())

            if enemyRect.colliderect(player_Boundaries):
                createShips(len(enemy_List))
                clearScreen(0)
                livesVar -= 1
                target_Var = ""

# -------# event handeler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if (pygame.key.name(event.key) == 'return'):
                    if (EMP_Stored >= 1):
                        target_Var = ""
                        using_EMP = True
                        EMP_zoom = 60
                        EMP_Center_X = player_X_Pos
                        EMP_Center_Y = player_Y_Pos
                        trajectoryAngle = 0
                        clearScreen(0)  # len(enemy_List) is set to 0

                # first get # spcShp.getWord() (word from the enemy class)
                # then get  # [0:1] (the first character from the word)

                # only start looping when target_Var is empty
                letter = str(event.unicode)
                if len(target_Var) == 0 and letter.isalpha() == True:
                    for counter, enemySHIPobj in enumerate(enemy_List):
                        if letter == enemy_List[counter].getWord()[0:1]:

                            # next 3 lines are for removing the letter hit from each word
                            enemy_List[counter].setWord(
                                enemy_List[counter].getWord()[1:])
                            target_Var = enemy_List[counter].getWord()

                            # THE COLOR OF THE WORDS
                            enemy_List[counter].setColor([255, 165, 0])
                            # bullet hit

                            # the second we find a ship word we break out of the loop
                            saveIndexOFSPACESHIPp = counter

                            # add bullet when a key is typed & letter is removed from the word
                            createBul(enemySHIPobj)
                            break

                letter2 = str(event.unicode)
                if len(target_Var) > 0:

                    while letter2 == enemy_List[saveIndexOFSPACESHIPp].getWord()[0:1] and len(enemy_List) > 0 and saveIndexOFSPACESHIPp < len(enemy_List):
                        enemy_List[saveIndexOFSPACESHIPp].setWord(
                            enemy_List[saveIndexOFSPACESHIPp].getWord()[1:])
                        target_Var = enemy_List[saveIndexOFSPACESHIPp].getWord(
                        )
                        createBul(enemySHIPobj)

                        if (len(target_Var) == 0 and saveIndexOFSPACESHIPp < len(enemy_List)):
                            del enemy_List[saveIndexOFSPACESHIPp]
                            target_Var = ""
                            score_Var += 100
                            wrds_Typd += 1
                            break

# -------# if lazers have spawned
        if (len(current_Lazers_List) > 0):

            # loop each lazer & check for collisions with enemies
            for shot in current_Lazers_List:

                # automatically remove bullet if it goes off the screen
                if (shot.getY() < 0 or shot.getX() < 0 or shot.getY() > M_HEIGHT or shot.getX() > M_WIDTH):
                    current_Lazers_List.remove(shot)

                enemyship = shot.getShipHeadedTowards()
                target_EnemyRect = pygame.Rect(
                    enemyship.getX(), enemyship.getY(), enemyship.getWidth(), enemyship.getHeight())
                bulletBorder = pygame.Rect(
                    shot.getX(), shot.getY(), shot.getWidth(), shot.getHeight())

                # bullet hit something
                if (target_EnemyRect.colliderect(bulletBorder)):
                    if shot in current_Lazers_List and len(current_Lazers_List) > 0:
                        current_Lazers_List.remove(shot)

                bulletX, bulletY = getNewPos(
                    shot.getX(), shot.getY(), shot.getSpeed(), enemyship.getRadians())

                shot.setX(bulletX)
                shot.setY(bulletY)
                turnBul(shot)

        fps.render(screen)
        fps.clock.tick(total_FPS)

        # update everything in pygame
        pygame.display.update()

        # if cross is clicked, the window closes
main()
