
import pygame, random, sys
pygame.init()

size = width, height = 800, 600

win = pygame.display.set_mode(size)
win.fill("dodgerblue2")
class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pygame.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


def redrawWindow():
    win.fill("dodgerblue4")
    greenButton.draw(win, (0,0,0 ))

run=True
greenButton = button("dodgerblue3",285, 235,225,150,"Start!")



 #activate the pygame library
# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()
clock = pygame.time.Clock()
# define the RGB value for white,
# green, blue colour .
white = (235,245,255)
green = (50,50,50)
blue = (0, 0, 128)
yellow =(255,200,0)
red = (255, 0 , 0)

# assigning values to X and Y variable
X = 800
Y = 600
winsound = pygame.mixer.Sound('win.mp3')
losesound = pygame.mixer.Sound('lose.mp3')
vupsound = pygame.mixer.Sound('vup.mp3')
finishsound = pygame.mixer.Sound('finish.mp3')
# create the display surface object
# of specific dimension..e(X, Y).
display_surface = pygame.display.set_mode((X, Y))

# set the pygame window name
pygame.display.set_caption('Memory Game - 18290088')

# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 32)



input_box = pygame.Rect(X // 2-100, Y //2 -16, 140, 36)
color_inactive = pygame.Color((200,190,140))
color_active = pygame.Color((200,200,200))
color = color_inactive
size = 5
key = True
active = False
done = False
text = ''
soru = True
key1 = False
# infinite loop
key2=True

while key:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        while run:
            redrawWindow()
            pygame.display.update()

            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if greenButton.isOver(pos):
                        run = False

                if event.type == pygame.MOUSEMOTION:
                    if greenButton.isOver(pos):
                        greenButton.color = "green"
                    else:
                        greenButton.color = "red"

        while soru == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    key = False
            san = font.render("Do you want to try again?(Y/N)", True, blue , "darkgrey")
            textRect = san.get_rect()
            textRect.center = (X // 2, Y // 2)
            display_surface.fill("darkgrey")
            display_surface.blit(san, textRect)
            pygame.display.update()
            clock.tick(30)
            pygame.time.delay(2000)

            done = False
            while not done:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # If the user clicked on the input_box rect.
                        if input_box.collidepoint(event.pos):
                            # Toggle the active variable.
                            active = not active
                        else:
                            active = False
                        # Change the current color of the input box.
                        color = color_active if active else color_inactive
                    if event.type == pygame.KEYDOWN:
                        if active:
                            if event.key == pygame.K_RETURN:
                                #print(text)
                                temp = text
                                text = ''
                                done = True
                            elif event.key == pygame.K_BACKSPACE:
                                text = text[:-1]
                            else:
                                text += event.unicode



                display_surface.fill(green)
                # Render the current text.
                txt_surface = font.render("Y/N : " + text, True, color)
                # Resize the box if the text is too long.
                width = max(200, txt_surface.get_width() + 10)
                input_box.w = width
                # Blit the text.
                display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
                # Blit the input_box rect.
                pygame.draw.rect(display_surface, color, input_box, 2)
                pygame.display.flip()
                clock.tick(30)

            if temp == "Y" or temp == "y":
                run=True
                size=5
                soru=True
                key1=True
                break
            elif temp == "N" or temp == "n":
                if size > 9:
                    san2 = font.render("Well Done!", True, blue, "darkgrey")
                    santext = san2.get_rect()
                    santext.center = (X // 2, (Y // 2)-36)
                else:
                    san2 = font.render("You can do better!", True, blue, "darkgrey")
                    santext = san2.get_rect()
                    santext.center = (X // 2, (Y // 2) - 36)
                san = font.render("Your score is:" + str(size-5), True, blue, "darkgrey")
                textRect = san.get_rect()
                textRect.center = (X // 2, Y // 2)
                display_surface.fill("darkgrey")
                display_surface.blit(san2, santext)
                display_surface.blit(san, textRect)

                finishsound.play()
                pygame.display.update()
                clock.tick(30)
                pygame.time.delay(11000)
                key = False
                soru=True
                break
            else:
                soru=False
                continue

        if key == False:
            break

        if key1==True:
            key1=False
            continue

        all = ''
        for i in range(size):
            pygame.time.delay(1000)
            rx = random.randint(32, X-32)
            ry = random.randint(32, Y-32)
            num = random.randint(0, 9)
            san = font.render(str(num), True, blue, "darkgrey")
            all += str(num)
            if i != size-1:
                all += ' '
            textRect = san.get_rect()

            textRect.center = (rx, ry)


            display_surface.fill("darkgrey")

            display_surface.blit(san, textRect)
            san = ""
            vupsound.play()
            pygame.display.update()
            clock.tick(30)
        pygame.time.delay(1000)


        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            #print(text)
                            temp=text
                            text = ''
                            done = True
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            display_surface.fill(green)
            # Render the current text.
            txt_surface = font.render("Numbers: " + text, True, color)
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            # Blit the text.
            display_surface.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(display_surface, color, input_box, 2)
            pygame.display.flip()
            clock.tick(30)


        if str(temp) == str(all):
            size += 1
            san = font.render("Correct!", True, yellow, green)
            textRect = san.get_rect()
            textRect.center = (X // 2, Y // 2)
            display_surface.fill(green)
            display_surface.blit(san, textRect)
            winsound.play()
            pygame.display.update()
            clock.tick(30)
            pygame.time.delay(2500)
        else:
            soru = False
            san = font.render("Wrong!", True, white, red)
            num = font.render("True combination of numbers: " , True , white,red)
            san3 = font.render(all, True, white, red)
            sanrext = san3.get_rect()
            sanrext.center = (X // 2, (Y // 2) +36)

            numconfig = num.get_rect()
            numconfig.center = (X // 2,(Y // 2))
            textRect = san.get_rect()
            textRect.center = (X // 2, (Y // 2)-36)
            display_surface.fill(red)
            display_surface.blit(san3, sanrext)
            display_surface.blit(san, textRect)
            display_surface.blit(num, numconfig)


            losesound.play()
            pygame.display.update()
            clock.tick(30)
            pygame.time.delay(5000)
