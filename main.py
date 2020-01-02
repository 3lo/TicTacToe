import sys
import pygame
pygame.init()  # initiates pygame function

print("Tic Tac Toe")
size = width, height = 320, 240
white = 255, 255, 255
black = 0, 0, 0
red = 255, 0, 0
cyan = 0, 255, 255

screen = pygame.display.set_mode(size)  # resolution of the game
pygame.display.set_caption("Tic Tac Toe")  # title of window
clock = pygame.time.Clock()  # frames per second (game clock)
turn = True


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def players():
    player1 = "X"
    player2 = "O"
    if turn is True:
        return player1
    elif turn is False:
        return player2


class Tiles:
    def __init__(self, area, color, player):
        self.area = area  # area of rectange position [x, y, width, height]
        self.color = color  # color of the tile (black = inactive) (white = active)
        self.player = player  # which player is there? X or O


def scoreboard(score1, score2):
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 1: " + str(score1), smallText)
    textRect.center = (53, 12)
    pygame.draw.rect(screen, red, pygame.Rect(0, 0, 320, 50))
    screen.blit(textSurf, textRect)

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects("Player 2: " + str(score2), smallText)
    textRect.center = (53, 35)
    screen.blit(textSurf, textRect)


def background():
    pygame.draw.rect(screen, topRowLeftTile.color, topRowLeftTile.area)  # upper left square
    pygame.draw.rect(screen, midRowLeftTile.color, midRowLeftTile.area)  # middle left square
    pygame.draw.rect(screen, botRowLeftTile.color, botRowLeftTile.area)  # lower left square

    pygame.draw.rect(screen, topRowMidTile.color, topRowMidTile.area)  # upper center square
    pygame.draw.rect(screen, midRowMidTile.color, midRowMidTile.area)  # middle center square
    pygame.draw.rect(screen, botRowMidTile.color, botRowMidTile.area)  # lower center square

    pygame.draw.rect(screen, topRowRightTile.color, topRowRightTile.area)  # upper right square
    pygame.draw.rect(screen, midRowRightTile.color, midRowRightTile.area)  # middle right square
    pygame.draw.rect(screen, botRowRightTile.color, botRowRightTile.area)  # lower right square


border_list = []


def set_player(border):
    if border.area not in border_list:
        border_list.append(border.area)

        pygame.draw.rect(screen, white, border.area)
        smallText = pygame.font.Font("freesansbold.ttf", 50)
        textSurf, textRect = text_objects(players(), smallText)
        textRect.center = ((border.area[0] + (106 / 2)), (border.area[1] + (63 / 2)))
        screen.blit(textSurf, textRect)

        border.player = players()

        wins = border.area, border.player
        check_winner(wins)


# data storage for winner checking
# horizontal rows
top_row = []
middle_row = []
bottom_row = []
# veritcal rows
first_column = []
sec_column = []
third_column = []
# diagonals
forward_slash = []  # /
back_slash = []  # \


def winner(pos):
    area = pos[0][0], pos[1][0], pos[2][0]
    print(area)
    if "O" not in pos:
        print("WINNER: PLAYER 1!")
        scoreboard(1, 0)
        game_finished(area)
    elif "X" not in pos:
        print("WINNER: PLAYER 2!")
        game_finished(area)
    elif len(border_list) == 9 and "X" in pos and "O" in pos:
        print("The game is a tie!")


def game_finished(area):
    print("The game is over!")
    for i in range(len(area)):
        pygame.draw.rect(screen, cyan, area[i], 3)


def check_winner(data):
    # horizontal rows
    if data[0][1] == 50:
        top_row.append(data)
        if len(top_row) == 3:
            winner(top_row)
    elif data[0][1] == 114:
        middle_row.append(data)
        if len(middle_row) == 3:
            winner(middle_row)
    elif data[0][1] == 178:
        bottom_row.append(data)
        if len(bottom_row) == 3:
            winner(bottom_row)
    # vertical rows
    if data[0][0] == 0:
        first_column.append(data)
        if len(first_column) == 3:
            winner(first_column)
    elif data[0][0] == 107:
        sec_column.append(data)
        if len(sec_column) == 3:
            winner(sec_column)
    elif data[0][0] == 214:
        third_column.append(data)
        if len(third_column) == 3:
            winner(third_column)
    # forward slash diagonal
    if data[0][0] == 0 and data[0][1] == 178 or data[0][0] == 107 and data[0][1] == 114 or data[0][0] == 214 \
            and data[0][1] == 50:
        forward_slash.append(data)
        if len(forward_slash) == 3:
            winner(forward_slash)
    # back slash diagonal
    if data[0][0] == 0 and data[0][1] == 50 or data[0][0] == 107 and data[0][1] == 114 or data[0][0] == 214 \
            and data[0][1] == 178:
        back_slash.append(data)
        if len(back_slash) == 3:
            winner(back_slash)


topRowLeftTile = Tiles((0, 50, 106, 63), black, None)
topRowMidTile = Tiles((107, 50, 106, 63), black, None)
topRowRightTile = Tiles((214, 50, 106, 63), black, None)

midRowLeftTile = Tiles((0, 114, 106, 63), black, None)
midRowMidTile = Tiles((107, 114, 106, 63), black, None)
midRowRightTile = Tiles((214, 114, 106, 63), black, None)

botRowLeftTile = Tiles((0, 178, 106, 63), black, None)
botRowMidTile = Tiles((107, 178, 106, 63), black, None)
botRowRightTile = Tiles((214, 178, 106, 63), black, None)


def clicked():
    if 0 + 106 > mouse[0] > 0 and 50 + 63 > mouse[1] > 50:  # inside the area of square1 - mouse = (x, y)
        set_player(topRowLeftTile)
    elif 0 + 106 > mouse[0] > 0 and 114 + 63 > mouse[1] > 114:
        set_player(midRowLeftTile)
    elif 0 + 106 > mouse[0] > 0 and 178 + 63 > mouse[1] > 178:
        set_player(botRowLeftTile)
    elif 107 + 106 > mouse[0] > 107 and 50 + 63 > mouse[1] > 50:
        set_player(topRowMidTile)
    elif 107 + 106 > mouse[0] > 107 and 114 + 63 > mouse[1] > 114:
        set_player(midRowMidTile)
    elif 107 + 106 > mouse[0] > 107 and 178 + 63 > mouse[1] > 178:
        set_player(botRowMidTile)
    elif 214 + 106 > mouse[0] > 214 and 50 + 63 > mouse[1] > 50:
        set_player(topRowRightTile)
    elif 214 + 106 > mouse[0] > 214 and 114 + 63 > mouse[1] > 114:
        set_player(midRowRightTile)
    elif 214 + 106 > mouse[0] > 214 and 178 + 63 > mouse[1] > 178:
        set_player(botRowRightTile)


screen.fill(white)
pygame.draw.rect(screen, red, pygame.Rect(0, 0, 320, 50))  # x, y, width, height - scoreboard
background()
scoreboard(0, 0)

while 1:
    mouse = pygame.mouse.get_pos()  # gets mouse position
    click = pygame.mouse.get_pressed()  # gets mouse clicks

    for event in pygame.event.get():  # gets any event that happens (mouse movement, clicks, key presses)
        if event.type == pygame.QUIT:  # exited the window quits program
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and mouse[1] > 50:  # add condition for areas that have been clicked
            clicked()  # click the same area twice and the next area can be the same player
            if turn is True:
                turn = False
            else:
                turn = True

    pygame.display.update()  # or pygame.display.flip()
    clock.tick(30)  # frames per second
